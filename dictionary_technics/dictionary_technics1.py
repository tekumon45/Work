# making a dictionary
d1 = {"name": "saurabh", "age": 18, "class": "12th"}

# Dictionary comprehension using zip
keys = ["name", "age", "class"]
values = ["saurabh", 18, "12th"]

d1 = {k: v for k, v in zip(keys, values)}
 
 # Merge multiple dictionaries into one
d1 = {"a":1, "b":3.14}
d2 = {"b":2.714, "c":None}
d3 = {"d":[]}

print(d1 | d2)
print(d2 | d1)
print(d1 | d2 | d3)
print({**d1, **d2, **d3})

# The update method performs an in-place operation (raises TypeError if keys overlap)
e = {}
# e.update(**d1, **d2)  # TypeError: dict.update() got multiple values for keyword argument 'b'

# By creating and merging a dictionary with initial values, the initial values and key order can be controlled
d_init = {"a": 1, "b": 2.5, "c": "python"}

d_input = {"b": 2.714, "c": None, "d": []}

d_merge = {**d_init, **d_input}
print(d_merge)  # {'a': 1, 'b': 2.714, 'c': None, 'd': []}

# Use the fromkeys class method if all keys share the same initial value
keys = ["a", "b", "c"]
print({}.fromkeys(keys)) # {'a': None, 'b': None, 'c': None}
print({}.fromkeys(keys, 0)) # {'a': 0, 'b': 0, 'c': 0}