def make_3sg_form(string):
    extensions = ("sh", "o", "ch", "z", "x")
    if filter(string.endswith, extensions):
        infinitive = string + "es"
    elif string[-1] == "y":
        infinitive = string.replace("y", "ies")
    else:
        infinitive = string + "s"
    return infinitive

if __name__ == "__main__":
    words = ["brush", "fix", "notch", "fiz", "try", "make"]
    for word in words:
        print make_3sg_form(word)
