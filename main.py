def primeseive(num):
    prime = [ True for i in range(num+1)]
    p =  2
    while(p * p <= num):
        if(prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            print(p)
num = int(input())
print("THE FOLLOWING ARE PRIME NUMBERS", num)
primeseive(num)