# Password Generator

This project provides a set of classes for generating different types of passwords, including numeric PIN codes, random alphanumeric passwords, and memorable passwords composed of words. It also includes functionality to calculate the entropy of generated passwords, which can be useful for assessing their strength.


This repository also contains unit tests for various password generation classes implemented in the `src.main_oop` module. The tests are designed to validate the functionality of different password generators, including PIN codes, random passwords, and memorable passwords. The tests also include checks for password entropy calculations.

## Table of Contents

- [Password Generator](#password-generator)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Unit test](#unit-test)
    - [Testing](#testing)
    - [Test Cases](#test-cases)

## Requirements

- Python 3.x
- nltk library (Natural Language Toolkit)

## Installation

1. Install the required libraries:
    ``` bash
    pip install nltk
    ```

2. Download the NLTK words corpus:
    ```python
    import nltk
    nltk.download('words')
    ```

## Usage

To use the password generators, you can create instances of the desired generator class and call the generate_password method. Below is an example of how to use each generator:
```python
if __name__ == '__main__':
    # Generate a 6-digit PIN code
    pin_code_generator = PinCodeGenerator(6)
    pin_code_generator.generate_password()
    pin_code_generator.calculate_entropy()

    # Generate a random alphanumeric password of length 12
    random_password_generator = RandomPasswordGenerator(12, include_numbers=True, include_symbols=True)
    random_password_generator.generate_password()
    random_password_generator.calculate_entropy()

    # Generate a memorable password with 3 words
    memorable_password_generator = MemorablePasswordGenerator(3)
    memorable_password_generator.generate_password()
    memorable_password_generator.calculate_entropy()
```
## Unit test
The unit tests are implemented using the unittest framework. The following classes are tested:

- `PinCodeGenerator`
- `RandomPasswordGenerator`
- `MemorablePasswordGenerator`

### Testing

To run the tests, execute the following command in your terminal:

```bash
python -m unittest src/test_main_oop.py
```

### Test Cases

The following test cases are included:

1. **Test PIN Code Generator**
   - Checks if the generated PIN code has the correct length.
   - Verifies that the PIN code consists only of digits.

2. **Test Random Password Generator**
   - Checks if the generated random password has the correct length.
   - Ensures that the password contains only allowed characters (letters, digits, punctuation).

3. **Test Memorable Password Generator**
   - Mocks the random sampling to generate a predictable output.
   - Validates that the generated memorable password matches the expected format.

4. **Test Entropy Calculation**
   - Validates the entropy calculation for a generated PIN code against the expected value.