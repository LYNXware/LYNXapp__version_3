test = {
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd'
}

test2 = {
    'a': '1',
    'b': '2',
}


print(test)

test |= test2

print(test)