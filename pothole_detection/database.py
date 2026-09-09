import sqlite3
import os

DB_NAME = 'potholes.db'

def init_db():
    """
    Initializes the SQLite database and creates the required schema.
    Includes basic error handling if the file is locked or unavailable.
    """
    try:
        # Connect to the database (creates it if it doesn't exist)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create the main table as per the schema requirements
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS detections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_name TEXT NOT NULL,
                latitude REAL,
                longitude REAL,
                confidence REAL,
                pothole_count INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create a basic users table for the Login Module
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Insert a default admin user if none exists (Password: admin123)
        # Note: In a production app, use werkzeug.security to hash this!
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, password) 
            VALUES ('admin', 'admin123')
        ''')

        conn.commit()
        print(f"Database '{DB_NAME}' initialized successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred while setting up the database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    init_db()