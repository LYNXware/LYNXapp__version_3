
from memory import loadLanguage


letters = {
    'a': '\x61',
    'b': '\x62',
    'c': '\x63'
}

numbers = {
    '0': 0x30,
    '1': 0x31,
    '2': 0x32
}

english_ascii = {
    'letters': letters,
    'numbers': numbers

}

print(english_ascii['letters']['a'])

# with open("../LYNXapp_Memory/language/english.json", "w") as outfile:
    # write the dictionary to the file in JSON format
#     json.dump(english_ascii, outfile, indent=4)
#
# with open("../LYNXapp_Memory/language/english.json", "r") as infile:
#     # read the JSON data from the file into a dictionary
#     person = json.load(infile)

# print(person['letters']['a'])

l = loadLanguage('english')

print(l['letters']['a'])