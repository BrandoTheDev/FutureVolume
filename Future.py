# Import necessary modules
import pandas as pd
import numpy as np
import argparse

# Function to read data from Excel
def read_data(file_path):
    # Read the Excel file into a pandas DataFrame
    data = pd.read_excel(file_path)
    return data

# Function to analyze volume trends for each day of the week
def analyze_trends(data):
    # Convert the 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    # Extract the day of the week from the 'Date' column
    data['DayOfWeek'] = data['Date'].dt.day_name()
    # Filter out days with zero volume (no operations)
    data = data[data['Volume'] > 0]
    # Calculate the average volume for each day of the week
    daily_avg = data.groupby('DayOfWeek')['Volume'].mean().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    return daily_avg

# Function to predict the volume for a day after a holiday
def predict_volume(daily_avg, day_after_holiday_date):
    # Convert the input date to datetime format
    day_after_holiday_date = pd.to_datetime(day_after_holiday_date)
    # Get the day of the week for the given date
    day_after_holiday = day_after_holiday_date.day_name()
    
    # Check if the given day is valid (i.e., not Sunday)
    if day_after_holiday not in daily_avg.index:
        raise ValueError("Invalid day of the week or no operations on this day")

    # Get the index of the day before the holiday
    holiday_index = daily_avg.index.get_loc(day_after_holiday) - 1
    
    # Handle case when the day before is Sunday (no operations)
    # If holiday_index is -1 (meaning the day after holiday is Monday), set to Saturday (last index)
    if holiday_index == -1:
        holiday_index = len(daily_avg) - 1
    
    # Increase the previous working day's volume by 50% to predict the volume after a holiday
    volume_after_holiday = daily_avg.iloc[holiday_index] + (daily_avg.iloc[holiday_index] * 0.5)
    
    return volume_after_holiday

# Main function to run the entire analysis and prediction
def main(file_path, day_after_holiday_date):
    # Read the data from the specified Excel file
    data = read_data(file_path)
    # Analyze the average volume trends for each day of the week
    daily_avg = analyze_trends(data)
    # Predict the volume for the specified day after a holiday
    predicted_volume = predict_volume(daily_avg, day_after_holiday_date)
    # Print the predicted volume
    print(f"Predicted volume for {day_after_holiday_date} after a holiday: {predicted_volume}")

if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Predict package volume after a holiday.')
    parser.add_argument('file_path', type=str, help='Path to the Excel file containing the data.')
    parser.add_argument('day_after_holiday_date', type=str, help='Date after the holiday (format: YYYY-MM-DD).')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Run the main function with the provided arguments
    main(args.file_path, args.day_after_holiday_date)
