
a = int(input("Enter 1 for converting the message to secret code and 0 for decoding\n"))

str = input("Enter the message\n")

mess = str.split(" ")

def encodeMess():
    new = []
    for i in mess:
        if (len(i) >= 3):
            r1 = "mgk"
            r2 = "xij"
            strnew = r1 + i[1:] + i[0] + r2
            new.append(strnew)
        else:
            new.append(i[::-1])

    print(" ".join(new))

def decodeMess():
    new = []
    for i in mess:
        if(len(i) >= 3):
            r1 = "mgk"
            r2 = "xij"
            strnew = i[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            new.append(strnew)

        else:
            new.append(i[::-1])

    print(" ".join(new))


if(a == 0):
    decodeMess()
elif(a == 1):
    encodeMess()
else:
    print("Invalid input")        


