def main():
    from preprocessing import (
    load_and_filter_zip_codes,
    load_and_clean_crime_data,
    process_and_merge_data,
    retype_data,
    save_cleaned_data
)
    zip_file = "./data/raw_data/zip.csv"
    crime_files = [
        "./data/raw_data/2020.csv",
        "./data/raw_data/2021.csv",
        "./data/raw_data/2022.csv",
        "./data/raw_data/2023.csv",
        "./data/raw_data/2024.csv"
    ]
    
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
    jefferson_zip_df = load_and_filter_zip_codes(zip_file)
    
    # Load and clean crime data
    crime_df = load_and_clean_crime_data(crime_files, columns_to_rename, columns_to_drop)
    
    # Merge and process data
    merged_data = process_and_merge_data(crime_df)
    # Cast all data as proper type
    cleaned_data = retype_data(merged_data)
    # Save the final cleaned data
    save_cleaned_data(cleaned_data)

if __name__ == "__main__":
    main()
