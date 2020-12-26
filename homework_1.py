import logging
from logging.handlers import RotatingFileHandler
import os
# test

operators = ("+", "-", "*", "/", "add", "sub", "mul", "div")
operators_list = []
operands = [0] * 2
expr = input()

logger = logging.getLogger("My logger")
log_dir = '.'
log_file_name = "davo.log"

logger.setLevel(logging.INFO)
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, log_file_name)
# 1GB for log files
log_handler = RotatingFileHandler(log_path, maxBytes=204800000, backupCount=50000)
formater = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
log_handler.setFormatter(formater)
logger.addHandler(log_handler)

logger.error("I think I should have written something")
logger.info("Here as well")


def infix_operation(expr):
    this_list = expr.split()
    if this_list[0] not in operators:
        print("Invalid expression")
        return
    for x in this_list:
        if x in operators:
            operators_list.append(x)
            continue
        else:
            if x.isnumeric():
                if operands[0] == 0:
                    operands[0] = float(x)
                else:
                    operands[1] = float(x)
                    current_oper = operators_list.pop()
                    if current_oper == "+" or current_oper == "+":
                        operands[0], operands[1] = operands[0] + operands[1], 0
                    elif current_oper == "-" or current_oper == "sub":
                        operands[0], operands[1] = operands[0] - operands[1], 0
                    elif current_oper == "*" or current_oper == "mul":
                        operands[0], operands[1] = operands[0] * operands[1], 0
                    elif current_oper == "/" or current_oper == "div":
                        operands[0], operands[1] = operands[0] / operands[1], 0
            else:
                print("Invalid expression")
                return
    return operands[0]

print("Expression: " + expr)
print("Result: " + str(infix_operation(expr)))

