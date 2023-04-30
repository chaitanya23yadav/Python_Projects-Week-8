from random import randint
dct = {
    1:  ' ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲\n│          │\n│    ⬤    │\n│          │\n ‾‾‾‾‾‾‾‾‾‾',
    2:  ' ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲\n│ ⬤       │\n│          │\n│       ⬤ │\n ‾‾‾‾‾‾‾‾‾‾',
    3:  ' ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲\n│ ⬤       │\n│    ⬤    │\n│       ⬤ │\n ‾‾‾‾‾‾‾‾‾‾',
    4:  ' ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲\n│ ⬤    ⬤ │\n│          │\n│ ⬤    ⬤ │\n ‾‾‾‾‾‾‾‾‾‾',
    5:  ' ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲\n│ ⬤    ⬤ │\n│    ⬤    │\n│ ⬤    ⬤ │\n ‾‾‾‾‾‾‾‾‾‾',
    6:  ' ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲ ̲\n│ ⬤    ⬤ │\n│ ⬤    ⬤ │\n│ ⬤    ⬤ │\n ‾‾‾‾‾‾‾‾‾‾'
}
user = int(input('No.of throws : '))
stack = []
for i in range(user):
    stack.append(randint(1, 6))
for i in stack:
    print(dct[i])
