# Unit Test Generator

Generating unit test by sequence-to-sequence model.

### Demo

```text
[Evaluation] Loss: 0.187 | Accuracy: %92.86
--------------------------------------------------------------------------------
[Input ] def subtract_numbers(number_a, number_b): return number_a - number_b
[Output] def test_subtraction(): assert subtract_numbers(64, 50) == 12
--------------------------------------------------------------------------------
[Input ] def calculate_sum(a, b): return a + b
[Output] def test_addition(): assert accumulate(82, 64) == 140
--------------------------------------------------------------------------------
[Input ] def plus(num1, num2): return num1 + num2
[Output] def test_addition(): assert plus(21, 100) == 119
--------------------------------------------------------------------------------
[Input ] def append(first, second): return first + second
[Output] def test_addition(): assert append(22, 23) == 45
--------------------------------------------------------------------------------
[Input ] def amplify(value_1, value_2): return value_1 * value_2
[Output] def test_multiplying_two_numbers(): assert amplify(64, 55) == 3060
--------------------------------------------------------------------------------
[Input ] def divide_numbers(number_a, number_b): return number_a / number_b
[Output] def test_divide_operation(): assert divide_numbers(8, 93) == 0
--------------------------------------------------------------------------------
[Input ] def calculate_quotient(x, y): return x / y
[Output] def test_quotient(): assert calculate_quotient(16, 50) == 0
--------------------------------------------------------------------------------
[Input ] def take_away(a, b): return a - b
[Output] def test_subtracting_two_numbers(): assert take_away(66, 83) == -17
--------------------------------------------------------------------------------
[Input ] def calculate_quotient(x, y): return x / y
[Output] def test_divide_operation(): assert partition(57, 63) == 0
--------------------------------------------------------------------------------
[Input ] def replicate(a, b): return a * b
[Output] def test_multiplying_two_numbers(): assert replicate(10, 50) == 400
--------------------------------------------------------------------------------
```

### Usage

- Recommended Python version: `Python 3.11.5`
- Create Python environment:
  - Option 1 (conda):
    - `conda env create -f environment.yml`
    - `conda activate unit_test_generator`
  - Option 2 (pip):
    - `python -m venv .venv`
    - `source ./.venv/bin/activate`
    - Install dependencies:
        - Option 1: `python -m pip install -r requirements.txt`
        - Option 2: `python -m pip install tensorflow==2.14.0`
- The first run might take long!
- To run prediction: `python pred.py`
- To generate dataset: `python data.py`
- To run training: `python train.py`
