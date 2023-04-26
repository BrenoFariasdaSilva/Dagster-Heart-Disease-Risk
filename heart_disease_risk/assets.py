# Assets are used to create data pipelines
# Data pipelines are used to read data, process it and return it in a format that can be used by the model
# Note: Create an assets does not mean that the data is read, processed and returned (materialized) which will be stored on databases or cloud storage.
# Think of the materialization as a instance of the asset which would create a snapshot of the data at that point in time
# Assets can be manually materialized (GUI) or automatically materialized (https://docs.dagster.io/_apidocs/ops#dagster.AssetMaterialization)

from dagster import asset # Import the asset decorator
import pandas as pd # Import the pandas library

# Function that reads the data from the csv file and stores it in a pandas dataframe
## Panda dataframe is a 2-dimensional labeled data structure with columns of potentially different types, similar to an Excel spreadsheet or SQL table
@asset # Decorator that marks the function as an asset (SDA - Software Defined Asset)
def read_csv_data(): 
	# csv is stores in the data folder that is in the same directory as the assets.py file
	csv_file = "heart_disease_risk/data/risco_cardiaco.csv"
	dataframe = pd.read_csv(csv_file) # Read the csv file and store it in a pandas dataframe
	return dataframe