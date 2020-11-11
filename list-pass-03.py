
#!/usr/bin/python
# coding=<encoding name>
""" This p
script was written 11/05/2020 by Muhammad Tayaq.
 This script is for a social engineering-based exam,
and it is available to everyone,
taking into account intellectual property rights.
Contact: Mohamedtayaq91@gmail.com"""
name =  u"""\u001b[36m
######################################################

                                                     
      (               )                      )       
 (    )\   (       ( /( (                 ( /(   (   
 )\  ((_) ))\  (   )\()))(    (    (      )\())( )\  
((_)  _  /((_) )\ (_))/(()\   )\   )\ )  (_))/ )(( ) 
| __|| |(_))  ((_)| |_  ((_) ((_) _(_/(  | |_ ((_)_) 
| _| | |/ -_)/ _| |  _|| '_|/ _ \| ' \)) |  _|/ _` | 
|___||_|\___|\__|  \__||_|  \___/|_||_|   \__|\__, | 
                                                 |_| 

\u001b[33m
    Create a professional and advanced personal
    password list targeting specific victims"   \u001b[37m
\u001b[37m"""
print (name)
commet=u"""\u001b[33m 
    creat wordlist perssonel 
    Example:
    python3 wordlist.py > /root/Desktop/dodo.txt
    Entere 5 information de target
    size  wordlist 5 MG byte
    Double size Example:
    python3 wordlist.py >> /root/Desktop/dodo.txt
"""
print (commet +"\033[0m")

import os, sys
ze = input(u"\u001b[36m enter name :>" +"\033[0m")
zo = input(u"\u001b[36m enter nechname :>"+"\033[0m")
zi = input(u"\u001b[36m enter nme  :>"+"\033[0m")
zu = input(u"\u001b[36m enter child :>"+"\033[0m")
za = input(u"\u001b[36m enter ? :>"+"\033[0m")

