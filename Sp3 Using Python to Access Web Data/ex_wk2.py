# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re

data = open('regex_sum_555756.txt')
numlist = list()

for line in data:
    n = re.findall('[0-9]+', line)
    numlist = numlist + n
# numlist.append(n) will be nest list so not work. Should use numlist.extend(n)

sum = 0
for x in numlist:
    sum = sum + int(x)
print(sum)

'''
# Python 3:

import re
print(sum([int(i) for i in re.findall('[0-9]+', open('regex_sum_555756.txt').read())]))
'''