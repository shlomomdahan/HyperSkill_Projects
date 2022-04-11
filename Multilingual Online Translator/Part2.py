import requests
from bs4 import BeautifulSoup


def welcome():
    while True:
        lang = input("Type 'en' if you want to translate from French into English, or 'fr' if you want to translate "
                     "from English into French: \n")
        if lang == "en" or lang == "fr":
            break
        else:
            print("Language not valid.")

    word = input("Type the word you want to translate: ")

    print(f'You chose "{lang}" as a language to translate "{word}" to.')

    return lang, word


def create_url(language, word_to_translate):
    base_url = 'https://context.reverso.net/translation/'

    if language == 'fr':
        full_url = base_url + 'english-french/' + word_to_translate
        return full_url
    elif language == 'en':
        full_url = base_url + 'french-english/' + word_to_translate
        return full_url

def connect_and_scrape(url):

    user_agent = 'Mozilla/5.0'
    r = requests.get(url, headers={'User-Agent': user_agent})
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






if __name__ == '__main__':
    lang, word = welcome()
    url = create_url(lang, word)
    connect_and_scrape(url)


