#!/usr/bin/env python
import os

from pip.req import parse_requirements
from setuptools import setup, find_packages

setup(
    author="INSS",
    author_email="cpaterso@thoughtworks.com",
    name="birmingham_cabinet",
    packages=find_packages(),
    scripts=["run_birmingham_cabinet"],
    version=os.environ.get("BUILD_NUMBER", "dev"),
    install_requires=[str(req.req) for req in
                      parse_requirements("requirements.dev.txt")],
    include_package_data=True,
    zip_safe=False
    )