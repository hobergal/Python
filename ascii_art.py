#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:04:12 2020

@author: alyxandrahoberg
"""

import random 

from art import * 

def spyderart(random_number):
   if random_number == 1:
       tprint("aly", "alpha")
   if random_number == 2:
       aprint("hug me")
   if random_number == 3:
       aprint("umadbro")
   if random_number == 4:
       aprint("inlove")
   if random_number == 5: 
       aprint("stars2")
   if random_number == 6: 
       aprint("love2")
   if random_number == 7:
       aprint("happy birthday 1")
   if random_number == 8:
       aprint("playing cards")
   if random_number == 9:
       aprint("american money 5")
       
print("SPYDER ART FUN \n") 
previous_num = 100

while True: #infinite loop 
    input("Press Enter for Art Fun!")
    random_num = random.randint(1, 9)
    if random_num == previous_num:
        print("Repeated # Fixed")
        random_num = random.randint(1, 9) 
    spyderart(random_num)
    previous_num = random_num 
    print(previous_num)
    