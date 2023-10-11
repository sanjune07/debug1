#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# In[6]:


# Main program
print("Prime Number Finder")


# In[8]:


# Get user input
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


# In[9]:


# Swap start and end if start is greater
if start > end:
    temp = start
    start = end
    end = temp


# In[10]:


# Find and print prime numbers
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")

