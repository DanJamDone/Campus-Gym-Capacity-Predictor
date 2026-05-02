import pandas as pd
from pathlib import Path

# File paths
RAW_PATH = Path("data/raw/rutgers_gym_popular_times.csv")
PROCESSED_PATH = Path("data/processed/rutgers_gym_cleaned.csv")


def label_capacity(percent):
    """
    Converts a busyness percentage into a category.
    """
    if percent < 40:
        return "Low"
    elif percent < 70:
        return "Medium"
    else:
        return "High"


def standardize_gym_name(name):
    """
    Makes gym names consistent.
    """
    if pd.isna(name):
        return "Unknown"

    name = str(name).strip().lower()

    gym_map = {
        "cag": "College Avenue Gym",
        "college ave gym": "College Avenue Gym",
        "college avenue gym": "College Avenue Gym",

        "livi rec": "Livingston Recreation Center",
        "livingston rec": "Livingston Recreation Center",
        "livingston recreation center": "Livingston Recreation Center",
        "livi": "Livingston Recreation Center",

        "sonny": "Sonny Werblin Recreation Center",
        "werblin": "Sonny Werblin Recreation Center",
        "sonny werblin": "Sonny Werblin Recreation Center",
        "sonny werblin recreation center": "Sonny Werblin Recreation Center",
        "busch": "Sonny Werblin RecreationCenter",

        "cook doug": "Cook/Douglass Recreation Center",
        "cook/douglass": "Cook/Douglass Recreation Center",
        "cook/douglass recreation center": "Cook/Douglass Recreation Center",
        "cook/doug": "Cook/Douglass Recreation Center",
        "cook/doug recreation center": "Cook/Douglass Recreation Center",
    }

    return gym_map.get(name, name.title())


def main():
    print("Loading raw gym data...")

    # Loads the raw CSV
    df = pd.read_csv(RAW_PATH)

    print(f"Raw rows loaded: {len(df)}")
    print("Original columns:", df.columns.tolist())

    # Removes duplicate rows
    before_duplicates = len(df)
    df = df.drop_duplicates()
    after_duplicates = len(df)

    # Standardize gym & day names
    df["Location"] = df["Location"].apply(standardize_gym_name)
    df["Day"] = df["Day"].astype(str).str.strip().str.title()

    # Convert hour from text format into military time (24 hr format)
    df["hour_24"] = pd.to_datetime(df["Hour"], format="%I:%M %p").dt.hour

    # Make sure busyness percentage is a number
    df["Estimated_Busyness_Percentage"] = pd.to_numeric(
        df["Estimated_Busyness_Percentage"],
        errors="coerce"
    )

    # Remove impossible busyness percentages
    df = df[
        (df["Estimated_Busyness_Percentage"] >= 0)
        & (df["Estimated_Busyness_Percentage"] <= 100)
    ]

    # Add weekend feature (more synthetic data)
    df["is_weekend"] = df["Day"].isin(["Saturday", "Sunday"])

    # Add semester week
    # Creates a realistic semester week column
    df["semester_week"] = ((df.index // 25) % 15) + 1

    # Add exam week feature
    # Treating weeks 14 and 15 as exam weeks
    df["is_exam_week"] = df["semester_week"].isin([14, 15])

    # Add weather feature.
    # This is synthetic because our raw data does not include weather.
    df["weather"] = "clear"
    df.loc[df["Day"].isin(["Monday", "Wednesday"]), "weather"] = "rain"

    # Add capacity label
    df["capacity_label"] = df["Estimated_Busyness_Percentage"].apply(label_capacity)

    # Rename columns to cleaner database-friendly names
    df = df.rename(columns={
        "Location": "gym_name",
        "Day": "day_of_week",
        "Hour": "hour",
        "Estimated_Busyness_Percentage": "busyness_percent"
    })

    # Fill any remaining missing values
    df["weather"] = df["weather"].fillna("clear")
    df["gym_name"] = df["gym_name"].fillna("Unknown")
    df["day_of_week"] = df["day_of_week"].fillna("Unknown")

    # Make processed folder if it doesn't exist
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save cleaned dataset
    df.to_csv(PROCESSED_PATH, index=False)

    print("\nPreprocessing complete.")
    print(f"Rows before duplicate removal: {before_duplicates}")
    print(f"Rows after duplicate removal: {after_duplicates}")
    print(f"Final cleaned rows: {len(df)}")
    print(f"Missing values left: {df.isna().sum().sum()}")
    print(f"Cleaned file saved to: {PROCESSED_PATH}")


if __name__ == "__main__":
    main()