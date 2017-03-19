#Made by Wesley Vong
def hangpole():
    turtle.clear()
    turtle.up()
    turtle.setpos(-125,-100)
    turtle.setheading(0)
    turtle.down()
    turtle.right(120)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.right(30)
    turtle.fd(300)
    turtle.right(90)
    turtle.fd(210)
    turtle.right(90)
    turtle.fd(50)
def write(player):
    turtle.up()
    turtle.setpos(-250,-255)
    turtle.down()
    for i in player:
        turtle.down
        turtle.write(i, font = ('Arial', 20, "normal"))
        turtle.up()
        turtle.setheading(0)
        turtle.fd(20)
def man(tries):
    turtle.up()
    turtle.setpos(85,80)
    turtle.setheading(0)
    if (tries == 5):
        turtle.down()
        turtle.circle(35)
    if (tries == 4):
        turtle.down()
        turtle.right(90)
        turtle.fd(100)
    if (tries == 3):
        turtle.right(90)
        turtle.fd(40)
        turtle.right(120)
        turtle.down()
        turtle.fd(60)
    if (tries == 2):
        turtle.right(90)
        turtle.fd(40)
        turtle.left(120)
        turtle.down()
        turtle.fd(60)
    if (tries == 1):
        turtle.right(90)
        turtle.fd(100)
        turtle.right(60)
        turtle.down()
        turtle.fd(60)
    if (tries == 0):
        turtle.right(90)
        turtle.fd(100)
        turtle.left(60)
        turtle.down()
        turtle.fd(60)
def message(message):
    turtle.setpos(-250,230)
    turtle.write(message, font=('Arial', 30, 'bold'))
    time.sleep(2)
    turtle.undo()
def menu():
    turtle.up()
    turtle.setpos(-250,200)
    turtle.down
    turtle.write("Hangman", font=('Arial', 50, 'bold'))
    turtle.up
    turtle.setpos(-50,0)
    turtle.down
    turtle.write("Click here to Start", font=('Arial', 20, 'normal'))
def game(x,y):
    if ((x < 110 and x > -53) and (y < 22 and y > 2)):
        turtle.bgcolor('#ffff86')
        while (True):
            hangpole()
            word = str(turtle.textinput("Word","What word should it be? Leave Blank for Random"))
            if (word == ""):
                word = word_file[random.randint(1,len(word_file))]
            word = list(word.upper())
            tries = 6
            win = False
            match = False
            used = False
            player = []
            usedletter = []
            for i in word:
                if i != " ":
                    player.append("_")
                else:
                    player.append(" ")
            write(player)
            while (tries > 0):
                used = False
                a = 0
                letter = str(turtle.textinput("Letter","Guess a letter leave blank to guess word"))
                if (letter != ""):
                    letter = letter.upper()
                    if (len(letter) > 1):
                        message("Only 1 letter please")
                    elif (len(letter) == 1):
                        for i in usedletter:
                            if (letter == i):
                                message("letter already used")
                                used = True
                                break
                        if (used == False):
                            usedletter.append(letter)
                            match = False
                            for i in word:
                                if (letter == i):
                                    player[a] = i
                                    match = True
                                a = a + 1
                            if (match == False):
                                tries = tries - 1
                                man(tries)
                    usedword(usedletter)
                    write(player)
                elif (letter == ""):
                    players = str(turtle.textinput("Word","Guess the Word"))
                    players = players.upper()
                    players = list(players)
                    if (players != word):
                        tries = tries - 1
                        man(tries)
                    else:
                        player = players
                if (player == word):
                    win = True
                    message("You Win")
                    turtle.end_fill()
                    time.sleep(3)
                    break
            if (win == False):
                message("You Lose")
                write(word)
                turtle.end_fill()
                time.sleep(2)
def usedword(usedletter):
    turtle.up()
    turtle.setpos(-250,-225)
    turtle.down()
    for i in usedletter:
        turtle.down
        turtle.write(i, font = ('Arial', 16, "normal"))
        turtle.up()
        turtle.setheading(0)
        turtle.fd(20)
import time
import random
import turtle
wn = turtle.Screen()
word_file = open("1-10000.txt").read().splitlines()
turtle.color('purple','orange')
turtle.begin_fill()
turtle.pensize(5)
turtle.bgcolor('cyan')
turtle.speed(7)
begin = 0
menu()
turtle.onscreenclick(game)
wn.mainloop()
