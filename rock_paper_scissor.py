from random import randint
while True:
    moves = ('rock', 'paper', 'scissor', 'rock')
    player = (input('\nChoose : ').lower())
    if player not in moves:
        print('Invalid Move')
        continue
    system = moves[randint(0, 3)]
    print('System :', system)
    if player == system:
        print('Draw')
    else:
        print('You Lose' if moves[moves.index(player) + 1] == system else 'You Win')
    k = input('\nplay again (1) / exit (0)\n')
    if k != '1':
        break
