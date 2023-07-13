# Assets are used to create data pipelines
# Data pipelines are used to read data, process it and return it in a format that can be used by the model
# Note: Create an assets does not mean that the data is read, processed and returned (materialized) which will be stored on databases or cloud storage.
# Think of the materialization as a instance of the asset which would create a snapshot of the data at that point in time
# Assets can be manually materialized (GUI) or automatically materialized (https://docs.dagster.io/_apidocs/ops#dagster.AssetMaterialization)

import base64
from io import BytesIO
from dagster import asset, job, op # Import the asset, job and op decorators from the dagster library
import pandas as pd # Import the pandas library
import numpy as np # Import the numpy library

# %matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree

from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler 
from sklearn import metrics

# Function that reads the data from the csv file and stores it in a pandas dataframe
## Panda dataframe is a 2-dimensional labeled data structure with columns of potentially different types, similar to an Excel spreadsheet or SQL table
@asset # Decorator that marks the function as an asset (SDA - Software Defined Asset)
def read_csv_data(): 
	# csv is stores in the data folder that is in the same directory as the assets.py file
	csv_file_path = "heart_disease_risk/data/risco_cardiaco.csv"
	csv_file = pd.read_csv(csv_file_path) # Read the csv file and store it in a pandas dataframe

	dataframe = pd.DataFrame(csv_file) # Create a pandas dataframe from the csv file
	return dataframe # Return the pandas dataframe

# Function that call read_csv_data() function and print dataframe.head() 
@op # Decorator that marks the function as a op
def csv_head():
	## Lendo os datasets
	dataframe = read_csv_data() # Call the read_csv_data() function and store the dataframe in a variable

	#Selecionando atributos
	X = dataframe.drop(columns =['HeartDisease'], axis = 1)

	#Selecionando variável alvo (teve ou não doença cardíaca)
	y = dataframe['HeartDisease']

	# Separando treinamento e teste
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = True, test_size = 0.2, random_state = 44)

	# print('Shape of training feature:', X_train.shape)
	# print('Shape of testing feature:', X_test.shape)
	# print('Shape of training label:', y_train.shape)
	# print('Shape of training label:', y_test.shape)

	#Aplicando OneHotEncoding para normalizar as variáveis categóricas
	transformer = make_column_transformer(
		(OneHotEncoder(sparse=False), ['AgeCategory', 'Race', 'GenHealth']),
		remainder='passthrough')
	
	#Aplicando OneHotEncoding para normalizar as variáveis numéricas
	transformer = make_column_transformer()

	# Encode training data 
	transformed_train = transformer.fit_transform(X_train)
	transformed_train_data = pd.DataFrame(transformed_train, columns=transformer.get_feature_names_out())

	# Concat the two tables
	transformed_train_data.reset_index(drop=True, inplace=True)
	X_train.reset_index(drop=True, inplace=True)
	X_train = pd.concat([transformed_train_data, X_train], axis=1)

	# Remove old columns
	X_train.drop(['AgeCategory', 'Race', 'GenHealth'], axis = 1, inplace = True)

	# Encode test data 
	transformed_test = transformer.fit_transform(X_test)
	transformed_test_data = pd.DataFrame(transformed_test, columns=transformer.get_feature_names_out())

	# Concat the two tables
	transformed_test_data.reset_index(drop=True, inplace=True)
	X_test.reset_index(drop=True, inplace=True)
	X_test = pd.concat([transformed_test_data, X_test], axis=1)

	# Remove old columns
	X_test.drop(['AgeCategory', 'Race', 'GenHealth'], axis = 1, inplace = True)

	print(f"len(X_test.columns): {len(X_test.columns)}")

	#Fazendo normalização dos dados numéricos com scaler (valores entre 0 e 1)
	scaler = StandardScaler()

	# print(f"Type of X_train: {type(X_train)}\nType of X_test: {type(X_test)}\n")
	# # print the type of X_train[0]
	# print(f"Type of X_train[0]: {type(X_train.iloc[0])}\n")
	# print(f"X_test.head(1): {X_test.head(1)}")

	# # Scale training data
	X_train = scaler.fit_transform(X_train)

	# # Scale test data
	# X_test = scaler.fit_transform(X_test)

# Function that call csv_head() function and execute it in a process
@job
def print_csv_data_job():
	csv_head()

# The execute_in_process() function executes the job in a separate process
result = print_csv_data_job.execute_in_process()