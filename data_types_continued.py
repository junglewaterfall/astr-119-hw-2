s = "i am a string"
print(type(s))
yes = True
print(type(yes))
no = False
print(type(no))

a_list = ["a", "b", "c"]
print(type(a_list))
print(type(a_list[0]))
a_list.append("d")
print(a_list)

a_tuple = ("a", "b", "c")
print(type(a_tuple))

try:
    a_tuple[2] = "d"
except TypeError:
    print("we can't add elements to tuples")
print(a_tuple)


