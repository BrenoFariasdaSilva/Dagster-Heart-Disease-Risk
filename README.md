# Heart Disease Risk
## Useful documentation:
* [Dagster](https://docs.dagster.io/tutorial)
* [Integrate Python Jupyter Notebook with Dagster](https://docs.dagster.io/integrations/dagstermill/using-notebooks-with-dagster)

# Clone the project:
```bash
git clone https://github.com/BrenoFariasdaSilva/Heart-Disease-Risk.git
cd Heart-Disease-Risk
```
# Installation:
```bash
pip install dagster dagit
```
# How the project was created:
```bash
dagster project scaffold --name heart_disease_risk
cd heart_disease_risk
```
# Execute:
```bash
make locally
```
# Open:
Open the following link in your browser in order to see the dagit UI:
```bash
http://127.0.0.1:3000
```
# File Hierarchy:
### * **Assets Files/Directory** ->  Assets are data artifacts that are produced and consumed by pipelines. They can be anything from raw data files (such as CSV or JSON) to processed data sets or model outputs. An asset definition typically includes the asset's name, the type of the asset (e.g. a file, a database table), and any associated metadata or configuration options. Assets can also specify dependencies on other assets, so that a pipeline will only run when all of its dependencies are available.
### * **Jobs** -> Jobs are used to define the scheduling and execution of pipelines. They are defined using a Python script with the .py extension, and are typically stored in the jobs/ directory of a Dagster project. A job definition typically includes the name of the job, the schedule on which the job should be run (e.g. daily, weekly), and the pipeline(s) that should be executed by the job. Jobs can also specify environment variables and other configuration options that are passed to the pipeline(s) when they are executed.
### * **workspace.yaml** -> This is a configuration file that defines the Dagster instance used in the tutorial notebooks. It specifies the location of the Dagster instance, which is important for connecting to the Dagster API.
### * **setup.py** -> This is a Python script that contains the configuration information for building and distributing a Python package. It typically includes information such as the package name, version, author, and dependencies. It can also specify scripts to be installed with the package, and other package-specific options.
### * **setup.cfg** -> This is a configuration file that is used to specify additional options for setuptools, the package that is commonly used to build and distribute Python packages. It can include options such as the package's entry points, the location of the package's data files, and various build and distribution options.
### * **pyproject.toml** -> This is a configuration file that is used by modern Python build tools such as poetry and flit. It specifies the project's dependencies, build tool configuration, and metadata. It can also include options for building and packaging the project.

# Important Notes:
### Each file has (or should have) comments explaining what it does, the same should be applied to functions. So, if you have any doubts, please, read the comments or contact me.