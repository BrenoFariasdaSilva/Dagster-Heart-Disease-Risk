from dagster import Definitions, load_assets_from_modules

# If you move the assets.py file to a different directory than the project root, you will need to update the import statement below.
# I moved the assets.py file from the heart_disease_risk/ to the heart_disease_risk/assets directory
# With that in mind, i renamed the assets.py file to __init__.py
# It allows me to import the assets from the assets directory without having to specify the file name 
# So the import went from "from assets.assets import assets" to "from assets import assets"
# It makes the code more readable and easier to maintain

from assets import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)
