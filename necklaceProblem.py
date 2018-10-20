n1 = int(input('Provide one single digit number.')) #1
n2 = int(input('Put in another single digit number. '))

print("n1 is " + str(n1))
print("n2 is " + str(n2))

neckLace = []
FOUND = False

neckLace.append(n1)
neckLace.append(n2)
    
while not FOUND:
    
    temp = neckLace[-2] + neckLace[-1]
    n4 = int(str(temp)[-1:])
    neckLace.append(n4)
    
    if neckLace[-2] == n1 and neckLace[-1] == n2:
        FOUND = True
        print("necklace is formed.")
        break

print(*neckLace,sep=' ', end='\n')

    

    
