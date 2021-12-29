myDic = {
            'name' : 'bilal',
            'age': 24,
            'grade' : 'A',
            'List' : [1,2,3,4],
            'dic2' : {'surface': 'an area of consideration', 'key': 'value'},
            45 :54
}


myDic['List'] = [3,6,7,8,9,0,8,6,4,3] # change the elements inside the list
myDic['grade'] = 'B'
print(myDic['age'])
print(myDic['grade'])
print(myDic['dic2']['surface'])
print(myDic['dic2']['key'])
print(myDic['List'])


# Dictionary methods
updated_dic = {

            'friends' : 'many',
            'others' : 'Loyal',
            'questions' : 'answers',
            'grade' : 'C', #update command also replaces the old valye in the dictionary to a new one such as before it was grade a but now it will change to grade c
            453 : 73627
}

print(type(myDic))
print(myDic.keys())
print(myDic.values())
print(list(myDic))
print(type(list(myDic)))

myDic.update(updated_dic) # updates means to add more content to the original dictionary
print(myDic)
print(myDic.get('friends2')) # since friends2 is not availbale in the dictionary therefore it returns the value of none 

#but if
print(myDic['friends2']) # since friends2 is not availbale in the dictionary therefore it returns error unlike get function


