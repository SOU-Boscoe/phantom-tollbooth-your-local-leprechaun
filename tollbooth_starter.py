import phantom_tollbooth

def getWords(book) -> list:
    """
    This function returns a list of all words, formated more properly into just words without any special characters.

    Parameters
    ----------
    book : Str  A string of the whole text of the book.

    Returns
    -------
    returnList : list  A list of all the words in the book. 
    """

    book2 = ""
    #Helps with a weirder one to replace normally
    book.replace("'s", "'")
    #List of all charcters to replace in the book
    replaceChar = [
        "", "'", "\"", "?", ".", ",", "(", ")", ";", "\n"
    ]
    #Goes through each character and removes all characters in replaceChar, making a new string
    for char in book:
        if char not in replaceChar:
            book2 += char
    
    #splits and returns the list of all words with special characters removed
    returnList = book2.split(" ")
    return returnList

def wordsToCount(words) -> list:
    """
    This functions returns a list of words that should be counted when counted. It gets rid of all words in nonCountable, such as pronouns, pre
    positions, conjugations, and articles.

    Parameters
    ----------
    words : list  A list of all possible words that need to be sorted out first

    Returns
    -------
    returnWords : list  List of all words that have now been sorted through
    """
    #All words to sort out of list
    nonCountable = [
        "", "the", "a", "an", "aboard", "about", "above", "across", "after", "against",
        "along", "against", "along", "amid", "among", "anti", "around", "as",
        "as", "at", "before", "behind", "below", "beneath", "beside", "besides",
        "between", "beyond", "but", "by", "concerning", "considering", "despite",
        "down", "during", "except", "excepting", "excluding", "following", "for",
        "from", "in", "inside", "into", "like", "minus", "near", "of", "off",
        "on", "onto", "opposite", "outside", "over", "past", "per", "plus", 
        "regarding", "round", "save", "since", "than", "through", "to", "towards",
        "toward", "under", "underneath", "unlike", "until", "up", "upon", "versus",
        "via", "with", "within", "without", "for", "and", "nor", "but", "or", "yet",
        "so", "i", "he", "she", "they", "his", "her", "their", "mine", "we", "you",
        "it", "us", "ours", "theirs", "this", "these", "that", "those", "who", "whom",
        "which", "what", "all", "another", "any", "anybody", "anyone", "each", "im", "my",
        "me"
    ]
    returnWords = []
    #Check which words will stay and which will not be returned
    for word in words:
        if word not in nonCountable:
            returnWords.append(word)
    return returnWords

def countWords(words) -> dict:
    """
    This function counts how many times each word is found in a list of words. Returns a dict with keys as words, 
    and values as the number of instances

    Parameters
    ----------
    words : list  A list of words you want to count instances of a word in

    Returns
    -------
    returnDict : dictionary  A dictionary with words as the key and number of instances as values
    """
    returnDict = {}
    foundWords = []
    #Goes through each word, if in foundWords, add to returnDict value, otherwise add to foundWords and returnDict value = 1
    for word in words:
        if word in foundWords:
            returnDict[word] += 1
        else:
            foundWords.append(word)
            returnDict[word] = 1

    return returnDict

def sortDict(dict) -> dict:
    """
    This function is used to sort a dictionary by value from highest to lowest

    Parameters
    ----------
    dict : dictionary This is the dictionary you want sorted. Values are ints, keys are strings

    Returns
    -------
    returnDict : dictionary  Returns an ordered dictionary based on values
    """
    num = 0
    returnDict = {}
    while num < len(dict):
        highestKey = ""
        highestValue = 0
        for key in dict:
            if dict[key] > highestValue:
                highestKey = key
                highestValue = dict[key]
            else:
                pass
        returnDict[highestKey] = highestValue
        del dict[highestKey]

        num += 1

    return returnDict

def printTop50(words) -> None:
    """
    This functions prints the first 50 keys and values of a dictionary

    Parameters
    ----------
    words : dictionary  The dictionary you want to print the first 50 of
    """
    num = 50
    for word in words:
        if num > 0:
            print(f"   {word:^8} - {words[word]}")
            num -= 1
        else:
            print()
            return

def main():
    #Quick hello
    print("Word Counter for Phantom Tollbooth!\n   Words excluded include prepositions, pronouns, conjugations, and articles.\n")
    input("Press 'Enter' to count!\n")

    #Entire Text of phantom_tollbooth
    book = phantom_tollbooth.get_text().lower()
    allWords = getWords(book)
    countedWords = countWords(wordsToCount(allWords))
    sortedWords = sortDict(countedWords)
    printTop50(sortedWords)

    input("Press 'Enter' to Exit\n")
    
    
    

if __name__ == '__main__':
    main()