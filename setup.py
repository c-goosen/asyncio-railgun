# -*- coding: utf-8 -*-
import os
import subprocess
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command
import codecs

__version__ = '0.0.3'

curr_dir = os.path.abspath(os.path.dirname(__file__))

long_description = ""
with codecs.open(os.path.join(curr_dir, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

tests_require = ["pytest", "pytest-cov", "codecov", "flake8", "black", "bandit"]


class BaseCommand(Command):
    """Base Command"""

    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def _run(self, s, command):
        try:
            self.status(s + "\n" + " ".join(command))
            subprocess.check_call(command)
        except subprocess.CalledProcessError as error:
            sys.exit(error.returncode)


class ValidateCommand(BaseCommand):
    """Support setup.py validate."""

    description = "Run Python static code analyzer (flake8), formatter (black) and unit tests (pytest)."

    def run(self):
        self._run(
            "Installing test dependencies…",
            [sys.executable, "-m", "pip", "install"] + tests_require,
        )
        self._run("Running black…", [sys.executable, "-m", "black", "railgun/"])
        self._run("Running flake8…", [sys.executable, "-m", "flake8", "railgun/"])
        self._run("Running bandit…", [sys.executable, "-m", "bandit", "-r", "railgun/"])
        self._run(
            "Running pytest…",
            [
                sys.executable,
                "-m",
                "pytest",
                "--cov-report=xml",
                "tests/",
            ],
        )


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
    # install_requires=["aiohttp>3.5.2"],
    # extras_require={"optional": ["aiodns>1.0"]},
    setup_requires=["pytest-runner"],
    test_suite="tests",
    tests_require=tests_require,
    cmdclass={"validate": ValidateCommand},
)
