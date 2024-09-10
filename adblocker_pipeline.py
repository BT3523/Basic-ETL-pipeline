import requests
import pandas as pd

def extract_data():
    # URL for the FilterLists API
    url = 'http://filterlists.com/api/directory/lists'

    # Send GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
def transform_data(data):
    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)

    # Select relevant columns for analysis (e.g., id, name, description, syntax, viewUrl)
    df = df[['id', 'name', 'description', 'syntax', 'viewUrl']]

    # Clean missing values
    df.fillna({'description': 'No description', 'syntax': 'Unknown'}, inplace=True)

    # Optionally, remove rows with missing 'name' or 'id'
    df.dropna(subset=['name', 'id'], inplace=True)
    
    return df
from sqlalchemy import create_engine

def load_data(df):
    # Create an SQLite engine
    engine = create_engine('sqlite:///filterlists.db')
    
    # Load data into the 'filter_lists' table in SQLite
    df.to_sql('filter_lists', con=engine, if_exists='replace', index=False)
    
    print("Data loaded successfully into the database!")
def run_etl_pipeline():
    # Step 1: Extract data from the API
    data = extract_data()
    
    # Step 2: If extraction was successful, transform the data
    if data:
        transformed_data = transform_data(data)
        
        # Step 3: Load the transformed data into the SQLite database
        load_data(transformed_data)
    else:
        print("No data to process.")

# Run the ETL pipeline
if __name__ == "__main__":
    run_etl_pipeline()
