# FutureVolume
Predict the future volume of a day

### Terminal Usage:

    python3 Future.py file_path day_after_holiday_date
    
    arguments:
        file_path                 Path to the Excel file containing the data.
        day_after_holiday_date    Date after the holiday (format: YYYY-MM-DD).
        
    options: 
        -h, --help                show the help message and exit

## Reading and Analyzing Data:

    The data is read from the Excel file.
    Days with zero volumes (holidays and Sundays) are filtered out.
    Average volumes for each day of the week are calculated from the remaining data.

## Average Volume Calculation:

    Average volumes for each day of the week are calculated (excluding Sunday):
        Monday: 7000
        Tuesday: 4200
        Wednesday: 4400
        Thursday: 4600
        Friday: 4700
        Saturday: 3950

## Prediction:

    The day after the holiday (July 5th) is a Friday.
    The previous working day is Wednesday (July 3rd), with an average volume of 4400.
    The predicted volume for July 5th is calculated as 4400 + (4400 * 0.5) = 6600.

### Screenshots
![Example of an excel sheet layout](https://github.com/BrandoTheDev/FutureVolume/blob/main/Screenshot%20from%202024-06-19%2023-27-54.png)
![Running the script in terminal](https://github.com/BrandoTheDev/FutureVolume/blob/main/Screenshot%20from%202024-06-19%2023-26-41.png)
