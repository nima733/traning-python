quiz = {
    'question1': 'what is your friend name?',
    'question2': 'what is your address?',
    'question3': 'where are you living?',
    'question4': 'what is your lastname',
    'question5': 'how old are you?',
    'question6': 'what is your name?',
    'nested dict': {
        'nima': 'abbasnejad'
    }
}
# -----------------------
print(quiz.keys())
quiz['my name is'] = 'nima'
print(quiz.keys())
print(quiz.get('question1'))
print(quiz.values())
print(quiz.items())
if 'nima' in quiz:
    print(quiz)
# access item is dictionary
# -----------------
# change items in dictionary
quiz.update({"nima": '24'})
print(quiz)
quiz.update({'question1': 'are you ali??'})
# -----------------------
# delete item dictionary
quiz.pop('question3')
print(quiz)
quiz.popitem()
print(quiz)
# del quiz
# print(quiz) #del item delete all data key and value from quiz
# quiz.clear()
# print(quiz)
# clear method delete all key and value item and return a empty dictionary
# -------------------------------
# loop on dictionary
for vale in quiz:
    print(vale, end=', ')
    # just print keys
print('')
for key, value in enumerate(quiz):
    print(key, value, end=', ')
    # print index with keys
print('')
for x in quiz:
    print(quiz[x])
    # print values
print('')
for x in quiz.values():
    print(x)
    # print just values
print()
for i in quiz.keys():
    print(i)
    # print just key
print('')
for x, y in quiz.items():
    print(x, y)
    # print both key and value
# ---------------------------------
# copy Dictionary
print('copy Dictionary')
copy_dict = quiz.copy()
print(copy_dict)
print('')
copy1_dict = dict(quiz)
print(copy1_dict)
# ---------------------------------
# nested Dictionary

print(quiz['nested dict']['nima'])
# ---------------------------------
# create a dictionary with 3 keys
# fromkeys()=method return a dictionary with specified key and specified value
x = ('nima', 'ali', 'reza')
y = (1, 2, 3)
new_dict = dict.fromkeys(x, y)
print(new_dict)
# ------------------------------
# setdefault()
x = quiz.setdefault('nima', 'programming')
print(x)
# -------------------------------
