#!/usr/bin/env python
import codecs
from setuptools import setup, find_packages


def read_files(*filenames):
    """
    Output the contents of one or more files to a single concatenated string.
    """
    output = []
    for filename in filenames:
        f = codecs.open(filename, encoding='utf-8')
        try:
            output.append(f.read())
        finally:
            f.close()
    return '\n\n'.join(output)


setup(
    name='pynexpose',
    version='0.1',
    description='Github forq of pynexpose with a build',
    long_description=read_files('README.md',),
    author='The Forqlift',
    author_email='forq@lift.this',
    url='https://github.com/forqlift/pynexpose/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
