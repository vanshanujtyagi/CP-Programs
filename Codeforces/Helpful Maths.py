summ=input() #summ takes string input eg. 8+4+9+1
values=summ.split("+") #.split("+") splits the string elements separated by + into a list of string elements.
values.sort() #sorts the list in default ascending order
print("+".join(values)) #.join() is kinda opposite to split(). It works on list of strings.
#General syntax : "separator".join(list/tuple)
