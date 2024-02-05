def prime(s,e,i=1):
    while i<=e:
        if not(i%1==0 and i%i==0):
            print(i)
            i=i+1
prime(1,20)
            
