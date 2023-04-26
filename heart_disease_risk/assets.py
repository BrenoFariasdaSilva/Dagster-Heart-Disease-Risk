# Assets are used to create data pipelines
# Data pipelines are used to read data, process it and return it in a format that can be used by the model

from dagster import asset # Import the asset decorator
import pandas as pd # Import the pandas library

# Function that reads the data from the csv file and stores it in a pandas dataframe
## Panda dataframe is a 2-dimensional labeled data structure with columns of potentially different types, similar to an Excel spreadsheet or SQL table
@asset # Decorator that marks the function as an asset
def read_csv_data(): 
	dataframe = pd.read_csv('../data/risco_cardiaco.csv')
	return dataframe