## This is used to convert your application or machine learning models into a package.

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    try:
        with open(file_path) as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line or cleaned_line.startswith('#'):
                    continue
                if cleaned_line.startswith('-'):
                    continue
                requirements.append(cleaned_line)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    return requirements

setup(
    name="mlProject",
    version="1.0.0",
    author="Shivam Agarwal",
    author_email="shivam.agarwal@hotmail.com",
    description="End to End Machine Learning Project with AWS, Azure Deployment",
    packages=find_packages(),  
    install_requires=get_requirements('requirements.txt')
)