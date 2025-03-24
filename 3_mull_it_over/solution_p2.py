import re

def extract_numbers(expression: str):
    numbers = re.findall(r"[0-9][0-9]?[0-9]?", expression)
    return numbers

def main():
    total_sum = 0
    input = open("input.txt").read()
    do_chunks = []
    dont_chunks = input.split("don't()")
    do_chunks.append(dont_chunks[0])
    dont_chunks.remove(dont_chunks[0])
    for chunk in dont_chunks:
        do_subchunks = chunk.split("do()")
        do_subchunks.remove(do_subchunks[0])
        for subchunk in do_subchunks:
            do_chunks.append(subchunk)
    for chunk in do_chunks:
        regex = r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)"
        filtered_input = re.findall(regex, chunk)
        for expression in filtered_input:
            first_number, second_number = extract_numbers(expression)
            product = int(first_number) * int(second_number)
            total_sum += product
    print(total_sum)
    
main()