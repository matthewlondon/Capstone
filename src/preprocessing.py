import pandas as pd
import numpy as np


def load_and_filter_zip_codes(zip_file):
    
    zip_to_county_df = pd.read_csv(zip_file)
    filtered_df = zip_to_county_df[
    (zip_to_county_df['county'] == 'Jefferson County') & 
    (zip_to_county_df['state'] == 'KY')
    ].copy()

    # Clean and reset index
    filtered_df['zip'] = pd.to_numeric(filtered_df['zip'], errors='coerce').astype('Int64')
    filtered_df = filtered_df[['zip']].reset_index(drop=True)
    filtered_df.to_csv('./data/jefferson_zip_df.csv', index=False)

def load_and_clean_crime_data(file_paths, columns_to_rename, columns_to_drop):
    
    data_frames = []
    
    for file in file_paths:
        df = pd.read_csv(file, low_memory=False)
        
        # Drop unnecessary columns
        df.drop(columns=columns_to_drop, errors='ignore', inplace=True)
        
        # Rename columns
        df.rename(columns=columns_to_rename, inplace=True)

        # Filter relevant offenses
        df = df[df['offense_classification'].isin(['MOTOR VEHICLE THEFT', '14 AUTO THEFT'])].copy()
        df['offense_classification'] = 'AUTO THEFT'

        # Standardize and clean other columns
        df['was_offense_completed'] = df['was_offense_completed'].replace(
            {'COMPLETED': 'YES', 'ATTEMPTED': 'NO'}, regex=True
        ).fillna('UNKNOWN')

        df['location_category'] = df['location_category'].str.strip()
        df['zip'] = (
        df['zip']
        .astype(str)
        .str.strip()
        .str.split('-').str[0]
        .str.replace(r'\.0$', '', regex=True)
        .replace(['99999', 'nan', None, '', 'NaN'], pd.NA)
        )

        # Keep valid ZIP codes
        df = df[df['zip'].str.match(r'^\d{5}$', na=False)]
        df['zip'] = pd.to_numeric(df['zip'], errors='coerce').astype('Int64')
        data_frames.append(df)
    
    # Combine all data frames
    return pd.concat(data_frames, ignore_index=True)

