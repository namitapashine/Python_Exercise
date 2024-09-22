# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:12:33 2024

@author: namita
Password generator using array 
"""

import random
import string

class pwd_generator :
 def __init__(instance_of_class_obj,length_of_pwd):
       
       instance_of_class_obj.pwd_len = length_of_pwd
       instance_of_class_obj.Array_of_char= [list(string.ascii_uppercase),
                                             list(string.ascii_lowercase),
                                             list(string.digits),
                                             list(string.punctuation)]
       instance_of_class_obj.final_password =""  
       
 def generate_pwd(instance_of_class_obj):
     print(f"Here is your {instance_of_class_obj.pwd_len} digit password") 
      
     instance_of_class_obj.final_password += ''.join(random.choices( instance_of_class_obj.Array_of_char[0], k=1 ))
     instance_of_class_obj.final_password += ''.join(random.choices( instance_of_class_obj.Array_of_char[1], k= (instance_of_class_obj.pwd_len-3)))
     instance_of_class_obj.final_password += ''.join(random.choices( instance_of_class_obj.Array_of_char[2], k=1))
     instance_of_class_obj.final_password += ''.join(random.choices( instance_of_class_obj.Array_of_char[3], k=1))

     print(instance_of_class_obj.final_password)                
       



#Taking user input
response = input("Do you want to generate the password Yes/No - ")

if response.lower() == "yes" :
    length_of_pwd = int(input("Please enter the length of paswored You Desire, Minimun Length should be 4: "))
    if length_of_pwd < 4:
       print("Sorry!, length of The `Password can not be less then 4 character ")   
    else:
       #create the instance of a class object
       object1 =  pwd_generator(length_of_pwd)
       object1.generate_pwd()
elif response.lower()=="no" :
    print(" See you again ")
else :
    print("Please enter correct choice Yes/No ")    
    
