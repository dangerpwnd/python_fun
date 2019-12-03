import json
from difflib import get_close_matches

# pull dictionary data
data = json.load(open("data.json"))

# Word Search function
def translate(w):
    # makes all input lowercase
    w = w.lower()
    # If match return definition
    if w in data:
        return data[w]
    # If proper noun return with proper casing
    elif w.title() in data:
        return data[w.title()]
    # If acronym return with upper casing
    elif w.upper() in data:
        return data[w.upper()]
    # If not exact match return close 
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        suggest = input("Did you mean %s instead? Y or N " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if suggest == "Y":
            return data[get_close_matches(w,data.keys(), cutoff=0.8)[0]]
        elif suggest == "y":
            return data[get_close_matches(w,data.keys(), cutoff=0.8)[0]]
        else:
            return "Try again"
    # If not close, notify user and finish script
    else:
        return "The word doesn't exist. Please double check it."
# User input for word search
word = input("Enter word: ")


# Output list to be processed
output = translate(word)
# Print out each line of definitions if a list
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)