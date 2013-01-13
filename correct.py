def correct(string):
    replace = string.replace(".", ". ")
    string = " ".join(replace.split())
    return string 

if __name__ == "__main__":
    string = "This   is  very funny  and    cool.Indeed!"
    print correct(string)
