import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        suggest = input("Did you mean %s instead? Y or N " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if suggest == "Y" | suggest == "y":
            return data[get_close_matches(w,data.keys(), cutoff=0.8)[0]]
        else:
            return "Try again"
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")



print(translate(word))