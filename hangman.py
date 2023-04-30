from random import randint
dct = {
    1: ['power', '_o__r', 'p_we_'],
    2: ['insect', '_n_ec_', 'i_s__t'],
    3: ['piano', 'p__n_', '_ia_o'],
    4: ['error', '_r__r', 'e_ro_'],
    5: ['river', 'r_v__', '_i_er']
}
dct1 = {
    0: "\n    +---+\n        |\n        |\n        |\n       ===",
    1: "\n    +---+\n    O   |\n        |\n        |\n       ===",
    2: "\n    +---+\n    O   |\n    |   |\n        |\n       ===",
    3: "\n    +---+\n    O   |\n   /|   |\n        |\n       ===",
    4: "\n    +---+\n    O   |\n   /|\  |\n        |\n       ===",
    5: "\n    +---+\n    O   |\n   /|\  |\n   /    |\n       ===",
    6: "\n    +---+\n    O   |\n   /|\  |\n   / \  |\n       ===",
}
guessed = []
k = dct[randint(1, 5)]
print('guess the word')
f = 0
while f < 6:
    print(dct1[f])
    print(k[1])
    user = input()
    guessed.append(user)
    if user in k[2]:
        m = k[2].index(user)
        k[1] = k[1][:m] + user + k[1][m+1:]
        k[2] = k[2][:m] + '_' + k[2][m+1:]
    else:
        f = f + 1
    if k[1] == k[0]:
        print(k[0], 'is the word')
        break
    print('you guessed :', *guessed)
else:
    print(dct1[6])
    print('Game Over')
