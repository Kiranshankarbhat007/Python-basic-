import random

def selection():
    # word = ['mercedes','hummer','ford','porche','cadillac',
    # 'mustang','bmw','lamborghini','mahindra','maruthi',
    # 'kia','mg','chevrolet','audi','jeep','datsun',
    # 'astonmartin','bentley','bugatti','ferrari','fiat',
    # 'honda','jagur','hyundai','landrover','lexus',
    # 'maserati','manza','mclaren','mitsubishi','pagani',
    # 'tata','tesla','suzuki','volvo','renault','rollsroyce',
    # 'volkswagen','nissan']

    with open("../../Downloads/words.txt") as f:
        words = f.read()
        word = words.split(" ")

    # random.shuffle(words)
    # word = word[0]
    word = random.choice(word)
    return word
word = selection()


def hang(word):
    print word
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

    chance = 0
    count = 0
    no_of_chance = 5
    f = no_of_chance
    
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
            print (gwords)
    
        if guess not in display:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
                    count = count +1
            print (' '.join(display))

            if guess in display:
                pass
            else:
                chance = chance +1
                f = f-1
                print 'your guess is wrong'
                print 'you have',f,'chance' 
                        
        if chance == no_of_chance:
            # print "your chancecs are over"
            print " YOU LOST THE GAME "
            break
    else:
        print (" YOU WON THE GAME ")
    
hang(word)