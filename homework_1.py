import os
from datetime import datetime

ERROR_COUNT = 0
INFO_COUNT = 0

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = os.path.join(ROOT_DIR, "logging")
LOG_FILE_PATH = os.path.join(LOG_DIR, 'logging.log')

os.makedirs(LOG_DIR, exist_ok=True)


def write_error(input_string, error_msg):
    with open(LOG_FILE_PATH, "a+") as log:
        log.write(f"{datetime.now()} :: ERROR :: {error_msg} :: {input_string}\n")


def write_info(input_string, res):
    with open(LOG_FILE_PATH, "a+") as log:
        log.write(f"{datetime.now()}:: INFO:: {input_string} :: {res}\n")


def is_operator(character: str) -> bool:
    if character in ("+", "-", "*", "/", "add", "sub", "mul", "div"):
        return True
    return False


def error_in_input(calc_string: str) -> bool:
    numerics = 0
    operators = 0
    calc_list = calc_string.split()

    if not is_operator(calc_list[0]) or not calc_list[-1].isnumeric() or \
            not calc_list[-2].isnumeric():
        write_error(" ".join(calc_list), "First item - operator, last 2 items - floats")
        return True

    for element in calc_list[1:-2]:
        if element.isnumeric():
            numerics += 1
            continue
        elif is_operator(element):
            operators += 1
            continue
        write_error(" ".join(calc_list), "Numeric or operator")
        return True

    # numerics should be equal to operands after first if
    if numerics != operators:
        write_error(" ".join(calc_list), "Items count")
        return True

    return False


def prefix_calc(calc_string: str) -> float:
    global ERROR_COUNT
    global INFO_COUNT

    calc_list = calc_string.split()
    if error_in_input(calc_string):
        ERROR_COUNT += 1
    else:
        operands = []
        while calc_list:
            last_item = calc_list.pop()
            if is_operator(last_item):
                ending = operands.pop()
                prev_ending = operands.pop()
                if last_item == "+" or last_item == "add":
                    operands.append(ending + prev_ending)
                elif last_item == "-" or last_item == "sub":
                    operands.append(ending - prev_ending)
                elif last_item == "*" or last_item == "mul":
                    operands.append(ending * prev_ending)
                elif last_item == "/" or last_item == "div":
                    operands.append(ending / prev_ending)
            else:
                operands.append(float(last_item))

        write_info(calc_string, operands[0])
        INFO_COUNT += 1
        return operands[0]


while True:
    input_str = input("Expression: ")
    result = prefix_calc(input_str)
    print(f"Result:  {result}" if result is not None else "ERROR: Invalid expression")
    print("Report: Info-{}, ERROR-{}".format(INFO_COUNT, ERROR_COUNT))


