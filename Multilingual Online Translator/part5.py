import requests
from bs4 import BeautifulSoup

languages_dict = {
    0: "All",
    1: "Arabic",
    2: "German",
    3: "English",
    4: "Spanish",
    5: "French",
    6: "Hebrew",
    7: "Japanese",
    8: "Dutch",
    9: "Polish",
    10: "Portuguese",
    11: "Romanian",
    12: "Russian",
    13: "Turkish"
}

loop_list = ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese", "dutch", "polish", "portuguese",
             "romanian", "russian", "turkish"]

print("Hello, you're welcome to the translator. Translator supports: ")
for key, value in languages_dict.items():
    print(str(key) + '. ' + value)

lang_from = languages_dict[int(input("Type the number of your language: "))]
lang_to = languages_dict[int(input('Type the number of language you want to translate to:'))]

word = input('Type the word: ')

headers = {'User-Agent': 'Mozilla/5.0'}

url_list = []
if lang_to != "All":
    r = requests.get(
        "https://context.reverso.net/translation/" + lang_from.lower() + "-" + lang_to.lower() + "/" + word,
        headers=headers)

    if r.status_code == 200:
        print('200 OK')
        print()

        soup = BeautifulSoup(r.content, 'html.parser')

        words_block = soup.find('div', {'id': 'translations-content'})
        words = words_block.find_all('a', {'class': 'translation'})

        sentences_block = soup.find('section', {'id': 'examples-content'})
        sentences = sentences_block.findAll('div', {'class': ['src', 'trg']})

        print(f"{lang_to} Translations")
        print()
        for word in words[:5]:
            print(word.get_text().strip())
        print()

        print(f"{lang_to} Examples")
        sent = []
        for idx, sentence in enumerate(sentences):
            # print(sentence.get_text().strip().replace('.', '').replace('"', ''))
            sent.append(sentence.get_text().strip())

        z = 0
        for idx, sentence in enumerate(sent):
            if sentence == '':
                sent.remove(sentence)
            if z < 15:
                print(sentence)
                z += 1

    else:
        print('Network error.')

elif lang_to == "All":
    for language in loop_list:
        if language != lang_from.lower():
            url_list.append(
                "https://context.reverso.net/translation/" + lang_from.lower() + "-" + language + "/" + word)
    with open(f'{word}.txt', 'w') as f:
        for url in url_list:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html.parser')

                words_block = soup.find('div', {'id': 'translations-content'})
                words = words_block.find_all('a', {'class': 'translation'})

                sentences_block = soup.find('section', {'id': 'examples-content'})
                sentences = sentences_block.findAll('div', {'class': ['src', 'trg']})
                get_lang = soup.find_all('span', class_="option front")

                langs = []
                for x in get_lang:
                    langs.append(x.text.strip())

                print()
                print(f'{langs[1]} Translations:')
                for word in words[:1]:
                    print(word.get_text().strip())
                print()

                print(f"{langs[1]} Examples")
                sent = []
                for idx, sentence in enumerate(sentences):
                    # print(sentence.get_text().strip().replace('.', '').replace('"', ''))
                    sent.append(sentence.get_text().strip())

                z = 0
                for idx, sentence in enumerate(sent):
                    if sentence == '':
                        sent.remove(sentence)
                    if z < 2:
                        print(sentence)
                        z += 1
                print()






else:
    print('Network error.')
