#1 
class str1:
    def __init__(self):
        self.string=''
    def getstr(self):
        self.string=str(input())
    def printup(self):
        print(self.string.upper())

ans=str1()
ans.getstr()
ans.printup() 

#2 
class s:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class square(s):
    def __init__(self, side_length):
        super().__init__
        self.side_length = side_length
        
    def area(self):
        return self.side_length*self.side_length
    
square = square(5)
print(square.area())
s = s()
print(s.area())

#3 
class R(s):
    def __init__(self, length, width):
        super().__init__
        self.length = length
        self.width = width
    def area (self):
        return(self.length * self.width)

R = R(5, 4)
print(R.area())
s=s()
print(s.area())

#4 
import math
class er:
    def __init__(self, a, b, godx, gody):
        self.a = a
        self.b = b
        self.godx = godx
        self.gody = gody  
    def f1(self):
        return( self.a, self.b)
    def f2(self):
        self.godx = self.godx + self.a
        self.gody = self.gody + self.b
        return(self.godx,self.gody)
    def f3(self):
        return(math.sqrt((self.a - self.godx)**2 + (self.b - self.gody)**2))


er = er(1, 2, 3, 4)
print(er.f1())
print(er.f2())
print(er.f3())
#5      
class ba():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def dep(self, amount):
        if(amount>=0):
             self.balance = self.balance + amount
             return(self.balance)
        else:
            return("amount is less than 0")
    def wd(self, amount):
        if amount>=0 and amount <=self.balance:
            self.balance=self.balance-amount
            return(self.balance)
        else:
            return("amount is greater than balance")
account = ba("ramazan", 1000000)
print(account.dep(500000))
print(account.wd(800000))


#6 
def pr(count):
    num=0
    if(count==0 or count==1):
        return False
    for i in range(2,count):
        if count%i==0:
            num=num+1
    if num==0:
        return True
    else:
        return False
        
list_nums = [int(s) for s in input().split()]
primes = list(filter(lambda count:pr(count), list_nums))
for i in range(len(primes)):
    print(primes[i], end=' ')