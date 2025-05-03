import os
import sqlite3
from datetime import datetime

UPLOAD_DIR = "uploads"
DB_PATH = "data/user_data.db"

CATEGORIES = ["lab_results", "mri_scans", "clinical_notes"]

def init_file_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS uploaded_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            category TEXT,
            filename TEXT,
            filepath TEXT,
            upload_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_file_metadata(username, category, filename, filepath, db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        INSERT INTO uploaded_files (username, category, filename, filepath, upload_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, category, filename, filepath, datetime.now().date()))
    conn.commit()
    conn.close()

def save_uploaded_file(username, category, uploaded_file):
    # Ensure upload path exists
    user_path = os.path.join(UPLOAD_DIR, username, category)
    os.makedirs(user_path, exist_ok=True)

    # Timestamped filename to avoid collisions
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{uploaded_file.name}"
    filepath = os.path.join(user_path, filename)

    # Save file
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Save metadata for search/filter
    save_file_metadata(username, category, filename, filepath)

    return filepath

def get_uploaded_files(username, db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        SELECT category, filename, filepath, upload_date
        FROM uploaded_files
        WHERE username=?
        ORDER BY upload_date DESC
    ''', (username,))
    records = [{"category": row[0], "filename": row[1], "filepath": row[2], "upload_date": row[3]} for row in c.fetchall()]
    conn.close()
    return records
