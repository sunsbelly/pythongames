import random
sliced = ['''


  O   
 /|\  
 / \ 
     

        ''', '''

    
  O   
 /|\  
 / 

       
      
        ''', '''

  

  O   
 /|\  
      
     
     
      
        ''', '''

  
  
  O   
 /|   
      
      
        ''', '''

  
  
  O   
  |    
      
        ''', '''

  
     
  O   

 
      
            ''']
lister = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


slicer = ["He still has a full body!", "You cut off his right leg",  "You cut off his left left leg!", "You cut off his right arm!", "You cut off his arm arm!", "You cut off his torso! he's dead!"] 
guessed = ""
rand = random.choice(lister)
alreadyGuessed = ''
missedLetters = ""
correctLetters = ""
missedLettersNum = 0

print "    **SliceMan**"
print "A variation of HangMan"
print "-" * 22
print "-" * 22
print "Guess this mystery word: "
blanks = "_" * len(rand)
blankslist = list(blanks)
emp3 = " ".join(blankslist)
print emp3
print
print "Fill in the blanks letter by letter, "
print "before the executioner gets to the head"
print
print rand

def alreadyGuesser(guessed):
    alreadyGuessed += guessed
    return    

def getGuess(): #this returns the letter that the player chooses
    while True:
        print
        print "Please guess a letter:"
        global alreadyGuessed
        global missedLetters
        global correctLetters
        global missedLettersNum
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print
            print "please enter a SINGLE letter"
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print
            print "Please enter a LETTER."    
        elif guess in alreadyGuessed:
            
            if guess in rand:
                print True
                return guess
            print
            print "you already guessed that"
            print
        elif guess not in rand:
            print
            print "not in word"
            print
            missedLetters += guess
            missedLettersNum += 1
            alreadyGuessed += guess
            return guess
        
        else:
            alreadyGuessed += guess
            correctLetters += guess
            return guess
 
while True:
    print
    print
    print "This is what you guessed so far: "
    print
    for i in blankslist:
        print i,
    print
    print
    print "Missed letters: " + missedLetters
    print "Correct letters: " + correctLetters
    print "already guessed: " + alreadyGuessed
    z = getGuess()
    for i in range(len(rand)):
        for d in range(len(blankslist)):
            if z == rand[i]:
                blankslist[i] = rand[i]    
    for i in blankslist:
        print i,  
    print
    print
    print slicer[missedLettersNum]
    print sliced[missedLettersNum]
    print 
   
    rightWord= "".join(blankslist)
    if rightWord == rand:
        print "You Win!!!"
        print 
        break
    if len(missedLetters) == len(slicer)-1:
        print "You lose!!"
        break
    


