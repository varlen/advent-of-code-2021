# https://adventofcode.com/2021/day/3
from functools import reduce
from collections import Counter
import statistics

input_file_path = 'input.txt'

# gamma rate -> most common bit in the position
# epsilon_rate -> least common bit --> !most common (1 or 0)

def run():

    with open(input_file_path) as file:
        file_content = file.readlines()

    number_of_bits = len(file_content[0].strip())

    def reducer(accumulator, current):
        for i in range(number_of_bits):
            accumulator[i].append(current[i])
        return accumulator

    bit_lists = reduce(
        reducer, 
        file_content, 
        [ [] for bit in range(number_of_bits) ]
    )

    binary_gamma_rate = ''.join(
        map(
            lambda bit_list : statistics.mode(bit_list), 
            bit_lists
        )
    )

    print(binary_gamma_rate)
    gamma_rate = int(binary_gamma_rate, base=2)
    # Bitwise not done by hand, limited to number of bits 
    # ~ operator will flip undersided bits 
    epsilon_rate = (1 << number_of_bits ) - 1 - gamma_rate
    power_consumption = gamma_rate * epsilon_rate
    print("Part 1:")
    print(f"{gamma_rate=} {epsilon_rate=} ")
    print(f"{power_consumption =}")

    binary_epsilon_rate = f"{epsilon_rate:b}"
    print(f"{binary_epsilon_rate=}")

    ##### Part 2
    def extract_oxygen_bit_criteria(bit_list):
        most_common_values = statistics.multimode(bit_list)
        return most_common_values[0] if len(most_common_values) == 1 else '1'

    def extract_co2_scrubber_criteria(bit_list):
        counts = Counter(bit_list)
        return '0' if counts['0'] <= counts['1'] else '1'


    oxygen_generator_rating_scope = file_content
    scrubber_rating_scope = file_content
    oxygen_generator_rating = None
    scrubber_rating = None
    oxygen_generator_rating_found = False
    scrubber_rating_found = False
    oxygen_bit_list = bit_lists[0]
    scrubber_bit_list = bit_lists[0]
    for bit_position in range(number_of_bits):
        if not oxygen_generator_rating_found:
            oxygen_bit_criteria = extract_oxygen_bit_criteria(oxygen_bit_list)
            oxygen_generator_rating_scope = list(filter(
                lambda binary : binary[bit_position] == oxygen_bit_criteria,
                oxygen_generator_rating_scope
            ))
            oxygen_bit_list = map(lambda x : x[bit_position], oxygen_generator_rating_scope)
            if len(oxygen_generator_rating_scope) == 1:
                oxygen_generator_rating_found = True
                print(oxygen_generator_rating_scope[0])
                oxygen_generator_rating = int(oxygen_generator_rating_scope[0], base=2)

        if not scrubber_rating_found:
            scrubber_bit_criteria = extract_co2_scrubber_criteria(scrubber_bit_list)
            print(f"{ scrubber_bit_criteria =} { bit_position =} { scrubber_rating_scope[0][bit_position] =} {len(scrubber_rating_scope) =}")

            scrubber_rating_scope = list(filter(
                lambda binary : binary[bit_position] == scrubber_bit_criteria,
                scrubber_rating_scope
            ))
            scrubber_bit_list = map(lambda x : x[bit_position], scrubber_rating_scope)
            if len(scrubber_rating_scope) == 1:
                scrubber_rating_found = True
                print(scrubber_rating_scope[0])
                scrubber_rating = int(scrubber_rating_scope[0], base=2)
        
        if scrubber_rating_found and oxygen_generator_rating_found:
            break
        

    print("Part 2:")
    print(f"{oxygen_generator_rating=} {scrubber_rating=}")
    print(f"{oxygen_generator_rating * scrubber_rating =}")

run()