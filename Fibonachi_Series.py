# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:58:24 2024

@author: namita
Fibonachi series
"""
number=int(input("Please enter the number : "))

def fun_fibonachi(number):

    for i in range(number+1):
        if i == 0 or i==1:
            print(i,end="")
            old_num1 = 0 
            old_num2 = 1      
        else : 
            new_num = old_num1 + old_num2
            print(new_num,end="")
            old_num1 = old_num2
            old_num2 = new_num   
            
fun_fibonachi(number)        