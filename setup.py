# helpful article: https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

import setuptools

with open("README.md", "r") as fh:
    long_description = open('README.md').read()

setuptools.setup(
    name='pytodo_package',  
    version='0.1.1',
    scripts=[] , # to add pytodo/bin/__init__.py ( please add the path only when the file would be completely written )
    author="Parth Paradkar",
    author_email="parthparadkar3@gmail.com",
    maintainer = "Shubhashish Dixit",
    maintainer_email="thisisshub@gmail.com",
    description="A minimal command line todo list built with Python and MongoDB",
    long_description=long_description,
    long_description_content_type="markdown",
    install_requires=[
        'pymongo==3.8.0',
        'astroid==1.6.6',
        'autopep8==1.4.4',
        'backports.functools-lru-cache==1.6.1',
        'configparser==4.0.2',
        'enum34==1.1.6',
        'futures==3.3.0',
        'isort==4.3.21',
        'lazy-object-proxy==1.4.3',
        'mccabe==0.6.1',
        'pycodestyle==2.5.0',
        'pylint==1.9.5',
        'singledispatch==3.4.0.3',
        'six==1.13.0',
        'wrapt==1.11.2'
],
    url="https://github.com/thescriptninja/pytodo",
    packages=setuptools.find_packages(),
    classifiers=[],
)
