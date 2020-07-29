
# This is the Master Branch
# adding a message.

def calcGcd(num1, num2):
    while (num1 != num2):
        if (num1 > num2):
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

def SetUpRsa(p, q):
    mylist = []
    mylist.append(p*q)
    totient = (p-1)*(q-1)
    for i in range(2, totient): # lets try making this for loop start at a random number between 2 and totient-1
        if (calcGcd(i, totient) == 1):
            e = i
            mylist.append(e)
            break
    for j in range(1, p*q):
        if (((e*j) % totient) == 1):
            d = j
            mylist.append(d)
            break
    return mylist

def encrypt(m, e, n):
    return m**e % n # we can speed this up by running a for loop to do the exponentiation

def decrypt(c, d, n):
    return c**d % n 

mylist = SetUpRsa(5, 7)
print(mylist)
message = 11
ciphertext = encrypt(message, mylist[1], mylist[0])

print("message: " + str(message))
print("ciphertext: " + str(ciphertext))
print("message: " + str(decrypt(ciphertext, mylist[2], mylist[0])))