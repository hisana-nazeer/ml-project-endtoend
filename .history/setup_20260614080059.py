from setuptools import find_packages, setup

setup(
    name='ml project-endtoend',
    version='0.1.0',
    author='Hisana',
    author_email='nhisana022@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)
    
def get
