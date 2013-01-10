def crypto(key, code):
    string = ""
    weird = " ?!"
    for char in code.lower():
        if char in weird:
            string += char
            continue
        string += key[char]
    return string

if __name__ == "__main__":
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b',  'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}
    code = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
    print crypto(key, code)
