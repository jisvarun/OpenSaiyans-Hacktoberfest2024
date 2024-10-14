a="This is my city.This city is very beautiful city"
print("The string is found at index:",a.find("city"))
###Note if we will not specify the range then it will return the index of first occurence.


#####NOw using start and end parameter
str1="Monkies Love Banana.Banana is a fruit."
b=str1.find("Bana",5,19)
print("The string Bana is found at index:",b)


####If substring not found it will return -1
str2="Potato"
print(str2.find("k"))

##This method is case sensitive so it will return -1 with case mismatch
str3="Banana"
print(str3.find('b'))
