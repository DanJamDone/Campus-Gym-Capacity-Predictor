# Campus Gym Capacity Predictor

## Project Overview

The **Campus Gym Capacity Predictor** is a data science and machine learning project designed to predict the busyness level of Rutgers University's main gym facilities on campus. The system analyzes historical gym utilization data to forecast capacity levels (Low, Medium, High), helping students and staff plan their gym visits efficiently.

## Team Members

- Arshdeep Singh, Danish Jamal, Hamdaan Mailk

## Problem Statement

Rutgers University students often struggle to find available time slots at campus gym facilities due to overcrowding during peak hours. This project addresses the need for predictive insights into gym capacity by:

- Analyzing historical patterns of gym utilization across different locations and times
- Building machine learning models to predict future capacity levels
- Enabling data-driven decision-making for gym visit planning

## Data Sources

- **Source**: Rutgers University gym popular times data from Google Maps
- **File**: `rutgers_gym_popular_times.csv`
- **Features**: 
  - Gym Location (College Avenue Gym, Livingston Rec Center, Sonny Werblin, Cook/Douglass Rec Center)
  - Day of the Week
  - Hour of Day
  - Estimated Busyness Percentage (0-100%)
  - Additional derived features: weekend indicator, semester week #, exam week indicator, weather conditions

## Project Structure

```
Campus-Gym-Capacity-Predictor/
│
├── README.md                          # Project documentation
│
├── data/
│   ├── raw/
│   │   └── rutgers_gym_popular_times.csv    # Raw gym utilization data
│   │
│   └── processed/
│       └── rutgers_gym_cleaned.csv           # Cleaned and preprocessed data
│
└── scripts/
    ├── load_data.py                   # Database loading and feature engineering
    └── preprocess.py                  # Data cleaning and preprocessing
```

## Setup Instructions

### Prerequisites
- Python 3.7+
- pandas
- scikit-learn
- mysql-connector-python
- MySQL Server (for database operations)

### Installation

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd Campus-Gym-Capacity-Predictor
   ```

2. **Install required dependencies**
   ```bash
   pip install pandas scikit-learn mysql-connector-python
   ```

3. **Data Preprocessing**
   - Place raw gym data in `data/raw/rutgers_gym_popular_times.csv`
   - Run the preprocessing script:
   ```bash
   python scripts/preprocess.py
   ```
   - Processed data will be saved to `data/processed/rutgers_gym_cleaned.csv`

4. **Load Data (Optional - for database)**
   ```bash
   python scripts/load_data.py
   ```
   - Ensure MySQL is running and configured with appropriate credentials in the script

## Results

### Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| [Model 1 Name] | [Accuracy]% | [Precision]% | [Recall]% | [F1-Score] |
| [Model 2 Name] | [Accuracy]% | [Precision]% | [Recall]% | [F1-Score] |
| [Best Model Name] | [Accuracy]% | [Precision]% | [Recall]% | [F1-Score] |

*Add your actual model comparison results above*

## Key Findings

### Feature Importance Analysis

Based on the feature importance analysis from the predictive models:

- **Most Important Features**:
  - [Add the top 3-5 features with their importance scores]
  
- **Insights**:
  - [Key insight 1: What patterns did the feature importance analysis reveal?]
  - [Key insight 2: How do seasonal patterns affect gym capacity?]
  - [Key insight 3: What times/days are consistently busier?]

### Model Performance Insights
- [Add insights about model performance and prediction quality]
- [Add any challenges encountered and how they were addressed]

## Next Steps and Future Improvements

- Deploy the model as a web service for real-time capacity predictions
- Integrate live gym data feeds
- Develop a mobile app for gym capacity alerts
- Incorporate additional features (e.g., weather, campus events, holidays)

---

**Last Updated**: May 2026
