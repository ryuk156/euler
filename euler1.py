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
##import time
##start_time = time.time()
##num = "73167176531330624919225119674426574742355349194934\
##96983520312774506326239578318016984801869478851843\
##85861560789112949495459501737958331952853208805511\
##12540698747158523863050715693290963295227443043557\
##66896648950445244523161731856403098711121722383113\
##62229893423380308135336276614282806444486645238749\
##30358907296290491560440772390713810515859307960866\
##70172427121883998797908792274921901699720888093776\
##65727333001053367881220235421809751254540594752243\
##52584907711670556013604839586446706324415722155397\
##53697817977846174064955149290862569321978468622482\
##83972241375657056057490261407972968652414535100474\
##82166370484403199890008895243450658541227588666881\
##16427171479924442928230863465674813919123162824586\
##17866458359124566529476545682848912883142607690042\
##24219022671055626321111109370544217506941658960408\
##07198403850962455444362981230987879927244284909188\
##84580156166097919133875499200524063689912560717606\
##05886116467109405077541002256983155200055935729725\
##71636269561882670428252483600823257530420752963450"
##print(len(num))
##i = 0
##j = 0
##k = 0
##while i < len(num) - 13:
##    one = int(num[i])
##    two = int(num[i + 1])
##    three = int(num[i + 2])
##    four = int(num[i + 3])
##    five = int(num[i + 4])
##    six = int(num[i + 5])
##    seven = int(num[i + 6])
##    eight = int(num[i + 7])
##    nine = int(num[i + 8])
##    ten = int(num[i + 9])
##    eleven = int(num[i + 10])
##    twoelve = int(num[i + 11])
##    thirteen = int(num[i + 12])
##    j = one * two * three * four * five * six * seven * eight * nine * ten * eleven * twoelve * thirteen
##    i = i + 1
##    if k < j:
##        k = j
##print(k)
##print(time.time() - start_time," seconds")




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
        


