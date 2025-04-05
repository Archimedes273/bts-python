# List
# Tuple
# Dictionaries
# Sets


#list
# fruits = ["apple" , "orange" , "cherry"]
# print(fruits[0])
# fruits.append("grapes")
# print(fruits)
# fruits.remove("orange")
# print(fruits)

# fruit_list = ["apple" , "banana" , "cherry", "date"]
# print(fruit_list)

# dict_new = {"class":"A" ,"class":"B","class":"c","age":32 }
# print(dict_new)
# dict_new.pop("age")
# print(dict_new)
# dict_new["email"] = "dineshvignesh179@gmail.com"
# print(dict_new)
# # del - predifine function to delet in dictonaires
# del dict_new["class"]
# print(dict_new)


#set
new_set = {1,2,3,4,5,1,2,4,5,6,7,7}
print(type(new_set))
print(new_set)
# print(new_set[1]) -- error(immutable)
new_set.add(8)
print(new_set)
second_set = {2,4,5,6,7,9,10,11}
new_set.update(second_set)  # --to update two set
print(new_set)

print(new_set.union(second_set))
print(new_set.intersection(second_set))

# ABC= list(new_set)
# print(ABC)
# ABC.append(8)
# print(ABC)
