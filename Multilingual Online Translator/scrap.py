import requests
from bs4 import BeautifulSoup

languages = {
    '1': 'arabic',
    '2': 'german',
    '3': 'english',
    '4': 'spanish',
    '5': 'french',
    '6': 'hebrew',
    '7': 'japanese',
    '8': 'dutch',
    '9': 'polish',
    '10': 'portuguese',
    '11': 'romanian',
    '12': 'russian',
    '13': 'turkish'
}

def welcome():

    print("Hello, welcome to the translator. Translator supports: ")
    for k, v in languages.items():
        print(f'{k}.', v.capitalize())

    source_lang = input("Type the number of your language: \n")
    to_lang = input("Type the number of language you want to translate to or '0' to translate to all languages: \n")
    word = input("Type the word you want to translate: ")

    return source_lang, to_lang, word

def create_url(source_num, dest_lang_num, word_to_trans):

    base_url = 'https://context.reverso.net/translation/'

    source_lang = languages[source_num]

    if dest_lang_num != '0':
        to_lang = languages[dest_lang_num]
    else:
        to_lang = 0

    url_list = []
    if to_lang == 0:
        for k, v in languages.items():
            if v != source_lang:
                url_list.append(base_url + f'{source_lang}-{v}/' + word_to_trans)
        return url_list, source_lang, to_lang
    else:
        full_url = base_url + f'{source_lang}-{to_lang}/' + word_to_trans
        return full_url, source_lang, to_lang

def connect_and_scrape(url, to_lang, word_to_tr):

    user_agent = 'Mozilla/5.0'

    if type(url) == list:
        master_list = []
        for link in url:
            r = requests.get(link, headers={'User-Agent': user_agent})
            status = r.status_code
            if status == 200:
                soup = BeautifulSoup(r.content, 'html.parser')
                get_lang = soup.find_all('span', class_="option front")

                langs = []
                for x in get_lang:
                    langs.append(x.text.strip())

                print(f'{langs[1]} Translations:')

                find_translations = soup.find_all('a', class_='translation')
                translations = []
                for x in find_translations:
                    translations.append(x.text.strip())
                del translations[0]

                n = 0
                for word in translations:
                    if n < 1:
                        print(word)
                        master_list.append(word)
                        n += 1


                print()
                print(f'{langs[1]} Example:')
                get_examples = soup.find_all('div', {'class': ['src', 'trg']})
                examples = []
                for x in get_examples:
                    examples.append(x.text.strip().replace('\r\n          ', ''))
                num = 0
                for i in range(len(examples)):
                    if num < 2:
                        print(examples[int(i * 2)])
                        print(examples[int((i * 2) + 1)])
                        num += 1

            else:
                print('Failed to connect')


    else:
        r = requests.get(url, headers={'User-Agent': user_agent})
        status = r.status_code
        if status == 200:
            print(f'{status} OK')
            print()
            soup = BeautifulSoup(r.content, 'html.parser')
            find_translations = soup.find_all('a', class_='translation')
            translations = []
            for x in find_translations:
                translations.append(x.text.strip())
            del translations[0]
            print(f'{to_lang.capitalize()} Translations')
            n = 0
            for word in translations:
                if n < 5:
                    print(word)
                    n += 1
            print()
            get_examples = soup.find_all('div', {'class': ['src', 'trg']})
            examples = []
            for x in get_examples:
                examples.append(x.text.strip().replace('\r\n          ', ''))
            print(f'{to_lang.capitalize()} Examples')
            num = 0
            for i in range(len(examples)):
                if num < 10:
                    print(examples[int(i*2)])
                    print(examples[int((i*2)+1)])
                    num += 1
        else:
            print('Failed to connect')






if __name__ == '__main__':
    source, to, word = welcome()
    urls, source_lang, to_lang = create_url(source, to, word)
    connect_and_scrape(urls, to_lang, word)

