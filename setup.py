from typing import List
from setuptools import find_packages,setup

def get_requirement()->List[str]:
    '''
    This function will return the list of requirements
    '''

    requirement_list:List[str] = []
    return requirement_list

setup(
    name="sensor",
    version='0.0.1',
    author="Rahul Pandey",
    author_email="rahulpandey4950@gmail.com",
    packages= find_packages(),
    install_requires= get_requirement(),
)