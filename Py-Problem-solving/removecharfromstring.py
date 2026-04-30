def find_Char(sentence, character):
    final = ''
    for char in sentence:
        if char != character:
            final += char
    return final
print(find_Char('AhmedDDDDDDDDDDD GalalDD doDnyDDaD', 'D')) 