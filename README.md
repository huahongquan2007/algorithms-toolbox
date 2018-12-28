[![PyPI version](https://badge.fury.io/py/algorithms-toolbox.svg)](https://badge.fury.io/py/algorithms-toolbox)
[![Build Status](https://travis-ci.org/quanhua92/algorithms-toolbox.svg?branch=master)](https://travis-ci.org/quanhua92/algorithms-toolbox)
[![Coverage Status](https://coveralls.io/repos/github/quanhua92/algorithms-toolbox/badge.svg?branch=master)](https://coveralls.io/github/quanhua92/algorithms-toolbox?branch=master)

# algorithms_toolbox

A small collection of algorithms in Python

## Tests

```
py.test
```

## Installation

```
pip install algorithms-toolbox
```

## Usage

```
from atb.search import binary_search

res = binary_search(4, [1, 2, 3, 4, 5])
print(res)
```

## List of algorithms

- [search](atb/search)
    - [binary-search](atb/search/binary_search.py)
