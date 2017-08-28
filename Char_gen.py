#char generator

import random

def Attribute():
    a = [1]*3
    b = [1]*3
    c = [1]*3
    n = []
    Attributes = [0]*18

    
    

    for i in range (5):
        n = random.randint(0,2)
        if(a[n] == 4 and i == 3 and random.randint(0,1)):
            a[n] += 1
            break
        else:
            a[n] += 1

    for i in range (4):
        n = random.randint(0,2)
        while(b[n] == 4):
            n = random.randint(0,2)
        b[n] += 1

    for i in range (3):
        c[random.randint(0,2)] += 1

    n = [a,b,c]
    random.shuffle(n)

    for i in range(3):
        Attributes[2*i+1] = n[0][i]
    for i in range(3):
        Attributes[2*i+7] = n[1][i]
    for i in range(3):
        Attributes[2*i+13] = n[2][i] 
    

    Attributes[0] = "Strength"
    Attributes[2] = "Dexterity"
    Attributes[4] = "Stamina"
    Attributes[6] = "Intelligence"
    Attributes[8] = "Wits"
    Attributes[10] = "Resolve"
    Attributes[12] = "Presence"
    Attributes[14] = "Manipulation"
    Attributes[16] = "Composure"
    
    return Attributes

def virtue():
    virtue = ["Charity", "Faith", "Fortitude", "Hope", "Justice", "Prudence", "Temperance"]
    return virtue[random.randint(0,6)]

def vice():
    vice = ["Envy", "Gluttony", "Greed", "Lust", "Pride", "Sloth", "Wraith"]
    return vice[random.randint(0,6)]

def listRandom(a,n,k):
    b = [k-n]
    for i in range (len(b)):
        b[i] = a[n+i]
        
    random.shuffle(b)
    
    for i in range (len(b)):
        a[n+i] = b[i]
    

def char_calc(n):
    n.append("Health")
    n.append(n[5] + 5)
    n.append("Willpower")
    n.append(n[11]+n[17])
    n.append("Size")
    n.append(5)
    n.append("Defense")
    if(n[3] > n[9]):
        n.append(n[9])
    else:
        n.append(n[3])
        
    n.append("Initiative")
    n.append(n[3] + n[17])
    n.append("Speed")
    n.append(n[1] + n[3] + 5)
    n.append("Morality")
    n.append(7)
    n.append("Virtue")
    n.append(virtue())
    n.append("Vice")
    n.append(vice())
    return n

print(char_calc(Attribute()))

    
    

