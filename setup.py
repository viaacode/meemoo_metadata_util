from setuptools import setup, find_packages

setup(name='meemoo_metadata_util',
      version='0.1',
      description='Utility functions for meemoo metadata',
      long_description=open('README.md').read(),
      url='https://github.com/viaacode/meemoo_metadata_util',
      author='Miel Vander Sande',
      author_email='miel.vandersande@meemoo.be',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      zip_safe=False)