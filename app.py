import wikipedia


TERM_SEARCH = input('What do you want to search for? ')


def bot_search():
    wikipedia.set_lang('en')

    wiki_Search = wikipedia.search(TERM_SEARCH, results=4)
    print(f'\n{wiki_Search}\n')

    wiki_article = wikipedia.summary(TERM_SEARCH, sentences=10)
    print(f'\n{wiki_article}\n')

    with open(f'article/subject.txt', 'w', encoding="utf-8") as f:
        for article in wiki_article:
            f.writelines(article)


if __name__ == '__main__':
    bot_search() 
