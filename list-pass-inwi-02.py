#!/usr/bin/python
""" This p
script was written 11/05/2020 by Muhammad Tayaq.
 This script is for a social engineering-based exam, 
and it is available to everyone, 
taking into account intellectual property rights.  
Contact: Mohamedtayaq91@gmail.com"""
name =  u"""\u001b[36m
######################################################
_____ _           _                        _        
|  ___| |         | |                     | |       
| |__ | | ___  ___| |_ _ __ ___  _ __     | |_ __ _ 
|  __|| |/ _ \/ __| __| '__/ _ \| '_ \    | __/ _` |
| |___| |  __/ (__| |_| | | (_) | | | |   | || (_| |
\____/|_|\___|\___|\__|_|  \___/|_| |_|    \__\__, |
                                                 | |
                                                 |_|
\u001b[33mCreate a professional and advanced personal 
password list targeting specific victims"   \u001b[37m 
\u001b[37m"""
print (name)
listsymbol1 = ['@','}','?','$','.','/',' ','#','@','%','~','.','=','(',')','|',']','[','$','_','-','¦','{','}']
listsymbol3 = ['$','{','*','#','?','~',']',' ','/','%','!','.','+','=','(',')','[',']','&','_',' ','-','?','{','}','@']
listsymbol2 = ['/''{','#','!','-','+','[','=',' ','%','*',']','^','_','(','/',')','$','@','?','!','~','|','&','>','<']


encrement_number = 0


wlist = input(u"\u001b[32m Enter wordlist : >\u001b[37m ")
wordlist  = open(wlist,'r')
paswds = open("Passwords.txt",'w')
print (u"\u001b[36m wihting.....\u001b[37m")

for i in wordlist.readlines(): #for loop encrement words as file
     i = i.rstrip("\n")
     paswds.write(i)
     #encement_symbol +=1
     for x in listsymbol1:
          #encrement_number +=1
          for y in listsymbol2 : #for loop encrement character as array
               for g in listsymbol3:
                   encrement_number = encrement_number +1
                   paswds.write(i+str(encrement_number)+"\n")
                   paswds.write(i+str(encrement_number)+str(encrement_number)+"\n")
                   paswds.write(str(encrement_number)+i+"\n")
                   paswds.write(i+str(encrement_number)+i+"\n")
                   paswds.write(str(encrement_number)+x+y+"\n")
                   paswds.write(i+str(encrement_number)*2+"\n")
                   paswds.write(i+y+x+g+"\n")
                   paswds.write(x*2+i+x*2+"\n")
                   paswds.write(str(encrement_number)+i+str(encrement_number)+"\n")
                   paswds.write(i+g+x+y+"\n")
                   paswds.write(i+g*4+x*4+"\n")
                   paswds.write(i+y*4+x*2+"\n")
                   paswds.write(g*2+x*2+y*2+i+"\n")
                   paswds.write(i+x*2+y*2+"\n")
                   paswds.write(str(encrement_number)*2+i+x+y+g+"\n")
                   paswds.write(x*4+i+str(encrement_number)+"\n")
                   paswds.write(i+str(encrement_number)+x*4+"\n")
                   if i == i.lower():
                       i = i.upper() #change lower str to upper str
                       paswds.write(i+str(encrement_number)+"\n")
                       paswds.write(str(encrement_number)+i+"\n")
                       paswds.write(i+str(encrement_number)+i+"\n")
                       paswds.write(str(encrement_number)+x+y+"\n")
                       paswds.write(i+str(encrement_number)*2+"\n")
                       paswds.write(i+y+x+g+"\n")
                       paswds.write(x*2+i+x*2+"\n")
                       paswds.write(str(encrement_number)+i+str(encrement_number)+"\n")
                       paswds.write(i+g+x+y+"\n")
                       paswds.write(i+g*4+x*4+"\n")
                       paswds.write(i+y*4+x*2+"\n")
                       paswds.write(g*2+x*2+y*2+i+"\n")
                       paswds.write(i+x*2+y*2+"\n")
                       paswds.write(str(encrement_number)*2+i+x+y+g+"\n")
                       paswds.write(x*4+i+str(encrement_number)+"\n")
                       paswds.write(i+str(encrement_number)+x*4+"\n")
                   i = i.lower() or upper()#change upper str to lower str
          if encrement_number >= 9999:
                  break
     
     encrement_number=0
print (u"\u001b[32m List Completed /Passwords.txt \u001b[37m")         
paswds.close()    
           
                        
      
