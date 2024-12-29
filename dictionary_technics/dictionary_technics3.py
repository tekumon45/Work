# remove duplicate from list
mylist = ["a", "b", "a", "c", "d"]
# mylist = list(dict.fromkeys(mylist))
# mylist = dict.fromkeys(mylist)
mylist = list(set(mylist))
print(mylist)