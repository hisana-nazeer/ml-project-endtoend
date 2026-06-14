from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list:
    """Read requirements from a requirements.txt and return as a list of strings."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj if req.strip() and not req.strip().startswith('#')]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name='ml project-endtoend',
    version='0.1.0',
    author='Hisana',
    author_email='nhisana022@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
