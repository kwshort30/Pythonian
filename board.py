import random

# board
def board(lst):
    print(lst[1] + '|' + lst[2] + '|' + lst[3])
    print('-----')
    print(lst[4] + '|' + lst[5] + '|' + lst[6])
    print('-----')
    print(lst[7] + '|' + lst[8] + '|' + lst[9])


def pick_who_goes_first():
	return random.choice([ "X", "O" ])
