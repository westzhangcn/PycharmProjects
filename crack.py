
from string import ascii_letters, digits, punctuation
from itertools import product

for passcode in product(ascii_letters, repeat=4):
    ...print(&passcode)