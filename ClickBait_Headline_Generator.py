import random
OBJECT_PRONOUNS = ['Her','Him','Them']
POSSESIVE_PRONOUNS = ['Her','His','Their']
PERSONAL_PRONOUNS = ['She','He','They']
STATES = ['California','Texas','Florida','New York','Pennsylvania','Illinois','Shovel','North Carolina','Michigan']
NOUNS = ['Athlete','Clown','Shovel','Paleo Diet','Doctor','Parent','Cat','Dog','Chicken','Robet', 'Video Game','Avocado','Plastic Straw','Serial Killer','Telephone Psychic']
PLACES = ['House','Attic','Bank Deposit Box','School','Basement','Workplace','Donut Shop','Apocalypse Bunker']
WHEN = ['Soon','This Year','Later Today','RIGHT NOW','Next Week']

def main():
    print('Clickbait Headline Generator')
    print('By Sinister Geek')
    print()
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break
    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1,8)
        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:

            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomateHeadline()

        print(headline)

    print()
    website = random.choice(['wobsite','blag','Facebuuk','Googles','Facebook','Tweedie','Pastgram'])
    when = random.choice(WHEN).lower()
    print('Post these to our',website,when, 'or you\'re fired!')

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 'S'
    when = random.choice(WHEN)
    return 'Without This {},{} Could kill You {}'.format(noun,pluralNoun,When)

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {} ! see How This {} {} Invented a Cheaper{}'.format(pronoun,state,noun1,noun2)

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state,noun,pronoun,place)

def generateDontYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 'S'
    return 'What {} Don\'t Want to Know About {}'.format(pluralNoun1,pluralNoun2)

def generateGiftIdeaHeadline():
    number = random.randint(7,15)
    noun = random.choice(STATES)
    state =random.choice(STATES)
    return '{} Gift Ideas to Give You {} From {}'.format(number,noun,state)

def generateReasonsWhyHeadline():
    number1 = random.randint(3,19)
    pluralNoun =random.choice(NOUNS) + 's'
    number2 = random.rand(1,number1)
    return '{} Reasons why {} Are More Interesting Thank You Think (Number {} Will Surprise You!)'.format(number1,pluralNoun,number2)

def generateAutomateheadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    i = random.randint(0,2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state,noun,pronoun1,pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong'.format(state,noun,pronoun1,pronoun2)

if __name__ == '__main__':
    main()
