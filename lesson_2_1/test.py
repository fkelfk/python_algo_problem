import os
import sys
import re


path = r'/Users/junghoonlee/Documents/data/2-1/2'
# list = os.listdir(path)
# file = open(path,'rt')
# lines = file.readlines(0)
# print(lines)
with open(path+"/"+"in2.txt", "r", encoding='utf-8') as f: 
    while True:
        line = f.readline()
        list = re.findall(r'\d+', line)
        list = [int(i) for i in list]
        if not line: break
        
        print(list)
