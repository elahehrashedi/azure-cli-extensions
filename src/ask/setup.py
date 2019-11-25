# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

VERSION = "0.3.0"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    'colorama~=0.3.7'
]

setup(
    name='ask',
    version=VERSION,
    description='Recommending alternative CLI commands',
    long_description='recom recommends CLI commands that might help you recover from the failed command"
    license='MIT',
    author='Elaheh Rashedi',
    author_email='elrashed@microsoft.com',
    url='https://github.com/Azure/azure-cli-extensions/tree/master/src/recom',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={'azext_ask': ['azext_metadata.json']}