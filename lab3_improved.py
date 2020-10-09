def main():
    process = selectEncryptOrDecrypt()
    key = getKey()
    message = getMessage(process)
    
#    print("")

    playfairMessage = ""
    for i in range(0, len(message), 2):
        bigram = message[i:i+2]
        
        finishedBigram = getPlayfairedBigram(bigram, key, process)

        playfairMessage += finishedBigram
    
    print("")
    print("Your final message is: ")
    print(f"|||{playfairMessage}|||")

    # Great for debugging, shows the table
#    print("")
#    for i in range(5):
#        print(key[5*i:5*i+5])

def selectEncryptOrDecrypt():
    print("Would you like to:")
    print("(1) Encrypt")
    print("(2) Decrypt")
    choice = int(input())
    return choice

def getKey():
    Alphabet = "ABCDEFGHIJKLMNOPRSTVWXYZ "
    key = input("Please enter a key: ")
    
    key = key.replace('u', 'v')
    key = key.replace('q', 'k')
    key = key.upper()
    key += Alphabet
    
    fullKey = ""
    for i in range(len(key)):
        if key[i] not in fullKey:
            fullKey += key[i]

    return fullKey

def getMessage(process):
    if process == 1:
        print("Please enter a message to encrypt:")
    else:
        print("Please enter a message to decrypt:")

    message = input()
    
    message = message.replace('u', 'v')
    message = message.replace('q', 'k')
    message = message.upper()
    
    if len(message) % 2 == 1:
        message += "X"

    for i in range(len(message) // 2):
        if message[2*i] == message[2*i + 1]:
            message = message[:2*i] + "X" + message[2*i + 1:]

    return message

def getPlayfairedBigram(bigram, key, process):
    if process == 1:
        option = 1
    else:
        option = -1

    r1 = key.find(bigram[0]) // 5
    r2 = key.find(bigram[1]) // 5
    c1 = key.find(bigram[0]) % 5
    c2 = key.find(bigram[1]) % 5

#   Great for debugging vvv
#    print(f"{bigram[0]} {r1} {c1} {bigram[1]} {r2} {c2}")

# Rule 2
    if c1 == c2:
        # If they are on the end, make their index -1, so we can +1 at the end to make it 0
        if r1 == 4:
            r1 = -1
        if r2 == 4:
            r2 = -1

        r1 += option
        r2 += option

        if r1 == -2:
            r1 = 3
        if r2 == -2:
            r2 = 3
        if r1 == -1:
            r1 = 4
        if r2 == -1:
            r1 = 4

        finishedBigram = key[(5 * r1) + c1] + key[(5 * r2) + c2]

# Rule 1
    elif r1 == r2:
        # Same as before, but with columns now
        if c1 == 4:
            c1 = -1
        if c2 == 4:
            c2 = -1

        c1 += option
        c2 += option

        if c1 == -2:
            c1 = 3
        if c2 == -2:
            c2 = 3
        if c1 == -1:
            c1 = 4
        if c2 == -1:
            c2 = 4

        finishedBigram = key[(5 * r1) + c1] + key[(5 * r2) + c2]

# Rule 3
    else:
        # Swaps rows to make a 'rectangle'
        finishedBigram = key[(5 * r2) + c1] + key[(5 * r1) + c2]

    
    return finishedBigram

main()
