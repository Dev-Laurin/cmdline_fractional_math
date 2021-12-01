# cmdline_fractional_math
A command line program that takes a string of fractions and operators and returns the mathematical result.

# Instructions
Write a command line program in the language of your choice that will take operations on fractions as an input and produce a fractional result.

* Legal operators shall be *, /, +, - (multiply, divide, add, subtract)

* Operands and operators shall be separated by one or more spaces

* Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"

* Improper fractions and whole numbers are also allowed as operands

Example run:

? 1/2 * 3_3/4

= 1_7/8

? 2_3/8 + 9/8

= 3_1/2

# Run Tests 
* Clone repo
* Run setup.py from Python 3+
```python
python3 setup.py
```
* Install package via symlink for dev code
```
pip install -e .
```
* Run pytest
```
pytest
```
