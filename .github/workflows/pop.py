//removing using pop()
letter=['a','d','g']
print(letter)
['a','d','g']
letter.pop()
g
print(letter)//to check what are there in  that variable
['a','d']
poppped_element=letter.pop()
print(letter)
['a']
type(poped_element)
str
//removing a list at any point of time from the list(not to use this element again)
letter=['a','d','g']
print(letter)
['a','d','g']

letter.pop(1)
'd'
print(letter)
['a','g']
//removing iteam by value
letter=['a','d','g']
print(letter)
['a','d','g']
letter.remove('d')
print(letter)
['a','g']
//remove by iteam by its value
remove_variable='b'
letter.remove(remove_variable)
print(letter)
['a','g']
letter=['a','d','d','f']
print(letter)
['a','d','d','f']
//removes only the first occurence of that which u specify
letter.remove('d')
print(letter)
['a,'d','g']




