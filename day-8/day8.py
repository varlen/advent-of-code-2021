from functools import reduce
from collections import defaultdict, namedtuple

def line_parser(accumulator, update):
    input_parts = update.split(' | ')
    accumulator[0].append(input_parts[0].split(' '))
    accumulator[1].append(list(map(lambda s : s.strip(), input_parts[1].split(' '))))
    return accumulator

IO = namedtuple('IO', 'wires display')
with open('input.txt') as file:
    input,output = reduce(line_parser, file.readlines(), ([], []))

digits_to_segment_count = {
    1 : 2,
    4 : 4,
    7 : 3,
    8 : 7
}

easily_identifiable_digits = len(list(
    filter(
        lambda str_size : str_size in digits_to_segment_count.values(), 
        map(len, [ x for f in output for x in f ])
    ))
)

# Part 1
print(f"{easily_identifiable_digits =}")

# -- Part 2
"""
            upper                          UP
upper left          upper right          UL  UR
            middle                  ==>    MD
lower left          lower right          LL  LR
            lower                          LO

"""

ONE = set(['UR','LR'])
FOUR = set(['UL','MD','UR','LR'])
SEVEN = set(['UP','UR','LR'])
EIGHT = set(['UP','UR','MD','UL','LL','LR','LO'])

SIX = set(EIGHT)
SIX.discard('UR')
ZERO = set(EIGHT)
ZERO.discard('MD')
FIVE = set(SIX)
FIVE.discard('LL')
NINE = set(EIGHT)
NINE.discard('LL')
TWO = set(EIGHT)
TWO.difference_update(set(['UL','LR']))
THREE = set(EIGHT)
THREE.difference_update(set(['UL','LL']))

decoded_values = []

for line_index, sequence in enumerate(input):
    segment_dict = {
        'UP' : None,

        'UL' : None,
        'UR' : None,
        'MD' : None,
        'LL' : None,
        'LR' : None,
        'LO' : None
    }
    length_dict = defaultdict(lambda : [])
    for word in sequence:
        length_dict[len(word)].append(set(list(word)))
    length_dict = dict(length_dict)
    # Find UP by the difference of 7 and 1
    segment_dict['UP'] = set(
        length_dict[digits_to_segment_count[7]][0]).difference(
            length_dict[digits_to_segment_count[1]][0]).pop()
    # Find UL, MD by 4 and 1
    UL_MD = set(
        length_dict[digits_to_segment_count[4]][0]).difference(
            length_dict[digits_to_segment_count[1]][0])
    # Find UP, MD, LO by intersection of digits that uses 5 segments
    UP_MD_LO = length_dict[5][0].intersection(length_dict[5][1]).intersection(length_dict[5][2])
    segment_dict['MD'] = UP_MD_LO.intersection(UL_MD).pop()
    segment_dict['UL'] = set(UL_MD).difference(set(segment_dict['MD'])).pop()
    segment_dict['LO'] = UP_MD_LO.difference(set([segment_dict['MD'], segment_dict['UP']])).pop()
    # Find LL by all previously found + 1 to form 9 and compare with 8
    nine_without_one = set([
        segment_dict['MD'], segment_dict['UP'], 
        segment_dict['UL'], segment_dict['LO']
    ])
    nine = nine_without_one.union(length_dict[digits_to_segment_count[1]][0])
    segment_dict['LL'] = set(length_dict[digits_to_segment_count[8]][0]).difference(nine).pop()
    # Find Upper Right
    lights_the_middle_segment = [ w for w in length_dict[6] if segment_dict['MD'] in w ]
    UR_LL = lights_the_middle_segment[0].symmetric_difference(lights_the_middle_segment[1])
    segment_dict['UR'] = UR_LL.difference(set([segment_dict['LL']])).pop()
    # Finally, find Lower Right
    segment_dict['LR'] = set(length_dict[2][0]).difference(set([segment_dict['UR']])).pop()

    generic_sets = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
    # Each set will map an integer
    decoder = { frozenset(map(lambda s : segment_dict[s], generic_sets[i])) : i for i in range(0,10) }
    output_sets = list(map(
        lambda active_wires : frozenset(list(active_wires)), 
        output[line_index]
    ))
    decoded_output = list(map(lambda encoded_set : decoder[encoded_set], output_sets))
    decoded_value = sum([ x * (10**i) for i,x in enumerate(reversed(decoded_output))])
    decoded_values.append(decoded_value)
print(f"{sum(decoded_values) =}")
    








    




