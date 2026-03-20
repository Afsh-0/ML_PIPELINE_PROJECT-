from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = "-e ."

"""we have difined a function which will pass through filepath we could be any folder or file and 
it will be string (str) (be default value was none that's why we have written here str)"""
def get_requirements(filepath: str) -> List[str]: 
    requirements = [] #created an empty list 

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n", "") for i in requirements]


        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    
    return requirements
    



"""to make setup.py file as a package we need to install it first and for that we will add -e . in 
requirenments.txt"""

from setuptools import setup

setup(
    name='ML_PIPLINE_PROJECT', #ADD ANY NAME BUT BEST PRACTISE IS TO ADD PROJECT NAME 
    version='0.0.1', #initial version 
    description='A sample ML_PIPLINE_PROJECT bsic',
    author='Afsha',
    author_email='248272946+Afsh-0@users.noreply.github.com',
    #url="github url"
    packages=find_packages(), #it will automatically search a packages from requirements.txt
    #we need to install all packages and library from requirements.txt in one single shot
    install_requires=get_requirements("requirements.txt"),
)

"""package setup up has been done but when we will rum requirements.txt, we don't want to make it a 
package now, so we will remove -e . for now and for that we will write codes in line 4 (defined it) 
and lines 16 and 17"""