import re

def extract_numbers(expression: str):
    numbers = re.findall(r"[0-9][0-9]?[0-9]?", expression)
    return numbers

def main():
    total_sum = 0
    input = open("input.txt").read()
    regex = r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)"
    filtered_input = re.findall(regex, input)
    for expression in filtered_input:
        first_number, second_number = extract_numbers(expression)
        product = int(first_number) * int(second_number)
        total_sum += product
    print(total_sum)
    
main()