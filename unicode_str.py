# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:45:40 2019
 Letters in string and its Unicode
@author: Jagannath
"""
s='mumbai'
for i in range(len(s)):
    print (s[i] ,'..unicode..>',ord(s[i]))
sum=0
for i in range(len(s)):
    sum=sum+ord(s[i])
print ('Sum of these unicode numbers is',sum)