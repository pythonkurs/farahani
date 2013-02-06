from setuptools import setup, find_packages
import sys, os

version = '0.1dev'

setup(name='farahani',
      version=version,
      description="SciLifeLab python course 2013",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='scilifelab bioinformatics',
      author='Hossein Farahani',
      author_email='farahani@scilifelab.se',
      url='http://github.com/pythonkurs/farahani',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=["scripts/getting_data.py", "scripts/check_repo.py"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
