import requests
from bs4 import BeautifulSoup

input_url = input("Input the URL: ")

# def get_info(url):
#     r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#     soup = BeautifulSoup(r.content, 'html.parser')
#     if r.status_code != 200 or soup.find('span', {'data-testid': 'plot-xl'}) is None:
#         print('Invalid movie page!')
#     else:
#         title = soup.find('h1').text
#         description = soup.find('span', {'data-testid': 'plot-xl'}).text
#         print({"title": title, "description": description})

# def write_file(url):
#
#     response = requests.get(url)
#     if response.status_code == 200:
#         r = response.content
#         with open('source.html', 'wb') as file:
#             file.write(r)
#             print('Content saved.')
#     else:
#         print('The URL returned', response.status_code)


r = requests.get(input_url)
soup = BeautifulSoup(r.content, 'html.parser')

# article_type = soup.find('span', {'data-test': 'article.type'}).text

# article_contents = soup.find('a', {'data-track-action': 'view article'})
# print(article_contents.get('href'))


def get_article_type(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    article_type = soup.find('span', {'data-test': 'article.type'}).text
    return article_type

def get_links(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all('a', {'data-track-action': 'view article'})
    links_href = []
    for link in links:
        links_href.append(link.get('href'))

    return links_href

def get_full_paths(links):

    full_paths = ['https://www.nature.com' + link for link in links]
    return full_paths

def save_articles(full_paths):

    for link in full_paths:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.find('title').text
        article_body = soup.find('div', {"class": "c-article-body"}).text
        with open(f'{title.replace(" ", "_")}.txt', 'w') as file:
            file.write(article_body)


if __name__ == "__main__":
    links = get_links(input_url)
    full_paths = get_full_paths(links)
    save_articles(full_paths)