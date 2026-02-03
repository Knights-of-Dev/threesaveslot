from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='threesaveslot',
    version='1.0.0',    
    description='description here. each time you want to update your module, make sure the version above doesnt already exist!',
    url='https://github.com/Knights-of-Dev/threesaveslot',
    author='Pitchfork',
    author_email='example@example.com',    
    license='MIT',
    packages=['threesaveslot'],
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Freeware',  
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15'
    ],
)    
