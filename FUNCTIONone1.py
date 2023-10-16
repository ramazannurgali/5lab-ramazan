#1 
def s(a):
    print(28.3495231 * a)
a=float(input())
s(a)

#2 
def a(A):
    print(float((5 / 9) * (A - 32)))
A=float(input())
a(A) 

#3 
def R(a,B):
    rab=(B-2*a)/2
    chickens=a-rab
    print("chickens:",chickens)
    print("rabbits:",rab)
a=int(input())
B=int(input())
R(a, B) 

#4 
def F(n):
    a=0
    for i in range(2,n):
        if(n%i==0):
            a=a+1
    if(a==0):
        print(n,end=' ')
L = input().split()
for i in range(0, len(L)):
    F(int(L[i]))
     
#5 
from itertools import permutations
def A(a):
    list = list(a)
A=permutations(list)
for i in A:
    print(i)

    
#6 
def r(list):
    for i in range(len(list)-1,-1,-1):
        print(list[i],end=' ')
    
list = [str(s) for s in input().split(' ')]
r(list)

    
#7 
def r(list):
    for i in range(len(list)-1):
        if(list[i]==3 and list[i+1]==3):
            return True
    return False
list = [int(s) for s in input().split()]
print(r(list))

#8 
def e(list):
    for i in range(len(list)-2):
        if(list[i]==0 and list[i+1]==0 and list[i+2]==7):
            return True
    return False
list = [int(s) for s in input().split()]
print(e(list))

#9 
import math
def e(r):
    return(float((4/3)* math.pi * r) )
r = int(input())
print(float(e(r)))

#10 
def a(list):
    l=[]
    for i in list: 
        if i not in l: 
            l.append(i) 
    return(l)
    
list = [int(s) for s in input().split()] 

res_list = a(list)   
for i in res_list: 
    print(i, end=' ')

#11 
def q(s):
    if(s==s[::-1]):
        print("is polindrome")
    else:
        print("is not polindrome")
s=str(input())
q(s)

#12 
def w(list):
    for i in range(len(list)):
        for j in range(list[i]):
            print('*',end='')
        print('\n')
list=[int(s) for s in input().split()]
w(list) 

#13 
import random
def r(num):
    s=input("Hello! What is your name?")
    print("Well,",s,", I am thinking of a number between 1 and 20.")
    c = 1
    g = int(input("Take a guess:"))
    if(g<num):
            print("Your guess is too low.")
    else:
            print("Your guess is too hight.")
    while(g != num):
        g = int(input("Take a guess:"))
        
        if(g<num):
            print("Your guess is too low.")
        elif(g==num):
            c=c+1
            break
        else:
            print("Your guess is too hight.")
        c=c+1
    print("Good job, KBTU! You guessed my number in", c , "guesses!")
        
num = random.randint(1,20)
r(num)

#14
from function1 import (
    s,
    a,
    R,
    F,
    A,
    r,
    r,
    e,
    e,
    a,
    q,
    w,
    r  
)
count=int(input())
s(count)

