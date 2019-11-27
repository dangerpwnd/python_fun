import json
data = json.load(open("data.json"))

def translate(w):
    wl = w.lower()
    if wl in data:
        return data[wl]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")



print(translate(word))