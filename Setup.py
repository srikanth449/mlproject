from setuptools import find_packages,setup
from typing import List

Hypen_E_Dot='-e .'
def get_requirements(file_path:str) -> List[str]:
    
    '''
    this function will retunr the list of requirements
    '''

    requiremnets =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
setup(
name='mlproject',
version='0.0.1',
author='Sri',
author_email='sriaknth.449@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')

)