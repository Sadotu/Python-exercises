def char_freq(string):
    count = {}
    for x in string:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    return count

if __name__ == "__main__":
    string = "abbabcbdbabdbdbabababcbcbab"
    print char_freq(string)
