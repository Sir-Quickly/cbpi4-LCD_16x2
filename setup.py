from setuptools import setup, find_packages
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-LCD_16x2',
      version='0.0.2',
      description='CraftBeerPi4 LCD Plugin for 16x2 Display',
      author='Roland Brand',
      author_email='sir.quickly0@googlemail.com',
      url='https://github.com/Sir-Quickly/cbpi4-LCD_16x2',
      license='GPLv3',
      include_package_data=True,
      package_data={
          # If any package contains *.txt or *.rst files, include them:
          '': ['*.txt', '*.rst', '*.yaml'],
          'cbpi4-LCD_16x2': ['*', '*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-LCD_16x2'],
      #packages=find_packages(),
      install_requires=[
            'smbus2',
            'RPLCD',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
