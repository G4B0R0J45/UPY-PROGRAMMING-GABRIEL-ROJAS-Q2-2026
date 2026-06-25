# Required Structures
pronouns = ["Yo", "Tú", "El", "Nosotros", "Vosotros", "Ellos"]

endings = {
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"]
}

# INPUT
verb = input("Write a spanish verb (ar/er/ir): ")

stem = verb[:-2] #Get the stem
ending = verb[-2:] #Get the ending

conjugations = endings[ending]

for index, pronoun in enumerate(pronouns):
    termination = conjugations[index]
    print(f"{pronoun} {stem}{termination}")

