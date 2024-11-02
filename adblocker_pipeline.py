import requests
import pandas as pd
from sqlalchemy import create_engine
import schedule
import time

def extract_data():
    url = 'http://filterlists.com/api/directory/lists'

    # Send GET
    response = requests.get(url)

    # Error Handling
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def transform_data(data):
    df = pd.DataFrame(data)
    df = df[['id', 'name', 'description', 'syntax', 'viewUrl']]
    df.fillna({'description': 'No description', 'syntax': 'Unknown'}, inplace=True)
    df.dropna(subset=['name', 'id'], inplace=True)
    
    return df

def load_data(df):
    engine = create_engine('sqlite:///filterlists.db')
        df.to_sql('filter_lists', con=engine, if_exists='replace', index=False)
    
    print("Data loaded successfully into the database!")

def run_etl_pipeline():
    print("Starting ETL pipeline...")
    data = extract_data()
        if data:
        transformed_data = transform_data(data)
                load_data(transformed_data)
    else:
        print("No data to process.")
    print("ETL pipeline completed.")

def run_etl():
    # Schedule
    run_etl_pipeline()
schedule.every().week.at("02:00").do(run_etl)

if __name__ == "__main__":
    print("Scheduler started. Waiting for scheduled tasks...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait one minute
