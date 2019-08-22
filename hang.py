import random

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

# random.shuffle(words)
# word = word[0]
word = random.choice(words)

gwords = []
display = []
display.extend(word)
print 'the word has',len(display),'letter'

for i in range (len(word)):
    display[i] = '-'

print (' '.join(display))

count =0
while count <len(word):

    guess = raw_input("guess a letter: ")
    if guess not in gwords:
        gwords.append(guess)
        print (gwords)
    else:
        print "u already guessed the letter"
        print (gwords)
    
    if guess not in display:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
                count = count +1
    
    print (' '.join(display))
print ("you gussed the word")
