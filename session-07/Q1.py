def analyze_text(text):
    
    #matn ro az fasele joda mikone 
    words = text.split()


    #meghdar dehi avalie
    result = {
     'words': len(words),
     'letters': 0,
     'digits': 0,
     'most_common_letter': '',
     'most_common_word': '',
     'longest_word': '',
     'shortest_word': '',
     'palindrome_words': 0,
     'uppercase': 0,
     'lowercase': 0
    }

    letter_count = {}
    word_count = {}


    #loop baraye barresi kalamat
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
        #loop baraye barresi horoof
        for char in word:
            if char.isalpha():
                result['letters'] += 1
                letter_count[char] = letter_count.get(char, 0) + 1

            if char.isdigit():
                result['digits'] += 1

            if char.isupper():
                result['uppercase'] += 1

            if char.islower():
                result['lowercase'] += 1

        if len(word) > 1 and word == word[::-1]:
            result['palindrome_words'] += 1

    if words:
        result['longest_word'] = max(words, key=len)
        result['shortest_word'] = min(words, key=len)

    if letter_count:
        result['most_common_letter'] = max(letter_count, key=letter_count.get)

    if word_count:
        result['most_common_word'] = max(word_count, key=word_count.get)

    return result



text = input('متن خود را وارد کنید : ')
print(analyze_text(text))