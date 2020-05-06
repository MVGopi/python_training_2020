Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 09:44:33) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = ['abc',23,8.7,9.5]
>>> list1
['abc', 23, 8.7, 9.5]
>>> list1.append(24)
>>> list1
['abc', 23, 8.7, 9.5, 24]
>>> list1.append([56,'def'])
>>> list1
['abc', 23, 8.7, 9.5, 24, [56, 'def']]
>>> list1.extend([1,2,3,4,5,6])
>>> list1
['abc', 23, 8.7, 9.5, 24, [56, 'def'], 1, 2, 3, 4, 5, 6]
>>> list1.insert(2, 'python')#listname.insert(index, element)
>>> list1
['abc', 23, 'python', 8.7, 9.5, 24, [56, 'def'], 1, 2, 3, 4, 5, 6]
>>> # update list
>>> list2 = ['venkat','pavan','ankita','haniha']
>>> list2
['venkat', 'pavan', 'ankita', 'haniha']
>>> list2 = ['venkat','pavan','ankita','hanisha']
>>> list2
['venkat', 'pavan', 'ankita', 'hanisha']
>>> list2[1] = 'pavan kumar'
>>> list2
['venkat', 'pavan kumar', 'ankita', 'hanisha']
>>> # delete list
>>> del list2[3]
>>> list2
['venkat', 'pavan kumar', 'ankita']
>>> list2.remove('venkat')
>>> list2
['pavan kumar', 'ankita']
>>> list2.pop(1)
'ankita'
>>> list2
['pavan kumar']
>>> list2.clear()#makes list empty
>>> list2
[]
>>> del list2
>>> list2
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list2
NameError: name 'list2' is not defined
>>> dir(list)#inbuilt function which returns list of functions of given data type
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> li1 = [1,2,3,4,5]
>>> li2 = li1
>>> li2
[1, 2, 3, 4, 5]
>>> li1
[1, 2, 3, 4, 5]
>>> li1.remove(5)
>>> li1
[1, 2, 3, 4]
>>> li2
[1, 2, 3, 4]
>>> li1
[1, 2, 3, 4]
>>> li3.copy(li1)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    li3.copy(li1)
NameError: name 'li3' is not defined
>>> li1
[1, 2, 3, 4]
>>> li2
[1, 2, 3, 4]
>>> li1.copy(li2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    li1.copy(li2)
TypeError: copy() takes no arguments (1 given)
>>> li2
[1, 2, 3, 4]
>>> li3 = li2.copy()# newList = oldList.copy()
>>> li3
[1, 2, 3, 4]
>>> li2
[1, 2, 3, 4]
>>> li2.remove(3)
>>> li2
[1, 2, 4]
>>> li3
[1, 2, 3, 4]
>>> li = ['a', 'b', 'c', 'a']
>>> li
['a', 'b', 'c', 'a']
>>> li.count('a') # returns frequency of given element
2
>>> li
['a', 'b', 'c', 'a']
>>> li.index('b')
1
>>> li.index('c')
2
>>> li
['a', 'b', 'c', 'a']
>>> li.reverse()
>>> li
['a', 'c', 'b', 'a']
>>> li
['a', 'c', 'b', 'a']
>>> li.sort()# default in ascending
>>> li
['a', 'a', 'b', 'c']
>>> li.sort(reverse = True)# default in ascending
>>> li
['c', 'b', 'a', 'a']
>>> 