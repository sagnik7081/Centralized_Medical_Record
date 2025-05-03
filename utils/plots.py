import pandas as pd
import sqlite3
import plotly.express as px
import os

DB_PATH = "data/user_data.db"
USER_FILE = "current_user.txt"  

def get_logged_in_username():
    if not os.path.exists(USER_FILE):
        print("No user is currently logged in.")
        return None
    with open(USER_FILE, "r") as f:
        username = f.read().strip()
    return username

def fetch_all_metric_names(username, db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT metric_name FROM metrics WHERE username=?", (username,))
    metric_names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return metric_names

def fetch_metrics(username, metric_name, db_path=DB_PATH, latest=False):
    conn = sqlite3.connect(db_path)
    query = "SELECT date, metric_value FROM metrics WHERE username=? AND metric_name=? ORDER BY date ASC"
    if latest:
        query = "SELECT date, metric_value FROM metrics WHERE username=? AND metric_name=? ORDER BY date DESC LIMIT 1"
    df = pd.read_sql_query(query, conn, params=(username, metric_name))
    conn.close()
    return df

def plot_metric_trend(df, metric_name):
    if df.empty:
        print(f"No data available for {metric_name}")
        return None
    fig = px.line(df, x='date', y='metric_value', title=f"{metric_name} Trend Over Time", markers=True)
    # Increase dot size by modifying marker size
    fig.update_traces(marker=dict(size=10))  # Adjust 'size' to make the dots bigger
    fig.update_xaxes(rangeslider_visible=True)
    fig.show()
    return fig

def plot_all_metrics_for_user(username):
    metric_names = fetch_all_metric_names(username)
    if not metric_names:
        print(f"No metrics found for user: {username}")
        return

    # Fetch the latest record for each metric if the user wants to see it
    for metric_name in metric_names:
        df = fetch_metrics(username, metric_name)
        plot_metric_trend(df, metric_name)

        # Ask user if they want to see the last record
        show_last_record = input(f"Do you want to see the last record for {metric_name}? (y/n): ").strip().lower()
        if show_last_record == 'y':
            last_record = fetch_metrics(username, metric_name, latest=True)
            if not last_record.empty:
                print(f"Last record for {metric_name}: {last_record}")
            else:
                print(f"No last record found for {metric_name}")

if __name__ == "__main__":
    username = get_logged_in_username()
    if username:
        plot_all_metrics_for_user(username)
