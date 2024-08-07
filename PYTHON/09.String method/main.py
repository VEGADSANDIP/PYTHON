# upper = all letter are upper cse
name = "sandip"
print(name.upper())

# lower = all letter are lower cse
name = "SANDIP"
print(name.lower())

# strip = remove white spaces before and after the string
name =  "  sadnip  "
print(name.strip())

# rstrip = remove trailing characters name
name = "!! sandip !!!!!!!!!"
print(name.rstrip("!"))

# replace = replace all occurence of a string with another string
name = "sandip"
print(name.replace("sandip","sandy"))

# ''' split = split the given string at the specified instance and returns the separated strings as list items '''
name =" sandip vegad"
print(name.split())

# capitalize = turn only the first character of the string to uppercase and the rest other characters of the
name = "sandip vegad"
print(name.capitalize())

# center = align the string to the center as per the parameters given by the user
name = "sandip"
print(name.center(60))
print(name.center(60,"-"))

# count = returns the number of times the given value has occurred within the given string
name = "sandip vegad"
print(name.count("a"))
 
# endswith = check if the string ends with a given value. if yes then return True, else return
name = " sandip vegad"
print(name.endswith("ad"))

# find - serch the occurtion and fina is tthe index of the first occurtion of the given value and return the index where it is present. if given value is ab
name = "sandip vegad"
print(name.find("n"))
print(name.find("1")) # answer is -1

# index = serch the occurtion and fina is tthe index of the first occurtion of the given value and return the
name = "sandip vegad"
print(name.index("d"))
# print(name.index("1")) # can you display on error

# isalnum =  A-Z, a-z, 0-9.
name = "sandipvegad"
print(name.isalnum())

# isalpha = A-Z, a-z.
name = "sandipvegad0"
print(name.isalpha())

# islower = all letter are lower cse,,, yes or no
name = "sandip"
print(name.islower())

# isprinttable = all letter are printable
name = "sandip\n"
print(name.isprintable()) #\n i not printed word

# istittle = all first letter of the word is capital
str1 = "World Health Organization" 
print(str1.istitle()) #there is all frist letter are capital
str2 = "To kill a Mocking bird"
print(str2.istitle()) #there is all frist letter not capital

# isupper- true or false
name = "SANDIP "
print(name.isupper())

# swapcase- upper to lowr and lower to upper
name = "vegad SANDIP"
print(name.swapcase())

# title - frist letter capital another are small
name = " The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case."
print(name.title())