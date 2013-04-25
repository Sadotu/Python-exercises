def make_ing_form(string):
    extension1 = ["e"]
    extension2 = ["ie"]
    if filter(string.endswith, extension2):
        infinitive = string[:-2] + "ying"
    elif filter(string.endswith, extension1):
        infinitive = string[:-1] + "ing"
    else:
        return False
    return infinitive

vowels = set(["a", "e", "i", "o", "u"])

def vowel(vowels, word):
    if len(word) != 3:
        return False
    if word[0] not in vowels and word[1] in vowels and word[2] not in vowels:
        tlw = word + word[-1]
        tlw = tlw + "ing"
        return tlw
    return False

if __name__ == "__main__":
    words = ["make", "skie", "get"]
    for word in words:
        if make_ing_form(word):
            print make_ing_form(word)
        if vowel(vowels, word):
            print vowel(vowels, word)
