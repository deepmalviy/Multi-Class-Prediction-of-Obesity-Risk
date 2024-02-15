from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requiements = []
    with open(file_path) as file_obj:
        requiements = file_obj.readlines()
        requiements = [req.replace('\n','') for req in requiements]
        
        if HYPEN_E_DOT in requiements:
            requiements.remove(HYPEN_E_DOT)

setup(
    name = 'Multi-Class Prediction of Obesity Risk',
    version = '0.0.1',
    author = 'deepmalviy',
    author_email = 'deep.malviya94@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)