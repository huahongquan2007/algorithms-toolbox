[![PyPI version](https://badge.fury.io/py/algorithms-toolbox.svg)](https://badge.fury.io/py/algorithms-toolbox)

# algorithms_toolbox

A small collection of algorithms in Python 3

## Tests

```
py.test --doctest-modules --cov --cov-report term-missing
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
