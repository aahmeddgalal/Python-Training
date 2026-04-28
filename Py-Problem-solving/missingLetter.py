# The problem is that kids while learning the alphabet may make mistakes by excluding some letters or so on

# The solutions: A functions that has the alphabet correctly in it and can detect any mistakes 

def findthemissingletter(sequance): #abde
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    start = alphabet.find(sequance[0].lower())
    end = alphabet.find(sequance[-1].lower())
    missed = ''
    alphSeq = alphabet[start:(end+1)]
    
    if alphabet[start:(end + 1)] == sequance:
        print("The sequance is right, BRAVO!")
    else:
        for char in alphSeq: # abcde 
            if char not in sequance:
                missed += char
        print(f'You missed [{missed}] letter/s')


findthemissingletter("af")