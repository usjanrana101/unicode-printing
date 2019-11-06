# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:08:40 2019
 Unicode using list
@author: Jagannath
"""
s='mumbai'
uni=[]
for i in range(len(s)):
    uni.append(ord(s[i]))
print ('Unicode of letters in ',s, 'are respectively:')
print (uni)