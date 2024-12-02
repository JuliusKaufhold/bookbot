def numberWords(words):
    wordList = words.split()
    return len(wordList)

def count_characters(words):
    words.lower()
    countChars = dict()
    for char in words:
        if char not in countChars:
            countChars[char] = 1
        else:
            countChars[char]+=1
    return countChars

def bookReport(book,content):
    print(f"book report of book: {book}")
    numWords = numberWords(content)
    print(f"The book has {numWords} words.")
    chars = count_characters(content)
    sortedChars = sorted(chars.items(),key=lambda x:x[1],reverse = True)
    sortedDict = dict(sortedChars)
    for char in sortedDict:
        count = sortedDict[char]
        if char.isalpha():
            print(f"Character {char} appears {count} times.")


def main():
    with open("books/frankenstein.txt") as book:
        book_content = book.read()
        bookReport("Frankenstein",book_content)

if __name__ == "__main__":
    main()
