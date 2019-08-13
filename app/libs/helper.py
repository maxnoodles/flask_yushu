

def is_isbn_or_key(word):
    """
    判断 word 是 key 还是 isbn
    isbn13 13个0-9
    isbn10 10个0-9，含有一些’-‘
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('_', '')
    if '_' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
