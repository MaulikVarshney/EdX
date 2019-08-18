my_str=input("Input your full name")
my_str=str(my_str)
space=my_str.find(' ')
print(f"Hello {my_str[:space+2]}.")
