# create a dict for quiz
quiz = {
    'question1': {
        'question': 'What is the Capital of France?',
        'answer': 'Paris'
    },
    'question2': {
        'question': 'What is the Capital of Germany?',
        'answer': 'Berlin'
    },
    'question3': {
        'question': 'What is the Capital of Spain?',
        'answer': 'Madrid'
    },
    'question4': {
        'question': 'What is the Capital of Iran?',
        'answer': 'Tehran'
    },
    'question5': {
        'question': 'What is the Capital of USA?',
        'answer': 'Newyork'
    },
    'question6': {
        'question': 'What is the Capital of England?',
        'answer': 'London'
    },
}

#create a loop for dict Get answer from User
score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input('answer?')
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print('your score is ' + str(score))
    else:
        print('Wrong')
        print('The answer is :' + value['answer'])
print(f'you have {int((score /6) * 100)} % correct answer')