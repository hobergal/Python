#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:54:36 2020

@author: alyxandrahoberg
"""


# MAGIC 8-BALL HOMEWORK

import random

history = ["History:"]

def magiceightball(random_number):
   if random_number == 1:
       answer = "Yes!"
   if random_number == 2:
       answer = "No."
   if random_number == 3:
       answer = "Maybe."
   if random_number == 4:
       answer = "Possibly."
   if random_number == 5: 
       answer = "You may rely on it."
   if random_number == 6: 
       answer = "Try Again."
       print(answer)  
 

# 8 ball 
print("Welcome to the Magic 8 Ball!")
print("Press H to see History, Press E to Exit, Press Enter to Ask Again")

while True: 
    print("What is your Question?")
    question = input()
    answer = random.randint(1,6)
    prediction = magiceightball(answer) 
    decision = input()
    history.append(question + " " + answer)
    if decision == "E":
        break
    if decision == "H":
        print(history)
        input("Press ENTER to Ask Again")
else:
    input()
    
    
    
    
    
    
    




