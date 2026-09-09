from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
# A secret key is required by Flask to securely sign session cookies
app.secret_key = 'super_secret_key_for_project' 

DB_NAME = 'potholes.db'

def get_db_connection():
    """Helper function to connect to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row # This allows us to access columns by name
    return conn

@app.route('/')
def index():
    """Redirects users based on their login status."""
    if 'logged_in' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles the login form rendering and submission."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        # Check if the user exists in our database (admin/admin123 created in Module 1)
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                            (username, password)).fetchone()
        conn.close()
        
        if user:
            session['logged_in'] = True
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Clears the session and logs the user out."""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    """A protected route for the main dashboard."""
    if 'logged_in' not in session:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('login'))
        
    return render_template('dashboard.html')

if __name__ == '__main__':
    # debug=True automatically reloads the server when you make code changes
    app.run(debug=True)