from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Scissor Paper Game")
root.configure(background="#29465B")
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))
u_label = Label(root, image=scissor_img, bg="#29465B")
c_label = Label(root, image=scissor_img_comp, bg="#29465B")
c_label.grid(row=2, column=0)
u_label.grid(row=2, column=2)
p_Score = Label(root, text=0, font=100, bg="#29465B", fg="white")
c_Score = Label(root, text=0, font=100, bg="#29465B", fg="white")
c_Score.grid(row=3, column=0)
p_Score.grid(row=3,column=2)
user_indicator = Label(root, font=50, text="USER", bg="#29465B", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",bg="#29465B", fg="white")
user_indicator.grid(row=0, column=2)
comp_indicator.grid(row=0, column=0)
msg = Label(root, font=50, bg="#29465B", fg="white")
msg.grid(row=2, column=1)
def updateMessage(x):
    msg['text'] = x
def updateUserScore():
    score = int(p_Score["text"])
    score += 1
    p_Score["text"] = str(score)
def updateCompScore():
    score = int(c_Score["text"])
    score += 1
    c_Score["text"] = str(score)
def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lost the game")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lost the game")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lost the game")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass
choices = ["rock", "paper", "scissor"]

def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        c_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        c_label.configure(image=paper_img_comp)
    else:
        c_label.configure(image=scissor_img_comp)
    if x == "rock":
        u_label.configure(image=rock_img)
    elif x == "paper":
        u_label.configure(image=paper_img)
    else:
        u_label.configure(image=scissor_img)

    checkWin(x, compChoice)
rock = Button(root, width=30, height=2, text="ROCK",
              bg="#808080", fg="white", command=lambda: updateChoice("rock")).grid(row=5, column=0)
paper = Button(root, width=30, height=2, text="PAPER",
               bg="#808080", fg="white", command=lambda: updateChoice("paper")).grid(row=5, column=1)
scissor = Button(root, width=30, height=2, text="SCISSOR",
                 bg="#808080", fg="white", command=lambda: updateChoice("scissor")).grid(row=5, column=2)

root.mainloop()