import phantom_tollbooth

def getWords(book) -> list:
    book2 = ""
    book.replace("'s", "'")
    replaceChar = [
        "", "'", "\"", "?", ".", ",", "(", ")", ";", "\n"
    ]
    for char in book:
        if char not in replaceChar:
            book2 += char
    
    returnList = book2.split(" ")
    return returnList

def wordsToCount(words) -> list:
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
    for word in words:
        if word not in nonCountable:
            returnWords.append(word)
    return returnWords

def countWords(words) -> dict:
    returnDict = {}
    foundWords = []
    for word in words:
        if word in foundWords:
            returnDict[word] += 1
        else:
            foundWords.append(word)
            returnDict[word] = 1

    return returnDict

def sortDict(dict) -> dict:
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

    return returnDict

def printTop50(words):
    num = 50
    for word in words:
        if num > 0:
            print(f"   {word:^8} - {words[word]}")
            num -= 1
        else:
            print()
            return

def main():
    print("Word Counter for Phantom Tollbooth!\n   Words excluded include prepositions, pronouns, conjugations, and articles.\n")
    input("Press 'Enter' to count!\n")

    book = phantom_tollbooth.get_text().lower()
    allWords = getWords(book)
    countedWords = countWords(wordsToCount(allWords))
    sortedWords = sortDict(countedWords)
    printTop50(sortedWords)

    input("Press 'Enter' to Exit\n")
    
    
    

if __name__ == '__main__':
    main()