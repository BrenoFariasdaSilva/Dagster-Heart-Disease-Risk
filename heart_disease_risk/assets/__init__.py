# Assets are used to create data pipelines
# Data pipelines are used to read data, process it and return it in a format that can be used by the model
# Note: Create an assets does not mean that the data is read, processed and returned (materialized) which will be stored on databases or cloud storage.
# Think of the materialization as a instance of the asset which would create a snapshot of the data at that point in time
# Assets can be manually materialized (GUI) or automatically materialized (https://docs.dagster.io/_apidocs/ops#dagster.AssetMaterialization)

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
	# print(dataframe.head())
	# save the dataframe.head as a csv file inside the cd../data folder
	dataframe.head().to_csv('heart_disease_risk/processed_data/dataframeHead.csv')
	
	## Descrevendo as features numéricas
	dataframe.describe().T.style.set_properties(**{'background-color': 'grey','color': 'white','border-color': 'white'})
	# save the dataframe.info as a csv file
	# dataframe.info().to_csv('heart_disease_risk/processed_data/dataframeInfo.csv')
	
	## Verificando valores únicos. Alguns atributos tem mais de dois valores únicos. Vamos usar OneHotEncoder para processar os dados e normalizá-los
	dataframe.nunique()
	dataframe =  dataframe[dataframe.columns].replace({'Yes':1, 'No':0, 'Male':1,'Female':0,'No, borderline diabetes':'0','Yes (during pregnancy)':'1' })
	dataframe['Diabetic'] = dataframe['Diabetic'].astype(int)
	# Save the previous dataframe as a csv file
	# dataframe.to_csv('heart_disease_risk/processed_data/output.csv', index=False)

	## Análise gráfica; distribuição de casos por sexo; 1 para homens, 0 para mulheres
	fig, ax = plt.subplots(figsize = (13,6))
	# generate output file that project the fig, ax

	ax.hist(dataframe[dataframe["HeartDisease"]==1]["Sex"], bins=15, alpha=0.5, color="red", label="HeartDisease")
	ax.hist(dataframe[dataframe["HeartDisease"]==0]["Sex"], bins=15, alpha=0.5, color="#fccc79", label="Normal")

	ax.set_xlabel("Genero")
	ax.set_ylabel("Frequencia")

	fig.suptitle("Distribuição dos casos com SIM/NAO (Yes/no) problemas cardíacos de acordo com o Genero")

	ax.legend();

# Function that call csv_head() function and execute it in a process
@job
def print_csv_data_job():
	csv_head()

# The execute_in_process() function executes the job in a separate process
result = print_csv_data_job.execute_in_process()