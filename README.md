# smartutils

## PROJECT TITLE : 

# SMART UTILS

## DESCRIPTION : 

SmartUtils is a Python utility package that provides reusable helper classes and functions. It allows developers to perform common tasks without rewriting the same code in every project.

## FEATURES : 

- Check whether a number is even or odd
- Check whether a number is positive, negative, or zero
- Determine whether a year is a leap year
- More utilities will be added in future releases

## Installation : 

JUST USE THIS 

```bash
pip install smartutils
```

## USAGE 

```python
from smartutils import NumberUtility

num = NumberUtility(10)

print(num.is_even())
print(num.check_sign())
```

## FOLDER STRUCTURE : 

```text
smartutils_project/
│
├── smartutils/
│   ├── __init__.py
│   ├── numbers.py
│
├── tests/
├── README.md
├── LICENSE
├── pyproject.toml
├── .gitignore
└── CHANGELOG.md
```

## Roadmap

- [x] Number utilities
- [ ] Finance utilities
- [ ] Date utilities
- [ ] Health utilities
- [ ] String utilities
- [ ] Unit converters

## License

This project is licensed under the MIT License.

