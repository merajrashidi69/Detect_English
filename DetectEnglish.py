#DetectEnglish.py

def sort(file):
    result = list()
    file = open(file,'r').readlines()
    for value in file:
        value=value.rstrip('\n')
        result.append(value)
    return result

def detect(word):
    word=word.lower()
    file = sort('dictionary.txt')
    for items in file:
        if items == word:
            print('Detected: ' + word)




            
