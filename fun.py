from django.test import TestCase


name = 'Test'
city = 'Kathmandu'
number = 9813966699
Country = 'Nepal'
for i in range(1,1000):
    dj = name+f"{i}"+','+city+','+f'{number}'+','+Country
    print(dj)