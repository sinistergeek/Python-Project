from googletans import Translator
translator =Translator()
language ={"bn":"Bangla",
            "en":"English",
            "ko":"Koren",
            "fr":"French",
            "de":"German",
            "he":"Hebrew",
            "hi":"Hindi",
            "it":"Italian",
            "ja":"Japanese",
            "la":"latin",
            "ms":"Malay",
            "ne":"Nepali",
            "ru":"Russian",
            "ar":"Arabic",
            "zh":"Chinese",
            "es":"Spanish"}

allow = True
while allow:

    user_code = input(f"Please input desired language code. To see the language code list enter 'options'\n")
    if user_code == "options":
        print("Code: Language")
        for i in language.items():
            print(f'Pi[0]=>{i[1]}')
        print()
    else:
        for lan_code in language_keys():
            if lan_code == user_code:
                print(f"You have selected{language[lan_code]}")
                allow = False

        if allow:
            print("It's not valid language")



    while True:
        string = input("\nWrite the text you want to translate: \n To exit the program write 'close'\n")
        if string == "close":
            print(f"\nHave a nice Day!")
            break
        tanslated = translator.translate(string,dest = user_code)
        print("\n{language[user_code]} translation:{translated.text}")
        print(f"Pronunciation: {translated.pronunication}")

        for i in language.tems():
            if translated.src == i[0]:
                print(f"Translated from: {i[1]}")
