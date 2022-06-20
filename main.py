number=[1,2,3]

# formula: new_list=[new_item for item in list]
new_list=[n+1 for n in number]
print(new_list)

name= "Sharath"

name_list= [val for val in name]
print(name_list)

number_list=[n*2 for n in range(1,5)]
print(number_list)

# formula: new_list=[new_item for item in list if test]
names=["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_name=[val for val in names if len(val)<5]
print(short_name)

uppercase_name=[val.upper() for val in names if len(val)>5 ]
print(uppercase_name)