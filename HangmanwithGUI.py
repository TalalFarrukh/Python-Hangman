# Hangman with graphics
from tkinter import *     #Module to make GUI

MW = Tk(); MW.title("Hang Man"); MW.geometry("800x500"); MW.configure(background='#FF7F27')
MFr = Frame(MW, width=800, height=500, background='white'); GS = Entry(MW, bg='white', fg='black', bd=3, relief= RAISED, width=10)
Quit = Button(MFr, text="Quit", bg='red', fg='black', font=("",10), relief='flat', width=10,height=2); Quit.place(x=0,y=450)

def erase(event):
    PlayB.destroy(); WM.destroy(); MFr.pack(); GS.place(x=200,y=270)

PlayB = Button(MW, text="Click here to start playing", bg='white', fg='black', font=("",20), relief='flat', width=20,height=2)
PlayB.place(x=225,y=150); PlayB.bind("<Button-1>", erase)
WM = Label(MW, text="Welcome to hangman", bg='white', fg='black', font=("",20), relief='flat', width=30, height=4); WM.place(x=150,y=0)

def quitgame(event):
    MW.destroy()

Quit.bind("<Button-1>", quitgame)

def GSS(event):
    mainstuff(GS.get())
    GS.delete(0, END)

GS.bind("<Return>", GSS)

import random  # To be used later in the code to pick up random elements from a set/tuple

LOW = ('heart', 'apple', 'circle', 'house', 'water', 'joker', 'bottle', 'song', 'comet', 'bell', 'test', 'cycle', 'late',
       'tree', 'table', 'tail', 'maths', 'report', 'game', 'artist')  # LOW = List Of Words

IN1 = Label(MFr,text="Instructions: ", anchor=W, fg='black', bg='white', width=60, height=2, font=("",10))
IN2 = Label(MFr,text="1. The aim of the game is to guess the word", anchor=W, fg='black', bg='white', width=60, height=1, font=("",10))
IN3 = Label(MFr,text="2. You have to guess the word letter by letter", anchor=W, fg='black', bg='white', width=60, height=2, font=("",10))
IN4 = Label(MFr,text="3. You will be given the hint for the word you have to guess", anchor=W, fg='black', bg='white', width=60, height=2, font=("",10))
IN5 = Label(MFr,text="4. For every wrong guess, you will lose a life", anchor=W, fg='black', bg='white', width=60, height=2, font=("",10))
IN6 = Label(MFr,text="5. You have six lives", fg='black', bg='white', anchor=W, width=60, height=2, font=("",10))
IN7 = Label(MFr,text="6. Guess the correct word to win the game", anchor=W, fg='black', bg='white', width=60, height=2, font=("",10))

IN1.place(x=0,y=0); IN2.place(x=0,y=30); IN3.place(x=0, y=60); IN4.place(x=0, y=90); IN5.place(x=0, y=120); IN6.place(x=0, y=150); IN7.place(x=0, y=180)

MD = Canvas(MFr, height=500, width=300, bg='white'); MD.place(x=500,y=0)     #Predefined figure
line1 = MD.create_line(220,200,220,400, width=5, fill='dark blue'); line2 = MD.create_line(180,400,260,400, width=5, fill='dark blue')
line3 = MD.create_line(222,200,180,200, width=5, fill='dark blue'); line4 = MD.create_line(180,199,180,220, width=5, fill='dark blue')

store = random.choice(LOW)  # Random element is selected and stored in the variable 'store'

if store == LOW[0]:
    Word1 = Label(MFr, text="Hint: central part of your body", fg='black', bg='white', width=60, height=2,
                  font=("", 10), anchor=W); Word1.place(x=10, y=230)
if store == LOW[1]:  # If the word selected randomly is the second element
    Word2 = Label(MFr, text="Hint: keeps the doctor away", fg='black', bg='white', width=60, height=2, font=("", 10),
                  anchor=W); Word2.place(x=10, y=230)
