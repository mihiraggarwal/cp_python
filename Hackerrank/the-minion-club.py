# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    k_count, s_count = 0, 0
    for i in range(len(string)):
        if string[i] in vowels:
            k_count += len(string[i:])
        else:
            s_count += len(string[i:])
    if k_count > s_count:
        print('Kevin '+str(k_count))
    elif s_count > k_count:
        print('Stuart '+str(s_count))
    else:
        print('Draw')

