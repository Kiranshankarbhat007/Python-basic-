import random

def selection():
    words = ['mercedes','hummer','ford','porche','cadillac',
    'mustang','bmw','lamborghini','mahindra','maruthi',
    'kia','mg','chevrolet','audi','jeep','datsun',
    'astonmartin','bentley','bugatti','ferrari','fiat',
    'honda','jagur','hyundai','landrover','lexus',
    'maserati','manza','mclaren','mitsubishi','pagani',
    'tata','tesla','suzuki','volvo','renault','rollsroyce',
    'volkswagen','nissan']

# with open("../../Downloads/words.txt") as f:
#     words = f.read()
#     word = words.split(" ")
    # print word

    # random.shuffle(words)
    # word = word[0]
    word = random.choice(words)
    return word
word = selection()
# print word

def hang(word):
    alpha = ['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z']
    gwords = []
    display = []
    display.extend(word)
    print ('the word has',len(display),'letter')

    for i in range (len(word)):
        display[i] = '-'

    print (' '.join(display))

    count =0
    while count <len(word):
        
        guess = raw_input("Enter your guess: ")
        guess = guess.lower()
        if guess in alpha:
            if guess not in gwords:
                gwords.append(guess)
                print (gwords)
            else:
                print ("u already guessed the letter")
                print (gwords)
        else:
            print ('Entered guess is invalid')
    
        if guess not in display:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
                    count = count +1
    
        print (' '.join(display))
    print ("you gussed the word")
hang(word)

