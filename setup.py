from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Package for using custom functions'
LONG_DESCRIPTION = 'Package for using custom functions'

# Setting up
setup(
        name="data_gadgets", 
        version=VERSION,
        author="Hamza Farrukh",
        author_email="<hamzafarrukh73@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy', 'pandas', 'matplotlib', 'seaborn'],         
        keywords=['python', 'data', 'visualization', 'analysis', 'cleaning'],
)