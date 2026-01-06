# GeorgeMao Utils Library

A common utility library for development teams, containing frequently used methods for strings, dates, and collections.

## Features

- **String Utilities**: Slugification and smart truncation.
- **Date Utilities**: ISO formatters and business day calculations.
- **Collection Utilities**: List chunking and flattening.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from utils.string_utils import slugify
from utils.date_utils import add_business_days
from datetime import datetime

# Slugify a string
print(slugify("Hello World!"))  # hello-world

# Add business days
next_business_day = add_business_days(datetime.now(), 1)
print(next_business_day)
```

## Running Tests

```bash
export PYTHONPATH=$PYTHONPATH:.
python3 tests/test_utils.py
```
