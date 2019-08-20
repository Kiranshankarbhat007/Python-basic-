import random

words = ['mercedes','hummer','ford','porche','cadillac',
'mustang','bmw','lamborghini','mahindra','maruthi',
'kia','mg','chevrolet','audi','jeep','datsun',
'aston martin','bentley','bugatti','ferrari','fiat',
'honda','jagur','hyundai','land rover','lexus',
'maserati','manza','mclaren''mitsubishi','pagani',
'tata','tesla','suzuki','volvo','renault','rolls royce',
'volkswagen','nissan']

random.shuffle(words)
word = list(words[0])
# print word

display = []
display.extend(word)
# print display
print ('the word has',len(display),'length')

# display = '_'*len(word)
for i in range (len(word)):
    display[i] = '-'

print (' '.join(display))

count =0
while count <len(word):
    guess = raw_input("guess a letter: ")
    
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
            count = count +1
    print (' '.join(display))

print ("you gussed the word")
