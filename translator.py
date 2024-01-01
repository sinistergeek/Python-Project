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