def process_and_merge_data(crime_df):
    jefferson_zip_df = pd.read_csv('./data/jefferson_zip_df.csv')
    merged_df = jefferson_zip_df.merge(crime_df, how='inner', on='zip')

    # Clean and format date columns
    merged_df['date_reported'] = merged_df['date_reported'].str.strip()
    merged_df['date_reported'] = merged_df['date_reported'].str.replace('/', '-')
    merged_df['date_occurred'] = merged_df['date_occurred'].str.strip()
    merged_df['date_occurred'] = merged_df['date_occurred'].str.replace('/', '-')
    merged_df['date_reported'] = pd.to_datetime(merged_df['date_reported'], format='mixed', utc=True).dt.tz_localize(None)
    merged_df['date_occurred'] = pd.to_datetime(merged_df['date_occurred'], format='mixed', utc=True).dt.tz_localize(None)

    # Normalize monetary value ranges
    regex_pattern = (
        r"(< \$500|"
        r"\$500 < \$1,000|"
        r"\$500 < \$10,000|"
        r"\$1,000 < \$10,000|"
        r"\$10,000 < \$1,000,000|"
        r"\$1,000,000 < \$10,000,000|"
        r"\$10,000,000 OR MORE|"
        r"> \$500 BUT < \$10,000|"
        r"> \$10,000 BUT < \$1,000,000)"
    )
    merged_df['value_range'] = merged_df['offense_code_name'].str.extract(regex_pattern, expand=False)
    merged_df['value_range'] = merged_df['value_range'].replace({
        "> $500 BUT < $10,000": "$500 < $10,000",
        "> $10,000 BUT < $1,000,000": "$10,000 < $1,000,000"
    }).fillna("UNKNOWN RANGE")
    
    # Normalize location categories
    location_mapping = {
        'RESIDENCE/HOME' : 'RESIDENCE / HOME',
        'OTHERRESIDENCE(APARTMENT/CONDO)' : 'APARTMENT / CONDO',
        'NON-ATTACHEDRESDGARAGE/SHED/BULD' : 'GARAGE / SHED / OUTBUILDING',
        'ATTACHEDRESIDENTIALGARAGE' : 'GARAGE / SHED / OUTBUILDING',
        'PARKINGLOT/GARAGE' : 'PARKING LOT / GARAGE',
        'PARKING/DROPLOT/GARAGE' : 'PARKING LOT / GARAGE',
        'RESTAREA' : 'REST AREA',
        '"SPECIALTYSTORE(TV,FUR,ETC)"' : 'SPECIALTY STORE',
        'SPECIALTYSTORE' : 'SPECIALTY STORE',
        'SCHOOL-ELEMENTARY/SECONDARY' : 'SCHOOL',
        'SCHOOLCOLLEGE' : 'COLLEGE',
        'SCHOOL-COLLEGE/UNIVERSITY' : 'COLLEGE',
        'BANK/SAVINGSANDLOAN' : 'BANK',
        'OTHER/UNKOWN' : 'OTHER / UNKNOWN',
        'HOTEL/MOTEL/ETC.' : 'HOTEL / MOTEL',
        'CAMP/CAMPGROUND' : 'CAMPGROUND',
        'CEMETERY/GRAVEYARD' : 'CEMETERY',
        'FIELD/WOODS' : 'FIELD / WOODS',
        'SERVICE/GASSTATION' : 'GAS STATION',
        'CONVENIENCESTORE' : 'CONVENIENCE STORE',
        'BAR/NIGHTCLUB' : 'BAR / NIGHTCLUB',
        "DRUGSTORE/DOCTOR'SOFFICE/HOSPITAL" :  'DRUGSTORE / DR / HOSPITAL',
        'DRUGSTORE/DR`SOFFICE/HOSPITAL' : 'DRUGSTORE / DR / HOSPITAL',
        'HIGHWAY/ROAD/ALLEY/STREET/SIDEWALK' : 'ROAD / ALLEY / STREET',
        'HIGHWAY/ROAD/ALLEY' : 'ROAD / ALLEY / STREET',
        'RESTAURANT' : 'RESTAURANT',
        'AUTODEALERSHIP(NEWORUSED)' : 'AUTO DEALERSHIP',
        'AUTODEALERSHIPNEW/USED' : 'AUTO DEALERSHIP',
        'RENTALSTORAGEFACILITY' : 'STORAGE FACILITY',
        'RENTAL/STORAGEFACILITY' : 'STORAGE FACILITY',
        'SHOPPINGMALL' : 'MALL',
        'MALL/SHOPPINGCENTER' : 'MALL',
        'DAYCAREFACILITY' : 'DAYCARE FACILITY',
        'PARK/PLAYGROUND' : 'PARK / PLAYGROUND',
        'LIQUORSTORE' : 'LIQUOR STORE',
        'SHELTER-MISSION/HOMELESS' : 'HOMELESS SHELTER',
        'HOMELESSSHELTER/MISSION' : 'HOMELESS SHELTER',
        'CHURCH/SYNAGOGUE/TEMPLE/MOSQUE' : 'PLACE OF WORHSIP',
        'CHURCH/SYNAGOGUE/TEMPLE' : 'PLACE OF WORSHIP',
        'GROCERY/SUPERMARKET' : 'GROCERY STORE',
        'DOCK/WHARF/FREIGHT/MODALTERMINAL' : 'DOCK / WHARF / FREIGHT TERMINAL',
        'RACETRACK/GAMBLINGFACILITY' : 'RACETRACK / GAMBLING FACILITY',
        'GAMBLINGFACILITY/CASINO/RACETRACK' : 'RACETRACK / GAMBLING FACILITY',
        'FAIRGROUNDS/STADIUM/ARENA' : 'ARENA / STADIUM / FAIRGROUNDS',
        'ARENA/STADIUM/FAIRGROUNDS/COLISEUM' : 'ARENA / STADIUM / FAIRGROUNDS',
        'DEPARTMENT/DISCOUNTSTORE' : 'DEPARTMENT STORE',
        'COMMUNITYCENTER' : 'COMMUNITY STORE',
        'AIR/BUS/TRAINTERMINAL' : 'AIR / BUS / TRAIN TERMINAL',
        'ATMSEPARATEFROMBANK' : 'ATM',
        'AMUSEMENTPARK' : 'AMUSEMENT PARK',
        'ABANDONED/CONDEMNEDSTRUCTURE' : 'CONDEMNED STRUCTURE',
        'INDUSTRIALSITE' : 'INDUSTRIAL SITE',
        'GOVERNMENT/PUBLICBUILDING' : 'PUBLIC BUILDING',
        'COMMERCIAL/OFFICEBUILDING' : 'OFFICE BUILDING'
    }
    merged_df['location_category'] = merged_df['location_category'].replace(location_mapping)

    # Add weekday columns
    merged_df['week_day_reported'] = merged_df['date_reported'].dt.day_name()
    merged_df['week_day_occurred'] = merged_df['date_occurred'].dt.day_name()
    merged_df.drop(columns=["offense_code_name"], inplace=True)
    return merged_df

def retype_data(merged_df):
    merged_df['zip'] = merged_df['zip'].astype('string')
    merged_df['incident_number'] = merged_df['incident_number'].astype('string')
    merged_df['offense_classification'] = merged_df['offense_classification'].astype('category')
    merged_df['was_offense_completed'] = merged_df['was_offense_completed'].astype('category')
    merged_df['location_category'] = merged_df['location_category'].astype('category')
    merged_df['week_day_reported'] = merged_df['week_day_reported'].astype('category')
    merged_df['week_day_occurred'] = merged_df['week_day_occurred'].astype('category')
    merged_df['value_range'] = merged_df['value_range'].astype('category')
    return merged_df

def save_cleaned_data(merged_df):

    merged_df.to_csv('./data/combined_crime_data.csv', index=False)
    print(merged_df.dtypes)
