#Import the random module for generating random values
import random
#Importing time module
import time
password=[]
#Function for generating password
def random_password_generator():
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case="abcdefghijklmnopqrstuvwxyz"
    number="0123456789"
    special_case="!@#$%^&*()?._"
    length=int(input("Enter the Length of the password : "))
    a=upper_case+lower_case+number+special_case
    password="".join(random.sample(a,length))
#Printing the generated password
    print("Generated Password : ",password)
#Function call
random_password_generator()
    
               
