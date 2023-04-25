import pandas as pd
from dagstermill import define_dagstermill_asset
from papermill_origami.noteable_dagstermill import define_noteable_dagster_asset

from dagster import AssetIn, Field, Int, asset, file_relative_path

# The code below create a Dagster asset of the heart disease risk dataset
# relevant documentation - https://docs.dagster.io/concepts/assets/software-defined-assets#a-basic-software-defined-asset

@asset(group_name="heart_disease_risk")
def heart_disease_dataset():
    return pd.read_csv(
        "../data/risco_cardiaco.csv",
    )

# The code below create a Dagster asset backed by a Jupyter notebook
# relevant documentation - https://docs.dagster.io/_apidocs/libraries/dagstermill#dagstermill.define_dagstermill_asset

heart_disease_jupyter_notebook = define_dagstermill_asset(
	name="heart_disease_jupyter",
	notebook_path=file_relative_path(__file__, "../notebooks/risco-doenca-cardiaca.ipynb"),
	group_name="heart_disease_risk",
	ins={"heart_disease": AssetIn("heart_disease_dataset")},  
)

# Uncomment the code below to create a Dagster asset backed by a Noteable notebook
# relevant documentation - https://papermill-origami.readthedocs.io/en/latest/reference/noteable_dagstermill/assets/

# notebook_id = "<your-noteable-notebook-id>"
# heart_disease_noteable_notebook = define_noteable_dagster_asset(
#     name="heart_disease_noteable",
#     notebook_id=notebook_id,
#     ins={"heart_disease": AssetIn("heart_disease_dataset")},
#     group_name="heart_disease_risk"
# )
