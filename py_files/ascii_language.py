print('ascii_language.py')

from py_files.memory import loadAsciiLanguage
from py_files.preferences import prefs


# with open("../LYNXapp_Memory/language/english.json", "w") as outfile:
    # write the dictionary to the file in JSON format
#     json.dump(english_ascii, outfile, indent=4)
#
# with open("../LYNXapp_Memory/language/english.json", "r") as infile:
#     # read the JSON data from the file into a dictionary
#     person = json.load(infile)

# print(person['letters']['a'])


class AsciiTable:
    def __init__(self):
        loadAsciiLanguage(prefs.get('language_ascii'))

    def loadAsciiTable(self, language):
        table = loadAsciiLanguage(language)
        self.letters = table['letters']
        self.numbers = table['numbers']
        self.keypad = table['keypad']
        self.punctuations = table['punctuations']
        self.symbols = table['symbols']
        self.whithespaces = table['whitespaces']
        self.modifiers = table['modifiers']

        print(table)




asciiTable = AsciiTable()