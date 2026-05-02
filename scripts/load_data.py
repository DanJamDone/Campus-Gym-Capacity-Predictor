import pandas as pd
import mysql.connector

# Load your CSV
df = pd.read_csv('data/raw/rutgers_gym_popular_times.csv')

# --- Feature engineering ---
df['hour_24'] = pd.to_datetime(df['Hour'], format='%I:%M %p').dt.hour
df['is_weekend'] = df['Day'].isin(['Saturday', 'Sunday'])


def label(pct):
    if pct < 40:
        return 'Low'
    elif pct < 70:
        return 'Medium'
    else:
        return 'High'


df['capacity_label'] = df['Estimated_Busyness_Percentage'].apply(label)

# --- Connect to MySQL ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rutgers_gym_db"
)
cur = conn.cursor()

# --- Insert gyms ---
gyms = df['Location'].unique()
gym_id_map = {}

for gym in gyms:
    cur.execute(
        "INSERT IGNORE INTO gyms (gym_name) VALUES (%s)",
        (gym,)
    )
    conn.commit()
    cur.execute("SELECT gym_id FROM gyms WHERE gym_name = %s", (gym,))
    gym_id_map[gym] = cur.fetchone()[0]

# --- Insert popular times rows ---
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO popular_times 
            (gym_id, day_of_week, hour, hour_24, is_weekend, busyness_pct, capacity_label)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        gym_id_map[row['Location']],
        row['Day'],
        row['Hour'],
        int(row['hour_24']),
        int(row['is_weekend']),
        int(row['Estimated_Busyness_Percentage']),
        row['capacity_label']
    ))

conn.commit()
cur.close()
conn.close()
print("Done! Data loaded successfully.")
