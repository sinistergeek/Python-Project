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

