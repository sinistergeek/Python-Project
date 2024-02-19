import random,sys

QUESTIONS = [{
            'question':"How many times can you take apple 2 apples a pile of 10 apples?",
            'answer': "Once. Then you have a pile of 8 apples.",
            'accept': ['once','one','1']
            },
        {
            'question': "The clerk at a butcher shop is exactly 177 centimeters tall. What do they weigh",
            'answer':"The clerk weighs meat.",
            'accept':['meat']
            }
        ]
CORRECT_TEXT = ['Correct','That is right.',"You're right","You got it.",'Righto!']
INCORRECT_TEXT = ['Incorrect!',"Nope, that isn't it.",'Nope.','Not quite.','You missed it.']

print('''
      Trick Questions
      Can you figure out the answers to these trick questions?
      (Enter QUIT to quit at any time.)
''')

input('Press Enter to begin...')
random.shuffle(QUESTIONS)
score = 0
for questionNumber, qa in enumerate(QUESTIONS):
    print('\n' * 40)
    print('Question:',questionNumber + 1)
    print('Score:',score, '/',len(QUESTIONS))
    print('QUESTION:',qa['question'])
    response = input('ANSWER:').lower()
    if response == 'quit':
        print('Thanks for playing')
        sys.exit()
    correct = False
    for acceptanceWord in qa['accept']:
        if acceptanceWord in response:
            correct = True
    if correct:
        text = random.choice(CORRECT_TEXT)
        print(text,qa['answer'])
        score += 1

    else:
        text = random.choice(INCORRECT_TEXT)
        print(text,'The answer is:',qa['answer'])
    response = input('Press ENter for the next question...').lower()
    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()
print("That's the questions. Thanks for playing!")
