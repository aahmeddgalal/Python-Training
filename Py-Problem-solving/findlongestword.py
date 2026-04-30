mysent = "he how has a why to live, can bear almost anyanyy how89dggygd"

def find_longest(sentence):
    count = 0
    words = sentence.split(' ') #['he', 'how', 'has'...]
    for item in words:
        if len(item) > count:
            count = len(item)
            ind = words.index(item)
    
    return count, words[ind]

print(find_longest(mysent))

# There's a bug here - Comma is included ya bro 