if store == LOW[2]:
    Word3 = Label(MFr, text="Hint: path you take on a round-about", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
    Word3.place(x=10, y=230)
if store == LOW[3]:  # If the word selected randomly is the first element
   Word4 = Label(MFr, text="Hint: a building for human habitation", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word4.place(x=10, y=230)
if store == LOW[4]:  # If the word selected randomly is the first element
   Word5 = Label(MFr, text="Hint: 60% of the human body", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word5.place(x=10, y=230)
if store == LOW[5]:  # If the word selected randomly is the first element
   Word6 = Label(MFr, text="Hint: Why so serious?", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word6.place(x=10, y=230)
if store == LOW[6]:  # If the word selected randomly is the first element
   Word7 = Label(MFr, text="Hint: a plastic container", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word7.place(x=10, y=230)
if store == LOW[7]:  # If the word selected randomly is the first element
   Word8 = Label(MFr, text="Hint: musical poem", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word8.place(x=10, y=230)
if store == LOW[8]:  # If the word selected randomly is the first element
   Word9 = Label(MFr, text="Hint: falling star", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word9.place(x=10, y=230)
if store == LOW[9]:  # If the word selected randomly is the first element
   Word10 = Label(MFr, text="Hint: a hollow metal object that makes a noise when struck", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word10.place(x=10, y=230)
if store == LOW[10]:  # If the word selected randomly is the first element
   Word11 = Label(MFr, text="Hint: a set of unanswered questions", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word11.place(x=10, y=230)
if store == LOW[11]:  # If the word selected randomly is the first element
   Word12 = Label(MFr, text="Hint: childhood vehicle", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word12.place(x=10, y=230)
if store == LOW[12]:  # If the word selected randomly is the first element
   Word13 = Label(MFr, text="Hint: doing something after the expected time", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word13.place(x=10, y=230)
if store == LOW[13]:  # If the word selected randomly is the first element
   Word14 = Label(MFr, text="Hint: a woody plant", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word14.place(x=10, y=230)
if store == LOW[14]:  # If the word selected randomly is the first element
   Word15 = Label(MFr, text="Hint: furniture with a flat top and four legs", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word15.place(x=10, y=230)
if store == LOW[15]:  # If the word selected randomly is the first element
   Word16 = Label(MFr, text="Hint: hindmost part of an animal", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word16.place(x=10, y=230)
if store == LOW[16]:  # If the word selected randomly is the first element
   Word17 = Label(MFr, text="Hint: calculations", fg='black', bg='white', width=60, height=2, font=("",10), anchor=W)
   Word17.place(x=10, y=230)
if store == LOW[17]:  # If the word selected randomly is the first element
    Word18 = Label(MFr, text="Hint: a piece of information supported by evidence", fg='black', bg='white', width=60,
                   height=2, font=("", 10), anchor=W); Word18.place(x=10, y=230)
if store == LOW[18]:  # If the word selected randomly is the first element
    Word19 = Label(MFr, text="Hint: fun activity", fg='black', bg='white', width=60, height=2, font=("", 10), anchor=W)
    Word19.place(x=10, y=230)
if store == LOW[19]:  # If the word selected randomly is the first element
    Word20 = Label(MFr, text="Hint: a person who creates paintings", fg='black', bg='white', width=60, height=2,
                   font=("", 10), anchor=W)
    Word20.place(x=10, y=230)

chances = 6; guess = 0
v1=v2=v3=v4=v5=0

def mainstuff(inp):
 Lose = Label(MFr, text="You have run out of lives!\nBetter luck next time!", fg='black', bg='red', width=30, height=5, font=50)
 Win = Label(MFr, text="Congratulations!\nYou have won the game!", fg='black', bg='green', width=30, height=5, font=50)
 global v1, v2, v3, v4, v5, chances, guess

 if store == LOW[0]:
    Word1_v1 = Label(MFr, text="h _ _ _ _", fg='black', bg='white', width=20, height=2, font=("", 10), anchor=W)
    Word1_v2 = Label(MFr, text="_ e _ _ _", fg='black', bg='white', width=20, height=2, font=("", 10), anchor=W)
    Word1_v3 = Label(MFr, text="_ _ a _ _", fg='black', bg='white', width=20, height=2, font=("", 10), anchor=W)
    Word1_v4 = Label(MFr, text="_ _ _ r _", fg='black', bg='white', width=20, height=2, font=("", 10), anchor=W)
    Word1_v5 = Label(MFr, text="_ _ _ _ t", fg='black', bg='white', width=20, height=2, font=("", 10), anchor=W)
 
    if inp == 'h' and v1 < 1:
            v1 += 1;
            Word1_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'e' and v2 < 1:
            v2 += 1;
            Word1_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'a' and v3 < 1:
            v3 += 1;
            Word1_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'r' and v4 < 1:
            v4 += 1;
            Word1_v4.place(x=10, y=350)
            guess += 1
    elif inp == 't' and v5 < 1:
            v5 += 1;
            Word1_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 
    elif guess == 5:
            Win.place(x=200,y=150);

 if store == LOW[1]:  # If the word selected randomly is the second element
    Word2_v1 = Label(MFr, text="a _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word2_v2 = Label(MFr, text="_ p p _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word2_v3 = Label(MFr, text="_ _ _ l _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word2_v4 = Label(MFr, text="_ _ _ _ e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
   
    if inp == 'a' and v1 < 1:
            v1 += 1;
            Word2_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'p' and v2 < 1:
            v2 += 1;
            Word2_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'l' and v3 < 1:
            v3 += 1;
            Word2_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'e' and v4 < 1:
            v4 += 1;
            Word2_v4.place(x=10, y=350)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150)

    elif guess == 4:
            Win.place(x=200,y=150)

 if store == LOW[2]:  # If the word selected randomly is the third element
    Word3_v1 = Label(MFr, text="c _ _ c _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word3_v2 = Label(MFr, text="_ i _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word3_v3 = Label(MFr, text="_ _ r _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word3_v4 = Label(MFr, text="_ _ _ _ l _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word3_v5 = Label(MFr, text="_ _ _ _ _ e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    
    if inp == 'c' and v1 < 1:
            v1 += 1;
            Word3_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'i' and v2 < 1:
            v2 += 1;
            Word3_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'r' and v3 < 1:
            v3 += 1;
            Word3_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'l' and v4 < 1:
            v4 += 1;
            Word3_v4.place(x=10, y=350)
            guess += 1
    elif inp == 'e' and v5 < 1:
            v5 += 1;
            Word3_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[3]:  # If the word selected randomly is the first element
    Word4_v1 = Label(MFr, text="h _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word4_v2 = Label(MFr, text="_ o _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word4_v3 = Label(MFr, text="_ _ u _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word4_v4 = Label(MFr, text="_ _ _ s _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word4_v5 = Label(MFr, text="_ _ _ _ e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'h' and v1 < 1:
            v1 += 1;
            Word4_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'o' and v2 < 1:
            v2 += 1;
            Word4_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'u' and v3 < 1:
            v3 += 1;
            Word4_v3.place(x=10, y=320)
            guess += 1
    elif inp == 's' and v4 < 1:
            v4 += 1;
            Word4_v4.place(x=10, y=350)
            guess += 1
    elif inp == 'e' and v5 < 1:
            v5 += 1;
            Word4_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[4]:  # If the word selected randomly is the first element
    Word5_v1 = Label(MFr, text="w _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word5_v2 = Label(MFr, text="_ a _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word5_v3 = Label(MFr, text="_ _ t _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word5_v4 = Label(MFr, text="_ _ _ e _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word5_v5 = Label(MFr, text="_ _ _ _ r", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'w' and v1 < 1:
            v1 += 1;
            Word5_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'a' and v2 < 1:
            v2 += 1;
            Word5_v2.place(x=10, y=290)
            guess += 1
    elif inp == 't' and v3 < 1:
            v3 += 1;
            Word5_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'e' and v4 < 1:
            v4 += 1;
            Word5_v4.place(x=10, y=350)
            guess += 1
    elif inp == 'r' and v5 < 1:
            v5 += 1;
            Word5_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[5]:  # If the word selected randomly is the first element
    Word6_v1 = Label(MFr, text="j _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word6_v2 = Label(MFr, text="_ o _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word6_v3 = Label(MFr, text="_ _ k _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word6_v4 = Label(MFr, text="_ _ _ e _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word6_v5 = Label(MFr, text="_ _ _ _ r", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'j' and v1 < 1:
            v1 += 1;
            Word6_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'o' and v2 < 1:
            v2 += 1;
            Word6_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'k' and v3 < 1:
            v3 += 1;
            Word6_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'e' and v4 < 1:
            v4 += 1;
            Word6_v4.place(x=10, y=350)
            guess += 1
    elif inp == 'r' and v5 < 1:
            v5 += 1;
            Word6_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[6]:  # If the word selected randomly is the first element
    Word7_v1 = Label(MFr, text="b _ _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word7_v2 = Label(MFr, text="_ o _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word7_v3 = Label(MFr, text="_ _ t t _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word7_v4 = Label(MFr, text="_ _ _ _ l _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word7_v5 = Label(MFr, text="_ _ _ _ _ e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'b' and v1 < 1:
            v1 += 1;
            Word7_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'o' and v2 < 1:
            v2 += 1;
            Word7_v2.place(x=10, y=290)
            guess += 1
    elif inp == 't' and v3 < 1:
            v3 += 1;
            Word7_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'l' and v4 < 1:
            v4 += 1;
            Word7_v4.place(x=10, y=350)
            guess += 1
    elif inp == 'e' and v5 < 1:
            v5 += 1;
            Word7_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[7]:  # If the word selected randomly is the first element
    Word8_v1 = Label(MFr, text="s _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word8_v2 = Label(MFr, text="_ o _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word8_v3 = Label(MFr, text="_ _ n _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word8_v4 = Label(MFr, text="_ _ _ g", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 's' and v1 < 1:
            v1 += 1;
            Word8_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'o' and v2 < 1:
            v2 += 1;
            Word8_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'n' and v3 < 1:
            v3 += 1;
            Word8_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'g' and v4 < 1:
            v4 += 1;
            Word8_v4.place(x=10, y=350)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 4:
            Win.place(x=200,y=150); 

 if store == LOW[8]:  # If the word selected randomly is the first element
    Word9_v1 = Label(MFr, text="c _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word9_v2 = Label(MFr, text="_ o _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word9_v3 = Label(MFr, text="_ _ m _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word9_v4 = Label(MFr, text="_ _ _ e _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word9_v5 = Label(MFr, text="_ _ _ _ t", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'c' and v1 < 1:
            v1 += 1;
            Word9_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'o' and v2 < 1:
            v2 += 1;
            Word9_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'm' and v3 < 1:
            v3 += 1;
            Word9_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'e' and v4 < 1:
            v4 += 1;
            Word9_v4.place(x=10, y=350)
            guess += 1
    elif inp == 't' and v5 < 1:
            v5 += 1;
            Word9_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[9]:  # If the word selected randomly is the first element
    Word10_v1 = Label(MFr, text="b _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word10_v2 = Label(MFr, text="_ e _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word10_v3 = Label(MFr, text="_ _ l l", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'b' and v1 < 1:
            v1 += 1;
            Word10_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'e' and v2 < 1:
            v2 += 1;
            Word10_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'l' and v3 < 1:
            v3 += 1;
            Word10_v3.place(x=10, y=320)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 3:
            Win.place(x=200,y=150); 

 if store == LOW[10]:  # If the word selected randomly is the first element
    Word11_v1 = Label(MFr, text="t _ _ t", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word11_v2 = Label(MFr, text="_ e _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word11_v3 = Label(MFr, text="_ _ s _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 't' and v1 < 1:
            v1 += 1;
            Word11_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'e' and v2 < 1:
            v2 += 1;
            Word11_v2.place(x=10, y=290)
            guess += 1
    elif inp == 's' and v3 < 1:
            v3 += 1;
            Word11_v3.place(x=10, y=320)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 3:
            Win.place(x=200,y=150); 

 if store == LOW[11]:  # If the word selected randomly is the first element
    Word12_v1 = Label(MFr, text="c _ c _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word12_v2 = Label(MFr, text="_ y _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word12_v3 = Label(MFr, text="_ _ _ l _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word12_v4 = Label(MFr, text="_ _ _ _ e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'c' and v1 < 1:
            v1 += 1;
            Word12_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'y' and v2 < 1:
            v2 += 1;
            Word12_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'l' and v3 < 1:
            v3 += 1;
            Word12_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'e' and v4 < 1:
            v4 += 1;
            Word12_v4.place(x=10, y=350)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 4:
            Win.place(x=200,y=150); 

 if store == LOW[12]:  # If the word selected randomly is the first element
    Word13_v1 = Label(MFr, text="l _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word13_v2 = Label(MFr, text="_ a _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word13_v3 = Label(MFr, text="_ _ t _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word13_v4 = Label(MFr, text="_ _ _ e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'l' and v1 < 1:
            v1 += 1;
            Word13_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'a' and v2 < 1:
            v2 += 1;
            Word13_v2.place(x=10, y=290)
            guess += 1
    elif inp == 't' and v3 < 1:
            v3 += 1;
            Word13_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'e' and v4 < 1:
            v4 += 1;
            Word13_v4.place(x=10, y=350)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 4:
            Win.place(x=200,y=150); 

 if store == LOW[13]:  # If the word selected randomly is the first element
    Word14_v1 = Label(MFr, text="t _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word14_v2 = Label(MFr, text="_ r _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word14_v3 = Label(MFr, text="_ _ e e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 't' and v1 < 1:
            v1 += 1;
            Word14_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'r' and v2 < 1:
            v2 += 1;
            Word14_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'e' and v3 < 1:
            v3 += 1;
            Word14_v3.place(x=10, y=320)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 3:
            Win.place(x=200,y=150); 

 if store == LOW[14]:  # If the word selected randomly is the first element
    Word15_v1 = Label(MFr, text="t _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word15_v2 = Label(MFr, text="_ a _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word15_v3 = Label(MFr, text="_ _ b _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word15_v4 = Label(MFr, text="_ _ _ l _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word15_v5 = Label(MFr, text="_ _ _ _ e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 't' and v1 < 1:
            v1 += 1;
            Word15_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'a' and v2 < 1:
            v2 += 1;
            Word15_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'b' and v3 < 1:
            v3 += 1;
            Word15_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'l' and v4 < 1:
            v4 += 1;
            Word15_v4.place(x=10, y=350)
            guess += 1
    elif inp == 'e' and v5 < 1:
            v5 += 1;
            Word15_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[15]:  # If the word selected randomly is the first element
    Word16_v1 = Label(MFr, text="t _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word16_v2 = Label(MFr, text="_ a _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word16_v3 = Label(MFr, text="_ _ i _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word16_v4 = Label(MFr, text="_ _ _ l", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 't' and v1 < 1:
            v1 += 1;
            Word16_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'a' and v2 < 1:
            v2 += 1;
            Word16_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'i' and v3 < 1:
            v3 += 1;
            Word16_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'l' and v4 < 1:
            v4 += 1;
            Word16_v4.place(x=10, y=350)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 4:
            Win.place(x=200,y=150); 

 if store == LOW[16]:  # If the word selected randomly is the first element
    Word17_v1 = Label(MFr, text="m _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word17_v2 = Label(MFr, text="_ a _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word17_v3 = Label(MFr, text="_ _ t _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word17_v4 = Label(MFr, text="_ _ _ h _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word17_v5 = Label(MFr, text="_ _ _ _ s", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'm' and v1 < 1:
            v1 += 1;
            Word17_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'a' and v2 < 1:
            v2 += 1;
            Word17_v2.place(x=10, y=290)
            guess += 1
    elif inp == 't' and v3 < 1:
            v3 += 1;
            Word17_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'h' and v4 < 1:
            v4 += 1;
            Word17_v4.place(x=10, y=350)
            guess += 1
    elif inp == 's' and v5 < 1:
            v5 += 1;
            Word17_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[17]:  # If the word selected randomly is the first element
    Word18_v1 = Label(MFr, text="r _ _ _ r _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word18_v2 = Label(MFr, text="_ e _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word18_v3 = Label(MFr, text="_ _ p _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word18_v4 = Label(MFr, text="_ _ _ o _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word18_v5 = Label(MFr, text="_ _ _ _ _ t", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'r' and v1 < 1:
            v1 += 1;
            Word18_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'e' and v2 < 1:
            v2 += 1;
            Word18_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'p' and v3 < 1:
            v3 += 1;
            Word18_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'o' and v4 <1:
            v4 +=1;
            Word18_v4.place(x=10, y=350)
            guess +=1
    elif inp == 't' and v5 < 1:
            v5 += 1;
            Word18_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 5:
            Win.place(x=200,y=150); 

 if store == LOW[18]:  # If the word selected randomly is the first element
    Word19_v1 = Label(MFr, text="g _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word19_v2 = Label(MFr, text="_ a _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word19_v3 = Label(MFr, text="_ _ m _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word19_v4 = Label(MFr, text="_ _ _ e", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'g' and v1 < 1:
            v1 += 1;
            Word19_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'a' and v2 < 1:
            v2 += 1;
            Word19_v2.place(x=10, y=290)
            guess += 1
    elif inp == 'm' and v3 < 1:
            v3 += 1;
            Word19_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'e' and v4 < 1:
            v4 += 1;
            Word19_v4.place(x=10, y=350)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')

    if chances == 0:
            Lose.place(x=200,y=150); 

    elif guess == 4:
            Win.place(x=200,y=150); 

 if store == LOW[19]:  # If the word selected randomly is the first element
    Word20_v1 = Label(MFr, text="a _ _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word20_v2 = Label(MFr, text="_ r _ _ _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word20_v3 = Label(MFr, text="_ _ t _ _ t", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word20_v4 = Label(MFr, text="_ _ _ i _ _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)
    Word20_v5 = Label(MFr, text="_ _ _ _ s _", fg='black', bg='white', width=20, height=2, font=("",10), anchor=W)

    if inp == 'a' and v1 < 1:
            v1 += 1;
            Word20_v1.place(x=10, y=260)
            guess += 1
    elif inp == 'r' and v2 < 1:
            v2 += 1;
            Word20_v2.place(x=10, y=290)
            guess += 1
    elif inp == 't' and v3 < 1:
            v3 += 1;
            Word20_v3.place(x=10, y=320)
            guess += 1
    elif inp == 'i' and v4 < 1:
            v4 += 1;
            Word20_v4.place(x=10, y=350)
            guess += 1
    elif inp == 's' and v5 < 1:
            v5 += 1;
            Word20_v5.place(x=10, y=380)
            guess += 1
    else:
            chances -= 1
            if chances == 5:
                MD.create_oval(160, 220, 200, 260, width=3, fill='red', outline='dark blue')
            elif chances == 4:
                MD.create_line(180, 260, 180, 350, width=3, fill='red')
            elif chances == 3:
                MD.create_line(180, 260, 210, 305, width=3, fill='red')
            elif chances == 2:
                MD.create_line(180, 260, 150, 305, width=3, fill='red')
            elif chances == 1:
                MD.create_line(180, 350, 210, 370, width=3, fill='red')
            elif chances == 0:
                MD.create_line(180, 350, 150, 370, width=3, fill='red')
            
    if chances == 0:
         Lose.place(x=200,y=150)

    elif guess == 5:
         Win.place(x=200,y=150)

MW.mainloop()