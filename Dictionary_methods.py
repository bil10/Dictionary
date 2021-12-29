W_Dict = {

            "technology" : "Scientific methods",
            "roman numerals" : "Ancient numbers",
            "counting" : [1, 2, 3, 4, 5],
            "newDict" : {"paper": "something made from wood"} ,#----nested dictionary(dictionary inside dictionary)
                34 : 43
}


print(type(W_Dict.keys())) #typecasting
print(list(W_Dict)) #typecasting changes to list
print(W_Dict.values()) #prints the values inside the dictionary
print(W_Dict.items()) #prints all the contents inside the dictionary in the form of a tuple
print(type(W_Dict))
