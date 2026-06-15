def reversed_string():
    #return word[::-1]
    for i in range(len(word)):
        print(word[len(word)-1-i],end="")

word = "This is a string"
print(reversed_string())


