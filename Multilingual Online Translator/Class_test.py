import requests
from bs4 import BeautifulSoup

class Translator:

    def __init__(self):
        while True:
            self.lang = input("Type 'en' if you want to translate from French into English, or 'fr' if you want to "
                              "translate from English into French: \n")
            if self.lang == "en" or self.lang == "fr":
                break
            else:
                print("Language not valid.")

        self.word = input("Type the word you want to translate: ")

        print(f'You chose "{self.lang}" as a language to translate "{self.word}" to.')


    def create_url(self):

        base_url = 'https://context.reverso.net/translation/'

        if self.lang == 'fr':
            full_url = base_url + 'english-french/' + self.word
            return full_url
        elif self.lang == 'en':
            full_url = base_url + 'french-english/' + self.word
            return full_url

    def connect_and_scrape(self):
        user_agent = 'Mozilla/5.0'
        r = requests.get(self.create_url(), headers={'User-Agent': user_agent})
        status = r.status_code
        if status == 200:
            print(f'{status} OK')
            soup = BeautifulSoup(r.content, 'html.parser')
            find_translations = soup.find_all('a', class_='translation')
            translations = []
            for x in find_translations:
                translations.append(x.text.strip())
            del translations[0]
            print('Translations')
            print(translations)
            get_examples_combined = soup.find_all('div', {"class": "example"})
            examples_both = []
            for x in get_examples_combined:
                examples_both.append(x.text.strip().replace("\n\n\n\n\r\n          ", ""))
            print(examples_both)
        else:
            print('Failed to connect')

Translator().connect_and_scrape()

