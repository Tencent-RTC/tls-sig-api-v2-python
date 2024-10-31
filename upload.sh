#! /bin/sh

rm -rf dist

python setup.py sdist

# You need to make sure twine is installed. If not, the installation command is as follows
# pip install twine

# Create .pypirc in the ~/ directory with the following content:
# [distutils]
# index-servers = pypi
# 
# [pypi]
# username:Your PyPi username
# password:Your PyPi password

twine upload dist/*.tar.gz

