# Crime Data Analysis Project

## Project Overview
This project analyzes crime data from Jefferson County, KY, spanning the years 2020 to 2024. The main focus is on processing, cleaning, and visualizing crime data, specifically related to auto thefts. The analysis merges crime data with ZIP code information and standardizes fields to prepare the data for insights and reporting. The motivation behind this project stems from my own vehicle theft during the first week of December, 2024. I had never met anyone who had dealt with this, and wanted to learn more about the prevalance of vehicle theft in my county. 

## Data Sources
- **Crime Data**: Raw crime data from 2020 to 2024 provided in CSV format.
- https://data.louisvilleky.gov/datasets/LOJIC::louisville-metro-ky-crime-data-2020/about
- https://data.louisvilleky.gov/datasets/LOJIC::louisville-metro-ky-crime-data-2021/about
- https://data.louisvilleky.gov/datasets/LOJIC::louisville-metro-ky-crime-data-2022/about
- https://data.louisvilleky.gov/datasets/LOJIC::louisville-metro-ky-crime-data-2023/about
- https://data.louisvilleky.gov/datasets/LOJIC::louisville-metro-ky-crime-data-2024/about

- **ZIP Codes**: ZIP code data for filtering relevant locations (Jefferson County, KY).
- https://www.unitedstateszipcodes.org/zip-code-database/
```
[x] Feature 1: Read TWO data files (JSON, CSV, Excel, etc.). 
```
## File Structure
- **`main.py`**: The main script that orchestrates data processing.
- **`preprocessing.py`**: Contains modular functions for loading, cleaning, and processing data.
```
[x] Feature 2: Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.  
```
- **`data/raw_data/`**: Folder containing raw crime data files.
- **`data/processed_data/`**: Folder containing processed data outputs.

## Steps to Reproduce
1. Clone the repository:
```
open new Git bash terminal in code editor
```
```bash
git clone https://github.com/matthewlondon/Capstone.git
```
2. Set up a virtual environment:

    [x] Feature 4: Utilize a virtual environment and include instructions in your README on how the user should set one up

```bash
python -m venv venv
```
```bash
source venv/bin/activate
```
if using Windows:
```bash
source venv\Scripts\activate
```
    
3. Install dependencies:
```bash
cd Capstone
```
```bash
pip install -r requirements.txt
```

4. Run the `main.py` script:
```bash
python src/main.py
```
5. Open the `exploration.ipynb` file:

6. Run all scripts to view matplot and seaborn visualizations:
```
[x] Feature 3: Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data.
```
    
        - Most Common Days for Reported Auto Thefts
        - Auto Theft Trends Over the Years
        - Top 10 ZIP Codes for Auto Thefts
        - Trends by Day of Week and Top 10 Locations
        - Yearly Trends by ZIP Code
        - Personal Analysis of My Car Theft Incident
        - Incidents per 100 People by ZIP Code
    
    

## Processed Data Outputs
- **`cleaned_crime_data.csv`**: Contains the cleaned and processed crime data.
- **`jefferson_zip_df.csv`**: Contains filtered ZIP code data for Jefferson County, KY.

## Data Dictionary
### Cleaned Crime Data
| Column Name               | Description                                             | Data Type   |
|---------------------------|---------------------------------------------------------|-------------|
| `zip`                    | ZIP code of the crime location.                        | String      |
| `incident_number`        | Unique identifier for each incident.                   | String      |
| `date_reported`          | Date when the crime was reported.                      | DateTime    |
| `date_occurred`          | Date when the crime occurred.                          | DateTime    |
| `offense_classification` | Standardized offense classification (e.g., AUTO THEFT).| Category    |
| `location_category`      | Category describing the crime location.                | Category    |
| `was_offense_completed`  | Whether the offense was completed (YES/NO/UNKNOWN).    | Category    |
| `value_range`            | Estimated monetary range associated with the offense.  | Category    |
| `week_day_reported`      | Day of the week the crime was reported.                | Category    |
| `week_day_occurred`      | Day of the week the crime occurred.                    | Category    |

### Jefferson County ZIP Data
| Column Name | Description                     | Data Type |
|-------------|---------------------------------|-----------|
| `zip`      | ZIP codes in Jefferson County, KY.| Integer   |
| `latitude`      | Coordinates| Float  |
| `longitude`      | Coordinates| Float   |
| `irs_estimated_population`      | 2020 population estimates based on exemption filings| Integer   |

## Visualizations
    - Most Common Days for Reported Auto Thefts
    - Auto Theft Trends Over the Years
    - Top 10 ZIP Codes for Auto Thefts
    - Trends by Day of Week and Top 10 Locations
    - Yearly Trends by ZIP Code
    - Personal Analysis of My Car Theft Incident
    - Incidents per 100 People by ZIP Code

## Contact
Matthew London - mmatthewlondon@gmail.com

