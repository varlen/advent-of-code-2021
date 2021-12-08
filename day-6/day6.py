from collections import Counter, defaultdict

input_file_path = 'input.txt'

with open(input_file_path) as file:
    input = list(map(int,file.readline().strip().split(',')))

# input = list(map(int,'3,4,3,1,2'.split(',')))

initial_state = Counter(input)
days = 80

def compute_next_state(state):
    next_state = defaultdict(lambda : 0)
    
    if 0 in state:
        next_state[6] += state[0]
        next_state[8] += state[0]
    for cooldown in range(1,9):
        if cooldown in state and state[cooldown] > 0:
            next_state[cooldown - 1] += state[cooldown]
    
    return dict(next_state)

current_state = initial_state
for day in range(256):
    current_state = compute_next_state(current_state)
    lanternfish_population = sum(current_state.values())
    print(f"Day {day+1:2}: {lanternfish_population} 🐟 : {current_state}")




