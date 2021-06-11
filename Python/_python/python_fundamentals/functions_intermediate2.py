#1 Update Values in Dictionaries and Lists
## 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
## 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
## 3. In the sports_directory, change 'Messi' to 'Andres'
## 4. Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

####

# 2 Iterate Through a List of Dictionaries
marvel_characters = [
    {"character_name": "Thor", "is_good": True},
    {"character_name": "Loki", "is_good": "Kind of?"},
    {"character_name": "Thanos", "is_good": False},
    {"character_name": "Captain America", "is_good": True},
    {"character_name": "Black Panther", "is_good": True},
    {"character_name": "Iron Man", "is_good": True},
    {"character_name": "Hulk", "is_good": True},
    {"character_name": "Black Widow", "is_good": True}
]
def iterateDictionary(some_list):
    for j in range(len(some_list)):
        print(", ".join(["{0} - {1}".format(k, v) for k, v in some_list[j].items()]))
print(iterateDictionary(marvel_characters))

# 3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for j in range(len(some_list)):
        print(some_list[j][key_name])
print(iterateDictionary2('character_name', marvel_characters))

# 4 Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for k, v in some_dict.items():
        print(f"{len(v)} {k.upper()}")
        for j in range(len(v)):
            print(f"{v[j]}")
print(printInfo(dojo))