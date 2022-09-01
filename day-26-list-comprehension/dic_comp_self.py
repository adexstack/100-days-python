import random

names = ["Dan", "Steve", "Grant", "Heyne"]

names_scores_dic = {name: random.randint(1,10) for name in names}
print(names_scores_dic)

excellent_dic = {name : grade for (name, grade) in names_scores_dic.items() if grade > 5}
print(excellent_dic)

letters = "adewole"
print(list(letters))
let_dic = []
for letter in letters[::-1]:
    let_dic.append(letter)
print(''.join(let_dic))

empty_dic = {}
empty_dic["name"] = "Steve"
empty_dic["age"] = 20
print(empty_dic.items())

tuple = (2,4,6,1,7,2)
set_a = set(tuple)
print(set_a)
listb = ["a", "b", "c"]
new_set = set_a.union(listb)
print(new_set)

# Can not reassign string and tuple as they are immutable
t= "Tutorialspoint"
print(type(t))
print(t[0])
#t[0] = "M"  TypeError: 'str' object does not support item assignment

k_list = ["d", "n", "f"]
k_list[0] = "h"
print(k_list)

k_tuple = ("d", "n", "f")
#k_tuple[0] = "h" TypeError: 'tuple' object does not support item assignment

