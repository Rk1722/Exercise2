def isprime(n):
    prime = True
    if n == 1:
        prime = False
    elif n ==2 :
        prime = True
    elif n==3 :
        prime = True
    else:    
        for i in range(int(n**1/2)+1):
            if n%(i+2) == 0:
                prime = False
                break
    return prime


