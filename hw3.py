import string
    
def caesar(message, key):
    # return the encoded message as a single string!
    
    string.ascii_lowercase
    alphabet = string.ascii_lowercase + " "
    letters = {}
    for (i,letter) in enumerate(alphabet):
        letters[i] = letter
    
    coded_message = {}
    for (j,letter) in enumerate(alphabet):
        coded_message[letter] = ((j+key)%27)
        
    output = ''
    for each_letter in message:
        letter_to_number = coded_message[each_letter]
        number_to_letter = letters[letter_to_number]
        output = output + number_to_letter
    
    return output 
        
message = "hi my name is caesar"; key = 3
coded_message = caesar(message, key)

decoded_message = caesar(coded_message, -3)
print(decoded_message)
        