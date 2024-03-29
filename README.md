# Python asyncio railgun
A python3.4+ asyncio library wrapper for utilzing asyncio tasks and gather(*) functionality. Library is meant to make concurrent tasks easier and safer through the use of semaphores.


[![pypi package][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]
[![Python Version][python-version]][pypi-url]
[![codecov][codecov-image]][codecov-url]


## Table of contents


### Requirements
---
This library requires Python 3.6 and above. 

> **Note:** You may need to use `python3` before your commands to ensure you use the correct Python path. e.g. `python3 --version`


```bash
python --version

-- or --

python3 --version
```

### Installation

We recommend using [PyPI][pypi] to install the Slack Developer Kit for Python.


```bash
pip3 install asyncio-railgun==0.0.1
```

### Basic Usage examples
---


#### Run
```python
from asyncio import get_event_loop
from railgun.railgun import Railgun
from http import client

def example_call_api(host='www.google.com', url='/'):
    conn = client.HTTPSConnection(host, port=443, timeout=5)
    conn.request(method='GET', url=url)
    response = conn.getresponse()
    return response.status

rail_gun = Railgun(semaphores_count=10)
results = rail_gun.run([example_call_api(), example_call_api()])
print(results)
```

#### Run async
TBD
#### Repeat
TBD
### Support
---
TBD

Contact me on christogoosen@gmail.com

Otherwise see the examples and log an issue.

<!-- Markdown links -->
[pypi-image]: https://badge.fury.io/py/asyncio-railgun.svg
[pypi-url]: https://pypi.python.org/pypi/asyncio-railgun
[travis-image]: https://api.travis-ci.org/c-goosen/asyncio-railgun.svg?branch=master
[travis-url]: https://travis-ci.org/c-goosen/asyncio-railgun
[codecov-image]: https://codecov.io/gh/c-goosen/asyncio-railgun/branch/master/graph/badge.svg
[codecov-url]: https://codecov.io/gh/c-goosen/asyncio-railgun
[pypi]: https://pypi.python.org/pypi
[pipenv]: https://pypi.org/project/pipenv/
[gh-issues]: https://github.com/c-goosen/asyncio-railgun/issues
[aiohttp]: https://aiohttp.readthedocs.io/
[python-version]: https://img.shields.io/pypi/pyversions/asyncio-railgun.svg