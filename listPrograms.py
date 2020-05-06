## Adding data into list dynamically
'''names = [] # empty list
N = int(input('Enter no of names to be added: '))
for var in range(N):
    name = input('Enter name: ')
    names.append(name)
print(names)'''# multi line comments

# find the nth largest value from given list
'''li = [33,8,77,9,34,2328,23]
n = int(input('Enter n value: '))
li.sort(reverse = True) # descending order
print(li)
print(li[n-1])'''

# sort without using function
'''li = [33,8,77,9,34,2328,23]
for var1 in range(len(li)):
    for var2 in range(var1+1,len(li)):
        if(li[var1]>li[var2]+1):
            temp = li[var1]
            li[var1] = li[var2]
            li[var2] = temp
print(li)'''

# find frequency of each number in range(1,9) in given input list
'''numbers = [1,5,3,1,3,5,8,3,5,9,3,8,9,1,6,7]
# 1 : 3
# 2 : 0
# 3 : 4
for var in range(1,10):
    print(var,':',numbers.count(var))'''

# Find sum of elements in the given 2 lists based on index
'''li1 = [1,2,3,4,5]
li2 = [4,5,6,7,8]
if(len(li1) == len(li2)):
    for var in range(len(li1)):
        li1[var] += li2[var]

print(li1)'''


# Program for finding kth largest frequency element from given list
# if any of the two elements having same frequency u can print any one
li3  = ['a','b','a','c','d','e','b','a']
k = int(input('Enter number: '))
unique = []# empty list
for var in li3:
        if var not in unique:
            unique.append(var)
print(unique)
freq = []
for var1 in unique:
    freq.append(li3.count(var1))
print(freq)
print(unique[k-1])


# find the largest frequency element from given list

