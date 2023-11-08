import phantom_tollbooth

wordCount = {}

wordCountOrder = []

notWords = [
    "the", "a", "an", "and", "but", "or", "he", "her", "it",
    "she"
]

def getWords(book):
    """
    This function will return all words from the book in a list without any blank spaces or anything like that, mostly using replace
    and split.

    Parameters
    ----------
    book - Str     This is the whole text of the thing we want to spit
    """
    returnWords = book.replace("?", "").replace("\n", " ").replace(",", "").replace("\"", "").replace(".", "").replace(";", "").replace("(", "").replace(")", "").split(" ")
    for word in returnWords:
        if word == "":
            del returnWords[returnWords.index(word)]
    return returnWords

def checkWordCount(allWords):
    for word in allWords:
        if word not in notWords:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

    return

def printTop50():
    pass

def main():
    book = phantom_tollbooth.get_text().lower()
    allWords = getWords(book)
    checkWordCount(allWords)
    print(sorted(wordCount.items(), reverse=True))
    

if __name__ == '__main__':
    main()