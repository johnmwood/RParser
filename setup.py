from setuptools import setup 
from rparser.parser import run_parser


setup( 
    # Needed to silence warnings (and to be a worthwhile package)
    name='RParser',
    url='https://github.com/HSPS-DataScience/RParser',
    author='John Wood',
    author_email='jmw.home@gmail.com',
    # Needed to actually package something
    packages=['rparser'],
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1.1',
    # The license can be anything you like
    license='',
    description='Parse an R script into Rmd using Python',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
    include_package_data=True, 
)
