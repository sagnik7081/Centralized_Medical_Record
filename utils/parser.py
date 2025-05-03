import re
import sqlite3
from datetime import datetime
import os

# PDF extraction
from pypdf import PdfReader  # pip install pypdf
# Image OCR
from PIL import Image, ImageOps, ImageFilter  # pip install pillow
import pytesseract  # pip install pytesseract

import mimetypes

def is_pdf(filepath):
    mime, _ = mimetypes.guess_type(filepath)
    return mime == "application/pdf"


DB_PATH = "data/user_data.db"

def init_metrics_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            category TEXT,
            metric_name TEXT,
            metric_value REAL,
            date DATE,
            file_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

from pypdf import PdfReader

def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += "\n" + page_text
        return text
    except Exception as e:
        print(f"PDF extraction failed: {e}")
        return ""

from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf_with_ocr(file_path):
    try:
        # Try standard extraction first
        text = extract_text_from_pdf(file_path)
        if text.strip():
            return text
        # If no text, try OCR
        pages = convert_from_path(file_path)
        ocr_text = ""
        for page in pages:
            ocr_text += pytesseract.image_to_string(page)
        return ocr_text
    except Exception as e:
        print(f"OCR PDF extraction failed: {e}")
        return ""



def extract_text_from_image(file_path):
    image = Image.open(file_path)
    # Preprocess for better OCR accuracy
    gray_image = ImageOps.grayscale(image)
    resized_image = gray_image.resize(
        (gray_image.width * 2, gray_image.height * 2),
        resample=Image.LANCZOS
    )
    thresholded_image = resized_image.filter(ImageFilter.FIND_EDGES)
    text = pytesseract.image_to_string(thresholded_image)
    return text

def extract_metrics_from_text(text):
    metric_patterns = {
        'Hemoglobin': r'Hemoglobin[:\s]+([\d.]+)\s*g/dL',
        'Glucose': r'Glucose[:\s]+([\d.]+)\s*mg/dL',
        'CRP': r'CRP[:\s]+([\d.]+)\s*mg/L'
    }
    metrics = []
    for metric, pattern in metric_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            metrics.append({
                'metric_name': metric,
                'metric_value': float(match.group(1)),
                'date': datetime.now().date()
            })
    return metrics

def save_metrics_to_db(username, category, metrics, file_path, db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for m in metrics:
        c.execute('''
            INSERT INTO metrics (username, category, metric_name, metric_value, date, file_path)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            username, category, m['metric_name'], m['metric_value'],
            m['date'], file_path
        ))
    conn.commit()
    conn.close()

def extract_and_save_metrics(username, category, file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        text = extract_text_from_txt(file_path)
    elif ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext in [".png", ".jpg", ".jpeg"]:
        text = extract_text_from_image(file_path)
    else:
        text = ""
    metrics = extract_metrics_from_text(text)
    print(f"Extracted metrics: {metrics}")  # ✅ DEBUG PRINT
    if metrics:
        save_metrics_to_db(username, category, metrics, file_path)
    return metrics

def get_saved_metrics(username=None, category=None, db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    query = "SELECT metric_name, metric_value, date, file_path FROM metrics"
    params = []
    conditions = []

    if username:
        conditions.append("username = ?")
        params.append(username)
    if category:
        conditions.append("category = ?")
        params.append(category)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    c.execute(query, params)
    results = c.fetchall()
    conn.close()
    return results
