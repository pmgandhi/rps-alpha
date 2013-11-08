#!/usr/bin/env python
import os

from pip.req import parse_requirements
from setuptools import setup, find_packages

setup(
    author="INSS",
    author_email="cpaterso@thoughtworks.com",
    name="redundancy_payments_service",
    packages=find_packages(),
    scripts=["redundancy_payments_service"],
    version=os.environ.get("BUILD_NUMBER", "dev"),
    install_requires=[str(req.req) for req in
                      parse_requirements("requirements.dev.txt")],
    include_package_data=True,
    )
