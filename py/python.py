#strings
#using format()
num=35;
name= 'sam'
print('given num is {one} and name is {two}'.format(one=num,two=name))

my_name="ragini"
print(my_name)
#slicing 
print(my_name[-1])
print(my_name[-2])
#using this notation, prints the string entirely
print(my_name[0:])

#using backward way slicing
#puts everything excluding last specified index
print(my_name[:3])
#rag-> ini
# print(my_name[-3])
lang= "Py"
distribution="anaconda"
version=3.13
env="venv"
#strings formatting
print(f"lang is {lang} with distribution {distribution} and version {version} and env is  {env}")

course="cybersecurity"
#exclude first and last substrings
print(course[5:13])

#lists
#muteable, heterogenous 
list= ["array", 5.678, 775, 'true']
print(list)
#output:array
print(list[0])
print(list[1:3])
print(list[1:4])
#appending the list
list[0]= "anaconda env"
print(f"updated list{list}")
list.append("ragini")
print(list)

#nesting
nest= ["fur"], ["dug"],[ "mug"], ["rug"],[5.678,86.46,788], ['true', 'false']
print(f"nested list {nest}")
print(nest [3][0])
print(nest[4])
print(nest[5])

#dictionaries: key value pairs
dict= {
    "username": "amy",
    "age":28,
    "password": "*******"
}
print(dict["age"])
# print(dict['username:' "ram"])

dict= {"password": {'innerKey': ['#####**&**@###']}}
# print(dict['password']['innerKey'][1])
print(dict['password']['innerKey'])
print(dict['password']['innerKey'][0])

#adding new key
dict["city"]= "del"
print(f"updated dict {dict}")

#updating the dictionary
dict["age"]= 32

#none
print(dict.get("username"))
print(dict.keys())
print(dict.values())
#key value pairs
print(dict.items())

for key,value in dict.items():
    print(key, ":", value)

#nested dict
user= {
    "first_name": "ava",
    "last_name" : "ava",
    "account": {
        "email": "avacado@gmail.com",
        "contact": 777898654387
    }
}
print(user.items())
print(user["last_name"])
print(user["account"]["contact"])

#dict with lists
data= {
    "fruits": {
     "name" : ["mango", "guava", "pineapple", "grapes"],
    "cost":  [55,55,80,55]
    }
    
}
print(data["fruits"]["cost"][1])
print(type(data["fruits"]["cost"][1]))
print(data["fruits"])

#lists are muteable 
#tuples are ordered, immuteable , once assigned can not be changed further
tuples= (10,20,40,50,60,70)
# print(tuples[0]="11")
#tuples can`t be reassigned 
print(tuples[0])
#neg indexing
#70
print(tuples[-1])
user_data= ["radheshyam",45,45,True,80000]
#80000
print(user_data[-1])

#to create tuple of one ele -> use , comma always
ISP= ("Jio")
#class-> string not tuples
print(type(ISP))

ISP= ("JIO",)
print(type(ISP))

#count()
print(user_data.count(45))
#find pos
print(user_data.index(45))
#unpacking tuples with dict
# student_data= ("Ragini Roy", 29, "project": ["predict spending habits"], 'true')
# name,age,project= student_data
# print(name)
# print(age)
# print(project)

#error-> without comma at the end of tuple says tuple object is not callable
random_data = (
    ("naam", 28),
    ("kaam",27)
)
print(random_data[0])
print(random_data[0][1])
print(random_data[1][1])
#data is fixed -> use tuples 

coordinates = (28.6139, 77.2090)
print(coordinates)
rgb_color = (255, 0, 0)
print(rgb_color)

#sequences-> stores multiple items in specific order
# String (str)
# List (list)
# Tuple (tuple)
# Range (range)

# All sequences support:

# Indexing
# Slicing
# Iteration (for loops)
# Length (len())
#set and dict are unordered not sequences



#sets->Collection of unique elements
sets= {1,24,45,56,75}
# print(sets.add(78))
#add() directly modifies n returns  none
#another way
sets.add(89)
# print(sets)

#list comprehensions
sq= [i*2 for i in range(1,6)]
print(sq)

fruits = ["mango", "apple", "grapes"]

upper_fruits = [fruit.upper() for fruit in fruits]

print(upper_fruits)

#map and lambda
# n= [11,24,53,54,32]
# sq= list(map(lambda x : x * x, n))
# print(sq)

#tuple unpacking
tuple= (124,564,354,753,764)
a,b,c,d, e= tuple
#added all the values
print(a + b + c+ d+ e)

#without parentheses
a,b= 5,9
print(a)
print(b)

#unpacking from lists
li=[3.14,3.147,3.14567]
a,b,c=li 
print(li)

#using extended unpacking
nums= [12,13,14,15,16,17,18,19,22]
#collecting remaining values from list
a,*b,c=nums
print(a)
print(b)
print(c)

pairs= [(1,'a'), (2, 'b') , (3,'c')]
for nums,ch in pairs:
    print(nums,ch)

#exe
planet= 'earth'
diameter= 12742
#('The diameter of {} is {}'.format(a=planet, b=diameter))
#IndexError: Replacement index 0 out of range for positional args tuple
print('The diameter of {a} is {b}'.format(a=planet, b=diameter))

s= 'sam is cool in painting portrait'
print(s.split())

lst= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1] [2])

d={'k1': [1,2,3, {'tricky': ['oh', 'man', 'inception', {'target': [1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])
