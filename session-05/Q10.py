#برنام ای بنویسید که دو جمله از کاربر بگیرید و مشخص کنید چه کلماتی در هر دو جمله وجود دارند 
#Sentence 1 : 
#I love Python programming
#Sentence 2 : 
#Python is a powerful programming language 
#Common words: 
#Python 
#Programming 


jomle1 = input(' لطفا جمله ی اول خود را وارد کنید : ').lower()
jomle2 = input(' لطفا جمله ی دوم خود را وارد کنید : ').lower()

word1= jomle1.split()
word2= jomle2.split()

print('کلمات مشترک : ')

for word in word1:
    if word in word2:
        print(word)