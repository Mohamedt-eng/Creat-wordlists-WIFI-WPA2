
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

\u001b[33m"""

print ("\u001b[34m.==========================================" )
tx= """ \u001b[33m.
thes  script  is dedicated to INW
so that you shorten us the way to password very simple
step1: Enter digit or charactet  example :
0123456789 or abcd..x or ABCD..X or 123abcd
step2: Enter nember 7   is the max length of 
the script password will complete the gap number
do not worry
 \u001b[37m """

import io ,os
import  itertools
print (tx)
print ("\u001b[34m.===========================================")

gap=3
contint  = input("\u001b[32m Enter digits >\u001b[37m")
max = input("\u001b[32m Enter max pass >\u001b[37m" )

outresult = itertools.product(contint,repeat=int(max))
f = open("password-defaolt-inwi.txt","w")
print (" witing.......")
for i in outresult :
    pas = "".join(i)
    f. writelines(str(gap)+pas+"\n")
f.close()
print ("\u001b[34m is file list-pass.txt completed >\u001b[37m")


