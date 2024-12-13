import os
from pathlib import Path
from preprocessing import (
load_and_filter_zip_codes,
load_and_clean_crime_data,
process_and_merge_data,
retype_data,
save_cleaned_data
)
def main():
    # Define the project root directory dynamically
    project_root = Path(__file__).resolve().parent.parent

    # Construct absolute paths for data
    zip_file = project_root / "data" / "raw_data" / "zip.csv"
    crime_files = [
        project_root / "data" / "raw_data" / f"{year}.csv"
        for year in range(2020, 2025)
    ]
    processed_data_dir = project_root / "data" / "processed_data"

    columns_to_drop = ['block_address', 'BLOCK_ADDRESS', 'city', 
                       'City','badge_id', 'BADGE_ID', 'ObjectId', 
                       'nibrs_code', 'NIBRS_CODE','nibrs_group_name',
                       'UCR_HIERARCHY', 'LMPD_BEAT', 'lmpd_beat', 
                       'LMPD_DIVISION', 'lmpd_division',]
    columns_to_rename = {
        'ZIP_CODE' : 'zip',
        'zip_code': 'zip',
        'INCIDENT_NUMBER' : 'incident_number',
        'DATE_REPORTED': 'date_reported',
        'DATE_OCCURED': 'date_occurred',
        'CRIME_TYPE': 'offense_classification',
        'PREMISE_TYPE' : 'location_category',
        'ATT_COMP' : 'was_offense_completed',
        'UOR_DESC' : 'offense_code_name'
    }

    # Load and process ZIP codes
    load_and_filter_zip_codes(zip_file,  processed_data_dir)
    
    # Load and clean crime data
    crime_df = load_and_clean_crime_data(crime_files, columns_to_rename, columns_to_drop)
    
    # Merge and process data
    merged_data = process_and_merge_data(crime_df,  processed_data_dir)
    # Cast all data as proper type
    cleaned_data = retype_data(merged_data)
    # Save the final cleaned data
    save_cleaned_data(cleaned_data,  processed_data_dir)

if __name__ == "__main__":
    main()
