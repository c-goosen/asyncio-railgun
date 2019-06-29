# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
import codecs

__version__ = '0.0.3'

curr_dir = os.path.abspath(os.path.dirname(__file__))

long_description = ""
with codecs.open(os.path.join(curr_dir, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

tests_require = ["pytest", "pytest-cov", "codecov", "flake8", "black", "bandit"]

setup(
    name="asyncio-railgun",
    version=__version__,
    description="Library for easier asyncio concurrent tasks.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/c-goosen/asyncio-railgun",
    author="Christo Goosen",
    author_email="christogoosen@gmail.com",
    python_requires=">=3.6.0",
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Framework :: AsyncIO",
        "Topic :: System :: Networking",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Typing :: Typed",
    ],
    keywords="asyncio concurrent gather tasks",
    packages=find_packages(
        exclude=["docs", "docs-src", "tests", "tests.*", "tutorial"]
    ),
    setup_requires=["pytest-runner"],
    test_suite="tests",
    tests_require=tests_require,
    # cmdclass={"validate": ValidateCommand},
)
