# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        contents = f.read()
        return contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    as_key = text.count("as")
    would_key = text.count("would")
    print("as:", as_key,", would:", would_key)
    
    #return {"as": 10, "would": 20}


count_words()
