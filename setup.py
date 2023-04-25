from setuptools import find_packages, setup

setup(
    name="heart_disease_risk_assets",
    packages=find_packages(exclude=["heart_disease_risk_assets"]),
    install_requires=[
        "dagster",
        "dagstermill",
        "papermill-origami>=0.0.8",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
