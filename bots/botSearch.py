import wikipedia



def bot_search():
    wikipedia.set_lang('en')
    term_search = input(f'\nWhat do you want to search for? ')
    
    wiki_search = wikipedia.search(term_search, results=8)
    print(f'\n Related search: {wiki_search}\n')

    wiki_valid = input('Do you want to choose another term above? (y/n) ')

    if wiki_valid == 'y' or wiki_valid == 'Y':
        wiki_word = input(
            f'\nWhat is the term above do you want to search for?\n ')
        wiki_article = wikipedia.summary(wiki_word, sentences=10)
        print(f'\n{wiki_article}\n')

        with open('article/subject.txt', 'w', encoding="utf-8") as f:
            for article in wiki_article:
                f.writelines(article)

        return True


    wiki_content = wikipedia.summary(term_search, sentences=10)
    print(f'\n{wiki_content}\n')

    with open('article/subject.txt', 'w', encoding="utf-8") as f:
        for content in wiki_content:
            f.writelines(content)
