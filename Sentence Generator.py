import random
import  time
selected_mode='Long'
names=['Peter','Sofia','Angel',"John","Jack","Steven",'Jake','Logan','Jim',"George"]
verbs=["found","accidentally broke","secretly borrowed","chased","forgot","discovered","stole","built","lost","delivered"]
details=["a mysterious USB drive","a box full of old laptops","the last slice of pizza","a talking sandwich",  "a very expensive keyboard","a secret treasure map",  "an enormous dictionary",   "a computer that could think", "a bag full of potatoes", "a golden toilet"]
places=["in the school library","under the kitchen table","inside an abandoned warehouse","near the train station","on the roof","in the middle of the forest","inside a computer shop","behind the supermarket","at the airport", "in a secret laboratory"]
Time=[ "yesterday","at midnight","during the lunch break",  "just before sunrise","last weekend",  "on Monday morning","three days ago", "during the night","after work", "at exactly 3 o'clock"]
def random_words(words):
    return random.choice(words)

print('=====================Sentence Generator ===================')
while True:
    print('Play')
    time.sleep(1)
    print('Options')
    time.sleep(1)
    print('Exit')
    time.sleep(1)
    option=input('Enter your option:  ').capitalize()
    if option=='Exit':
        time.sleep(1)
        print('Thanks for visiting')
        break
    if option=='Options':
        print('Select sentence length')
        time.sleep(1)
        print('Short')
        time.sleep(1)
        print('Long')
        selected_mode=input('Enter your answer: ').strip().capitalize()
        if selected_mode == 'Short' or selected_mode == 'Long':
            sentence_mode = selected_mode
            print(f'Sentence length set to {sentence_mode}')
        else:
           print('Invalid option. Keeping the current setting.')

    if option=='Play':
        while True:
            random_name=random_words(names)
            random_verbs=random_words(verbs)
            random_detail=random_words(details)
            random_place=random_words(places)
            random_time=random_words(Time)
            if selected_mode == 'Short':
                print(f'{random_name} {random_verbs} {random_detail}.')
            else:
                print(f'{random_name} {random_verbs} {random_detail} '
                      f'{random_place} {random_time}.')
            print('Would you like to generate a new sentence: ')
            answer=input('Y/N: ').capitalize()
            if answer=='N':
                break
