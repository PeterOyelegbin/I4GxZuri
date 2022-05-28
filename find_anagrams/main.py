# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(word1, word2):
    # [assignment] Add your code here
    w1 = sorted(word1.lower())
    w2 = sorted(word2.lower())
    
    if (w1 == w2):
        print("True")
    else:
        print("False")


find_anagrams("Heart", "Earth")
