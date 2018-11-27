"""The setup script."""
import os
import json
from setuptools import setup, find_packages, Command

NAME = "khumeia"
VERSION = "1.0.dev0"

if os.path.exists(".branch.version"):
    with open(".branch.version", "r") as f:
        VERSION = (VERSION + f.read()).replace('\n', '')
elif os.path.exists(".tag.version"):
    with open(".tag.version", "r") as f:
        VERSION = (f.read()).replace('\n', '')

with open('README.md', "r") as f:
    readme = str(f.read())

with open('requirements.txt', 'r') as f:
    requirements = [line for line in f.readlines()]

with open('requirements.test.txt', 'r') as f:
    test_requirements = [line for line in f.readlines()]

with open('requirements.extras.json', 'r') as f:
    extras_requirements = json.load(f)
    extras_requirements['test'] = test_requirements


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


setup(
    name=NAME,
    version=VERSION,
    description="Framework for a hands on with Deep Learning & aircrafts detection at ISAE-SUPAERO",
    long_description=readme + '\n\n',
    author="Florient CHOUTEAU & Matthieu LE GOFF",
    author_email='florient.chouteau@gmail.com',
    url='',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"], ),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='',
    tests_require=test_requirements,
    extras_require=extras_requirements,
    cmdclass={
        'clean': CleanCommand,
    })
