from random import randint
while True:
    target = randint(1, 11)
    guess = -1
    turns = 10
    while guess != target and turns > 0:
        guess = int(input('\nEnter Your Guess : '))
        turns = turns - 1
    score = (turns + 1) * 10
    print('\nYOUR SCORE : %d' % score if score > 0 else '\nYOUR SCORE : 0\n---YOU LOSE---')
    k = input('\nrestart / exit\n')
    if k != 'restart':
        break
