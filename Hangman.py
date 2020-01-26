import random
class hangman ():
    def __init__(self):
        
        self.words = "word worm cold duck beautiful smart stupid ugly fam fat"

        self.l_w = words.split()
        
        self.missed = 0
        
        
    def load_random(self):
        
        return self.l_w[random.randint(0,len(self.l_w)-1)]
    
    
    
    def generate (self, word):
        
        return ["_*_"]*len(word)
    def check_word (self,word ,guess,guessed):
        
        if len(guess)!= 1 or guess not in word :
            self.missed += 1 
            print("Wrong Guess")
            
            return False , guessed ,word
        
        for i in range(len(word)) :
            if guess == word[i]:
                guessed[i] = guess
                temp = word[:i]
                word = word[i+1:]
                word = temp+"*"+word
                
               
                
                print("your Guess is right")
                
                return True ,guessed ,word 
                
        
        
    def start (self):
        word = self.load_random()
        guessed = self.generate(word)
        print(word)
        
        right = 0
        
        
        
        while self.missed<8 :
            guess = input("Enter a random Guess \n")
            
            check , guessed,word = self.check_word(word,guess,guessed)
            print(guessed)
            print("faliures = {}".format(self.missed))
            
            if check :
                right += 1 
                
            if right == len(word) :
                print("you won !!")
                break
                
                
        if self.missed == 8 :
            
            print("you lost")
        
        
        
        
        
        
hangman().start()        
        