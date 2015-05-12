word = raw_input("Enter the word you want to translate to Pig Latin: ")

first_word = word[0]
remaining_words = word[1:]
pig_latin = remaining_words + first_word + "ay"

if len(word) > 1 and word.isalpha():
    print pig_latin.lower()
else:
    print word + " is not a word"
