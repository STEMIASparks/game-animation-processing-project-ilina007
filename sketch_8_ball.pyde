import random
import string
#allows the code to randomly generate a string
print("Welcome to Magic 8 Ball")
#introduction to the game

def setup():
    size(600,600)
    background(220,220,220)


def draw():
    circle(300,300,300)
    fill(128)
    #circle design
    text("Magic 8 Ball says...", 180,310,300)
    #ball design
    textSize(30)
    fill(0)

    
    
def input(messages=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog("Ask a Yes or No question") 
user_message = input("type in something")
#user input box which allows users to input information
#user_message can be used to print the user input




print("You asked " +user_message)
#shows what the players asked

letters = ["yes", "no", "maybe", "no way", "I dont think so", "tough chance", "it is certain",
"It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it, yes",
"Most likely","Signs point to yes", "That will always remain unanswerd","be realistic", "Those expectations are too high"]
#list of all possible responses

print ( ''.join(random.choice(letters) for i in range(1)) )
#choses a random repsonse
