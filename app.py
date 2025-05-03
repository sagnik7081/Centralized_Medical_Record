import streamlit as st
from utils.auth import init_db, register_user, login_user
from utils.file_manager import save_uploaded_file, CATEGORIES, init_file_db, get_uploaded_files
from utils.parser import extract_and_save_metrics, init_metrics_db
from utils.plots import fetch_metrics, plot_metric_trend
from datetime import datetime

# Initialize DBs
init_db()
init_metrics_db()
init_file_db()

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'last_uploaded_filepath' not in st.session_state:
    st.session_state.last_uploaded_filepath = None
if 'last_uploaded_filename' not in st.session_state:
    st.session_state.last_uploaded_filename = None


def login_page():
    st.title("🩺 Centralized Medical Record Repository")
    st.subheader("Login or Register")

    tabs = st.tabs(["🔐 Login", "📝 Register"])

    with tabs[0]:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            if login_user(username, password):
                st.success("Login successful!")
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid credentials.")

    with tabs[1]:
        new_user = st.text_input("New Username", key="reg_user")
        new_pass = st.text_input("New Password", type="password", key="reg_pass")
        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("Registration successful! You can now log in.")
            else:
                st.error("Username already exists.")


def dashboard():
    st.sidebar.success(f"Logged in as: {st.session_state.username}")
    st.sidebar.title("🧭 Navigation")
    selection = st.sidebar.radio("Go to", ["🏠 Home", "📤 Upload Records", "📊 Trends", "📝 Summarize", "🔍 Search & Filter"])

    if selection == "🏠 Home":
        st.title("📁 Welcome to Your Health Portal")
        st.write("You can now upload and manage your medical records securely.")

    elif selection == "📤 Upload Records":
        st.title("📤 Upload Medical Records")
        st.markdown("Upload your documents and organize them by category.")

        category = st.selectbox("Select Category", CATEGORIES)
        uploaded_file = st.file_uploader("Choose a medical file", type=["pdf", "png", "jpg", "jpeg", "txt"])

        if uploaded_file is not None:
            filepath = save_uploaded_file(st.session_state.username, category, uploaded_file)
            st.session_state.last_uploaded_filepath = filepath
            st.session_state.last_uploaded_filename = uploaded_file.name
            st.success(f"File saved to: `{filepath}`")
            # Unified parsing for all formats
            metrics = extract_and_save_metrics(st.session_state.username, category, filepath)
            if metrics:
                st.info(f"Extracted and saved {len(metrics)} health metric(s) from this file.")
            else:
                st.info("No recognizable metrics found in this file.")

    elif selection == "📊 Trends":
        st.title("📊 Time-Series Trend Analysis")
        metric_name = st.selectbox("Select Metric", ["Hemoglobin", "Glucose", "CRP"])
        df = fetch_metrics(st.session_state.username, metric_name)
        fig = plot_metric_trend(df, metric_name)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available for this metric yet.")

    elif selection == "📝 Summarize":
        st.title("📝 Medical Report Summarization")
        st.markdown("Summarize your most recently uploaded file.")

        if st.session_state.last_uploaded_filepath:
            filepath = st.session_state.last_uploaded_filepath
            filename = st.session_state.last_uploaded_filename
            st.info(f"Summarizing: `{filename}`")

            groq_api_key = st.text_input("Enter your Groq API Key", type="password")

            if groq_api_key:
                import os
                from utils.parser import extract_text_from_txt, extract_text_from_pdf, extract_text_from_image
                ext = os.path.splitext(filepath)[1].lower()
                if ext == ".txt":
                    text = extract_text_from_txt(filepath)
                elif ext == ".pdf":
                    text = extract_text_from_pdf(filepath)
                elif ext in [".png", ".jpg", ".jpeg"]:
                    text = extract_text_from_image(filepath)
                else:
                    text = ""

                if text.strip():
                    from utils.summarize import summarize_text
                    with st.spinner("Summarizing..."):
                        summary = summarize_text(text, groq_api_key)
                    st.subheader("Summary:")
                    st.success(summary)
                    st.session_state.chat_history.append({
                        "filename": filename,
                        "summary": summary
                    })
                else:
                    st.warning("No text could be extracted from this file.")

            
            if st.session_state.chat_history:
                st.divider()
                st.subheader("🗂️ Previous Summaries This Session")
                for i, item in enumerate(st.session_state.chat_history[::-1], 1):
                    st.markdown(f"**{i}. File:** `{item['filename']}`")
                    st.info(item["summary"])
        else:
            st.warning("Please upload a file first in 'Upload Records'.")

    elif selection == "🔍 Search & Filter":
        st.title("🔍 Search & Filter Medical Records")
        st.markdown("Find your records by keyword, category, or upload date.")

        # Inputs for filtering
        keyword = st.text_input("Keyword (filename or notes)")
        category = st.selectbox("Category", ["All"] + CATEGORIES)
        date = st.date_input("Uploaded After", value=None)

        # Fetch records from your metadata store
        records = get_uploaded_files(st.session_state.username)

        # Apply filters
        filtered = []
        for r in records:
            # Convert upload_date string to date for comparison
            rec_date = datetime.strptime(r['upload_date'], "%Y-%m-%d").date() if r['upload_date'] else None
            if category != "All" and r['category'] != category:
                continue
            if keyword and keyword.lower() not in r['filename'].lower():
                continue
            if date and rec_date and rec_date < date:
                continue
            filtered.append(r)

        # Display results
        if filtered:
            for rec in filtered:
                st.markdown(f"- **{rec['filename']}** ({rec['category']}, {rec['upload_date']})")
        else:
            st.info("No records found matching your search.")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.session_state.last_uploaded_filepath = None
        st.session_state.last_uploaded_filename = None
        st.session_state.chat_history = []
        st.rerun()

# Routing
if st.session_state.logged_in:
    dashboard()
else:
    login_page()
