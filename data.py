import random

ops = {
    '+': [
        [
            'add',
            'sum',
            'plus',
            'add_numbers',
            'add_values',
            'calculate_sum',
            'accumulate',
            'total',
            'combine',
            'append',
        ],
        [
            'test_addition',
            'test_sum',
            'test_adding_two_numbers',
            'should_add_numbers_correctly',
            'verify_add_function',
            'check_simple_addition',
            'addition_test_case',
            'validate_addition_results',
            'assert_addition_works',
            'test_plus_operation',
        ]
    ],
    '-': [
        [
            'subtract',
            'minus',
            'deduct',
            'subtract_numbers',
            'remove',
            'decrease',
            'lessen',
            'deduct_values',
            'reduce',
            'take_away',
        ],
        [
            'test_subtraction',
            'test_difference',
            'test_subtracting_two_numbers',
            'should_subtract_numbers_correctly',
            'verify_subtract_function',
            'check_simple_subtraction',
            'subtraction_test_case',
            'validate_subtraction_results',
            'assert_subtraction_works',
            'test_minus_operation',
        ]
    ],
    '*': [
        [
            'multiply',
            'product',
            'times',
            'multiply_numbers',
            'calculate_product',
            'amplify',
            'expand',
            'double',
            'scale',
            'replicate',
        ],
        [
            'test_multiplication',
            'test_product',
            'test_multiplying_two_numbers',
            'should_multiply_numbers_correctly',
            'verify_multiply_function',
            'check_simple_multiplication',
            'multiplication_test_case',
            'validate_multiplication_results',
            'assert_multiplication_works',
            'test_times_operation',
        ]
    ],
    '/': [
        [
            'divide',
            'quotient',
            'split',
            'divide_numbers',
            'halve',
            'separate',
            'partition',
            'break_down',
            'calculate_quotient',
            'distribute',
        ],
        [
            'test_division',
            'test_quotient',
            'test_dividing_two_numbers',
            'should_divide_numbers_correctly',
            'verify_divide_function',
            'check_simple_division',
            'division_test_case',
            'validate_division_results',
            'assert_division_works',
            'test_divide_operation',
        ]
    ]
}

params = [
    ['a', 'b'],
    ['x', 'y'],
    ['num1', 'num2'],
    ['first', 'second'],
    ['number_a', 'number_b'],
    ['value_1', 'value_2'],
]


def get_ans(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a // b


def gen_src_func(op, src_name):
    a_name, b_name = random.choice(params)
    return f'def {src_name}({a_name}, {b_name}): return {a_name} {op} {b_name}'


def gen_test_func(op, src_name):
    test_name = random.choice(ops[op][1])
    a_value = random.randint(1, 100)
    b_value = random.randint(1, 100)
    ans = get_ans(op, a_value, b_value)
    return f'def {test_name}(): assert {src_name}({a_value}, {b_value}) == {ans}'


def gen_sample():
    op = random.choice(list(ops.keys()))
    src_name = random.choice(ops[op][0])
    src_func = gen_src_func(op, src_name)
    test_func = gen_test_func(op, src_name)
    return f'{src_func}\n{test_func}'


data = ''
for _ in range(10_000):
    data += gen_sample() + '\n'
with open('dataset.txt', 'w') as f:
    f.write(data)
