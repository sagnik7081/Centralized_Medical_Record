# Centralized_Medical_Record

# 🩺 Centralized Medical Record Repository

A lightweight and modular web application for organizing, summarizing, and visualizing personal medical records — built with Python and Streamlit.

---

## 🚀 Overview

Managing medical records can be messy and overwhelming. This application streamlines the process by allowing users to upload their medical PDFs, which are then:

- Categorized (e.g., prescriptions, test reports)
- Parsed for important details
- Summarized in plain language
- Visualized through interactive health trends

The goal is to make medical information more accessible and meaningful to both patients and healthcare professionals.

---

## ✨ Key Features

- 🔐 Secure user authentication (with hashed passwords)
- 📁 Upload and auto-categorize PDF medical records
- 🧠 Extract important data: symptoms, medicines, test outcomes
- 📝 Generate clean, readable summaries
- 📊 Interactive health data visualization using Plotly
- ⚙️ Fully modular codebase

---

## 🧰 Tech Stack

- **Frontend & Backend**: Python, Streamlit  
- **Database**: SQLite  
- **PDF Handling**: PyMuPDF  
- **Data Visualization**: Plotly  
- **Other Tools**: `dotenv`, `hashlib`, `re`, `os`, `pandas`, `datetime`

---

## 🗂️ Project Structure

```
📁 centralized-medical-repo/
│
├── auth.py             # Handles login and registration
├── file_manager.py     # File uploading and categorization
├── parser.py           # Extracts key info from PDFs
├── summarize.py        # Generates text summaries
├── plots.py            # Plots graphs using Plotly
├── main.py             # Streamlit app entry point
├── users.db            # SQLite database for credentials
├── requirements.txt    # Project dependencies
└── .env                # Environment variables
```

---

## 🛠️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/centralized-medical-repo.git
   cd centralized-medical-repo
   ```

2. **Set Up Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` File**
   ```
   SECRET_KEY=your_secret_key_here
   ```

5. **Run the App**
   ```bash
   streamlit run main.py
   ```
   "remember the patients name and username should be same"
---

## ⚠️ Known Challenges

- Inconsistent formatting across different medical PDFs made parsing and data extraction challenging.
- Fine-tuning regex logic for reliability took significant effort.

---

## 📌 Future Improvements

- Add cloud storage integration for multi-device access
- Support for image-based PDFs using OCR
- Multi-user dashboard for doctors and caregivers

---

## 🧑‍💻 Contributors

- Sagnik Ghosh
- Shantanu
- Shaurya Pratap Singh
- Vishal Singh  

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
