##pbrlm1
##sum=0
##for i in range(0,1000):
##    if i%5==0 or i%3==0:
##        
##        sum+=i
##print(sum)


#pbrlm2

##a=0
##b=1
##even=0
##d=10
##sum=0
##for i in range(1,10):
##    
##    c=a+b
##    a=b
##    b=c
##    print(c)
    
##    if c%2==0:
##        
##        even+=c
##print(even)
        
    
    
##pbrlm3
##n = 600851475143
##i = 2
##while i < n:
##   
##    while n % i == 0:
##         
##         n = n / i
##         
##    i = i + 1
##
##print (n)


##pbrlm4
##print(max([x * y for x in range(1000) for y in range(x) if str(x * y) == str(x * y)[::-1]]))


##pbrlm5
##def num(number):
##    
##
##    for i in range(2,11):
##        
##        if number%i!=0:
##        
##            
##            return False
##    return True
##number=10
##while True:
##    if num(number):
##        break
##    number=number+10
##print(number)

##pbrlm6
##sum=0
##for i in range(101):
##    c=i**2
##    sum=sum+c
##e=sum
##
##sum=0
##for i in range(101):
##    sum=sum+i
##    c=sum**2
##f=c
##
##g=f-e
##print(g)

##pbrlm7
##not solved



##pbrlm 8
##not solved



##pbrlm9
##for c in range(1, 500): 
##	for b in range(1, c):
##		for a in range(1, b):
##			if a + b + c == 1000 and a*a + b*b == c*c:
##				print(a*b*c)


##pbrlm10
##list=[]
##a=int(input())

##for i in range(2,a+1):
    ##isPrime=True
    ##for j in range(2,int(i**0.5)+1):
        ##if i%j==0:
            ##isPrime=False
            ##break
    ##if  isPrime:
        ##list.append(i)
##print(sum(list))
        


