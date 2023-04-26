from setuptools import find_packages, setup

setup(
    name="heart_disease_risk",
    packages=find_packages(exclude=["heart_disease_risk_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