def wordls():
    a = ["p","h","g","s","q"]
    a[0]= ze
    a[1]= zo
    a[2]= zi
    a[3]= zu
    a[4]= za
    s = ['*','%','$','&','@','§','?','!','-','_','+','/','(',')','[',']','}','{','=','|','.','^']
    b = 0
    tk = 0
    for i in a :
        for x in s:
            b = b + 1
            print(a[0] + x)
            print(a[1] + x)
            print(a[2] + x)
            print(a[3] + x)
            print(a[4] + x)
            print(a[0] + x + s[1])
            print(a[1] + x + s[2])
            print(a[2] + x + s[3])
            print(a[3] + x + s[4])
            print(a[4] + x + s[5])
            print(a[0] + x + s[6])
            print(a[1] + x + s[7])
            print(a[2] + x + s[8])
            print(a[3] + x + s[9])
            print(a[4] + x + s[10])
            print(a[4] + x)
            print(a[0] + x + s[1]+s[10])
            print(a[1] + x + s[2]+s[9])
            print(a[2] + x + s[3]+s[8])
            print(a[3] + x + s[4]+s[7])
            print(a[4] + x + s[5]+s[6])
            print(a[0] + x + s[6]+s[5])
            print(a[1] + x + s[7]+s[4])
            print(a[2] + x + s[8]+s[3])
            print(a[3] + x + s[9]+s[2])
            print(a[4] + x + s[10]+s[1])
         
            print(a[0] + x + s[1]+s[10]+x)
            print(a[1] + x + s[2]+s[9]+x)
            print(a[2] + x + s[3]+s[8]+x)
            print(a[3] + x + s[4]+s[7]+x)
            print(a[4] + x + s[5]+s[6]+x)
            print(a[0] + x + s[6]+s[5]+x)
            print(a[1] + x + s[7]+s[4]+x)
            print(a[2] + x + s[8]+s[3]+x)
            print(a[3] + x + s[9]+s[2]+x)
            print(a[4] + x + s[10]+s[1]+x)
          
               
            print(a[1] + str(b)+s[0])
            print(a[1] + str(b)+s[1])
            print(a[1] + str(b)+s[2])
            print(a[1] + str(b)+s[3])
            print(a[1] + str(b)+s[4])
            print(a[1] + str(b)+s[5])
            print(a[1] + str(b)+s[6])
            print(a[1] + str(b)+s[7])
            print(a[1] + str(b)+s[8])
            print(a[1] + str(b)+s[9])
            print(a[1] + str(b)+s[10])
                  

            print(a[2] + str(b)+s[0])
            print(a[2] + str(b)+s[1])
            print(a[2] + str(b)+s[2])
            print(a[2] + str(b)+s[3])
            print(a[2] + str(b)+s[4])
            print(a[2] + str(b)+s[5])
            print(a[2] + str(b)+s[6])
            print(a[2] + str(b)+s[7])
            print(a[2] + str(b)+s[8])
            print(a[2] + str(b)+s[9])
            print(a[2] + str(b)+s[10])
                 
            print(a[3] + str(b)+s[0])
            print(a[3] + str(b)+s[1])
            print(a[3] + str(b)+s[2])
            print(a[3] + str(b)+s[3])
            print(a[3] + str(b)+s[4])
            print(a[3] + str(b)+s[5])
            print(a[3] + str(b)+s[6])
            print(a[3] + str(b)+s[7])
            print(a[3] + str(b)+s[8])
            print(a[3] + str(b)+s[9])
            print(a[3] + str(b)+s[10])


            print(a[4] + str(b)+s[0])
            print(a[4] + str(b)+s[1])
            print(a[4] + str(b)+s[2])
            print(a[4] + str(b)+s[3])
            print(a[4] + str(b)+s[4])
            print(a[4] + str(b)+s[5])
            print(a[4] + str(b)+s[6])
            print(a[4] + str(b)+s[7])
            print(a[4] + str(b)+s[8])
            print(a[4] + str(b)+s[9])
            print(a[4] + str(b)+s[10])
            while b < 12345 :
                b = b +1
                print(a[0] + str(b))
                print(a[1] + str(b))
                print(a[2] + str(b))
                print(a[3] + str(b))
                print(a[4] + str(b))

                while tk < 12345 :
                    tk = tk +1
                    print(str(tk) + a[0])
                    print(str(tk) + a[1])
                    print(str(tk) + a[2])
                    print(str(tk) + a[3])
                    print(str(tk) + a[4])

    a[0]= ze.upper()
    a[1]= zo.upper()
    a[2]= zi.upper()
    a[3]= zu.upper()
    a[4]= za.upper()
    s = ['*','%','$','&','@','§','?','!','-','_','+','/','(',')','[',']','}','{','=','|','.','^']
    b = 0

    for i in a :
        for x in s:
            b = b + 1
            print(a[0] + x)
            print(a[1] + x)
            print(a[2] + x)
            print(a[3] + x)
            print(a[4] + x)
            print(a[0] + x + s[1])
            print(a[1] + x + s[2])
            print(a[2] + x + s[3])
            print(a[3] + x + s[4])
            print(a[4] + x + s[5])
            print(a[0] + x + s[6])
            print(a[1] + x + s[7])
            print(a[2] + x + s[8])
            print(a[3] + x + s[9])
            print(a[4] + x + s[10])
            print(a[4] + x)
            print(a[0] + x + s[1]+s[10])
            print(a[1] + x + s[2]+s[9])
            print(a[2] + x + s[3]+s[8])
            print(a[3] + x + s[4]+s[7])
            print(a[4] + x + s[5]+s[6])
            print(a[0] + x + s[6]+s[5])
            print(a[1] + x + s[7]+s[4])
            print(a[2] + x + s[8]+s[3])
            print(a[3] + x + s[9]+s[2])
            print(a[4] + x + s[10]+s[1])
         
            print(a[0] + x + s[1]+s[10]+x)
            print(a[1] + x + s[2]+s[9]+x)
            print(a[2] + x + s[3]+s[8]+x)
            print(a[3] + x + s[4]+s[7]+x)
            print(a[4] + x + s[5]+s[6]+x)
            print(a[0] + x + s[6]+s[5]+x)
            print(a[1] + x + s[7]+s[4]+x)
            print(a[2] + x + s[8]+s[3]+x)
            print(a[3] + x + s[9]+s[2]+x)
            print(a[4] + x + s[10]+s[1]+x)
          
               
            print(a[1] + str(b)+s[0])
            print(a[1] + str(b)+s[1])
            print(a[1] + str(b)+s[2])
            print(a[1] + str(b)+s[3])
            print(a[1] + str(b)+s[4])
            print(a[1] + str(b)+s[5])
            print(a[1] + str(b)+s[6])
            print(a[1] + str(b)+s[7])
            print(a[1] + str(b)+s[8])
            print(a[1] + str(b)+s[9])
            print(a[1] + str(b)+s[10])
                  

            print(a[2] + str(b)+s[0])
            print(a[2] + str(b)+s[1])
            print(a[2] + str(b)+s[2])
            print(a[2] + str(b)+s[3])
            print(a[2] + str(b)+s[4])
            print(a[2] + str(b)+s[5])
            print(a[2] + str(b)+s[6])
            print(a[2] + str(b)+s[7])
            print(a[2] + str(b)+s[8])
            print(a[2] + str(b)+s[9])
            print(a[2] + str(b)+s[10])
                 
            print(a[3] + str(b)+s[0])
            print(a[3] + str(b)+s[1])
            print(a[3] + str(b)+s[2])
            print(a[3] + str(b)+s[3])
            print(a[3] + str(b)+s[4])
            print(a[3] + str(b)+s[5])
            print(a[3] + str(b)+s[6])
            print(a[3] + str(b)+s[7])
            print(a[3] + str(b)+s[8])
            print(a[3] + str(b)+s[9])
            print(a[3] + str(b)+s[10])


            print(a[4] + str(b)+s[0])
            print(a[4] + str(b)+s[1])
            print(a[4] + str(b)+s[2])
            print(a[4] + str(b)+s[3])
            print(a[4] + str(b)+s[4])
            print(a[4] + str(b)+s[5])
            print(a[4] + str(b)+s[6])
            print(a[4] + str(b)+s[7])
            print(a[4] + str(b)+s[8])
            print(a[4] + str(b)+s[9])
            print(a[4] + str(b)+s[10])
            while b < 12345 :
                b = b +1
                print(a[0] + str(b))
                print(a[1] + str(b))
                print(a[2] + str(b))
                print(a[3] + str(b))
                print(a[4] + str(b))   

    bb = 0 
    ss = 0
    t = ['*','%','$','&','@','§','?','!','-','_','+','/','(',')','[',']','}','{','=','|','.','^']

    for i in t :


        print(a[0]+ str(i))
        print(a[0]+ str(i*2))
        print(a[0]+ str(i*3))
        print(a[0]+ str(i*4))
        print(a[0]+ str(i*5))
        print(a[0]+ str(i*6))
        print(a[0]+ str(i*7))
        print(a[0]+ str(i*8))
        print(a[0]+ str(i*9))
        print(a[0]+ str(i*10))
        print(a[1]+ str(i))
        print(a[1]+ str(i*2))
        print(a[1]+ str(i*3))
        print(a[1]+ str(i*4))
        print(a[1]+ str(i*5))
        print(a[1]+ str(i*6))
        print(a[1]+ str(i*7))
        print(a[1]+ str(i*8))
        print(a[1]+ str(i*9))
        print(a[1]+ str(i*10))
        print(a[2]+ str(i))
        print(a[2]+ str(i*2))
        print(a[2]+ str(i*3))
        print(a[2]+ str(i*4))
        print(a[2]+ str(i*5))
        print(a[2]+ str(i*6))
        print(a[2]+ str(i*7))
        print(a[2]+ str(i*8))
        print(a[2]+ str(i*9))
        print(a[2]+ str(i*10))
        print(a[3]+ str(i))
        print(a[3]+ str(i*2))
        print(a[3]+ str(i*3))
        print(a[3]+ str(i*4))
        print(a[3]+ str(i*5))
        print(a[3]+ str(i*6))
        print(a[3]+ str(i*7))
        print(a[3]+ str(i*8))
        print(a[3]+ str(i*9))
        print(a[3]+ str(i*10))
        print(a[4]+ str(i))
        print(a[4]+ str(i*2))
        print(a[4]+ str(i*3))
        print(a[4]+ str(i*4))
        print(a[4]+ str(i*5))
        print(a[4]+ str(i*6))
        print(a[4]+ str(i*7))
        print(a[4]+ str(i*8))
        print(a[4]+ str(i*9))
        print(a[4]+ str(i*10))

        while ss < 12345 :
            ss = ss +1
            print(a[0] + str(ss))
            print(a[1] + str(ss))
            print(a[2] + str(ss))
            print(a[3] + str(ss))
            print(a[4] + str(ss))
            while bb < 12345 :
                bb = bb +1
                print(str(bb) + a[0])
                print(str(bb) + a[1])
                print(str(bb) + a[2])
                print(str(bb) + a[3])
                print(str(bb) + a[4])

    ta = ['*','%','$','&','@','§','?','!','-','_','+','/','(',')','[',']','}','{','=','|','.','^']
    a[0]= ze
    a[1]= zo
    a[2]= zi
    a[3]= zu
    a[4]= za
    junx = 0
    junc = 0
    for i in ta :


        print(a[0]+ str(i))
        print(a[0]+ str(i*2))
        print(a[0]+ str(i*3))
        print(a[0]+ str(i*4))
        print(a[0]+ str(i*5))
        print(a[0]+ str(i*6))
        print(a[0]+ str(i*7))
        print(a[0]+ str(i*8))
        print(a[0]+ str(i*9))
        print(a[0]+ str(i*10))
        print(a[1]+ str(i))
        print(a[1]+ str(i*2))
        print(a[1]+ str(i*3))
        print(a[1]+ str(i*4))
        print(a[1]+ str(i*5))
        print(a[1]+ str(i*6))
        print(a[1]+ str(i*7))
        print(a[1]+ str(i*8))
        print(a[1]+ str(i*9))
        print(a[1]+ str(i*10))
        print(a[2]+ str(i))
        print(a[2]+ str(i*2))
        print(a[2]+ str(i*3))
        print(a[2]+ str(i*4))
        print(a[2]+ str(i*5))
        print(a[2]+ str(i*6))
        print(a[2]+ str(i*7))
        print(a[2]+ str(i*8))
        print(a[2]+ str(i*9))
        print(a[2]+ str(i*10))
        print(a[3]+ str(i))
        print(a[3]+ str(i*2))
        print(a[3]+ str(i*3))
        print(a[3]+ str(i*4))
        print(a[3]+ str(i*5))
        print(a[3]+ str(i*6))
        print(a[3]+ str(i*7))
        print(a[3]+ str(i*8))
        print(a[3]+ str(i*9))
        print(a[3]+ str(i*10))
        print(a[4]+ str(i))
        print(a[4]+ str(i*2))
        print(a[4]+ str(i*3))
        print(a[4]+ str(i*4))
        print(a[4]+ str(i*5))
        print(a[4]+ str(i*6))
        print(a[4]+ str(i*7))
        print(a[4]+ str(i*8))
        print(a[4]+ str(i*9))
        print(a[4]+ str(i*10))


        while junx < 12345 :
            junx = junx +1
            print(a[0] + str(junx))
            print(a[1] + str(junx))
            print(a[2] + str(junx))
            print(a[3] + str(junx))
            print(a[4] + str(junx))
            while junc < 12345 :
                junc = junc +1
                print(str(junc) + a[0])
                print(str(junc) + a[1])
                print(str(junc) + a[2])
                print(str(junc) + a[3])
                print(str(junc) + a[4])

wordls()
