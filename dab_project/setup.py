from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.1",
    description="This contains code in src directory",
    author="Torrance",
    packages=find_packages(where="./src"),
    package_dir={"":"./src"},
    install_requires=["setuptools"]
)