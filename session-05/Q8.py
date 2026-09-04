#برنامه ای بنویسید که یک متن از کاربر دریافت کند و کزارش های زیر را تولید کند : 
#Total characters: 
#Total words: 
#Total leters: 
#Total digits: 
#Total spaces: 
#Total uppercase: 
#Total lowercase: 
#Longest word: 
#Shortest word: 
#Most repeated character: 
#Most repeated word: 

text = input('رشته ی خود را وارد کنید :  ')

words = text.split()
total_characters = len(text)
total_words = len(words)


letters = 0
digits = 0
spaces = 0
uppercase = 0
lowercase = 0

for char in text:
    if char.isalpha():
        letters += 1

    if char.isdigit():
        digits += 1

    if char == ' ':
        spaces += 1

    if char.isupper():
        uppercase += 1

    if char.islower():
        lowercase += 1


# طولانی‌ترین و کوتاه‌ترین کلمه

if words:
    longest_word = words[0]
    shortest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

else:
    longest_word = ''
    shortest_word = ''


# بیشترین کاراکتر تکراری

if text:
    most_char = text[0]
    max_char_count = 0

    for char in text:
        count = text.count(char)

        if count > max_char_count:
            max_char_count = count
            most_char = char
else:
    most_char = ''


# بیشترین کلمهٔ تکراری

if words:
    most_word = words[0]
    max_word_count = 0

    for word in words:
        count = words.count(word)

        if count > max_word_count:
            max_word_count = count
            most_word = word

else:
    most_word = ''


print('Total characters: ', total_characters)
print('Total words: ', total_words)
print('Total letters: ', letters)
print('Total digits: ', digits)
print('Total spaces: ', spaces)
print('Total uppercase: ', uppercase)
print('Total lowercase: ', lowercase)
print('Longest word: ', longest_word)
print('Shortest word: ', shortest_word)
print('Most repeated character: ', most_char)
print('Most repeated word: ', most_word)