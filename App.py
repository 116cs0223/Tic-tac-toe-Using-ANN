# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 08:21:33 2022

@author: SUBHAM SAHOO
"""

from tkinter import *
from tkinter import messagebox

root=Tk()

root.title('Subham:- Tic-Tac-Toe')
# tkinter window with dimensions 150x200
#root.geometry('1200x700')

player1_turn=True
count=0
good_move=True


def makeMoveGood():
    global good_move
    good_move=True

def makeMoveBad():
    global good_move
    good_move=False

# Change the label text
def show():
    label.config( text = clicked.get() )

def disableButtons():
    global b_list
    for btn in b_list:
        btn["state"]="disabled"
        


def colorButtons(indices,color):
    global b_list
    for i in indices:
        b_list[i]["bg"]=color
        
def checkWinner():
    global b_list, good_move
    b0_text=b_list[0]["text"]
    b1_text=b_list[1]["text"]
    b2_text=b_list[2]["text"]
    
    b3_text=b_list[3]["text"]
    b4_text=b_list[4]["text"]
    b5_text=b_list[5]["text"]
    
    b6_text=b_list[6]["text"]
    b7_text=b_list[7]["text"]
    b8_text=b_list[8]["text"]
    
    
    if(b0_text!=" " and b0_text==b1_text and b1_text==b2_text):
        colorButtons([0,1,2],'RED')
        messagebox.showinfo("Tic-Tac-Toe",b0_text+" Wins")
        disableButtons()
        
    elif(b3_text!=" " and b3_text==b4_text and b4_text==b5_text):
        colorButtons([3,4,5],'RED')
        messagebox.showinfo("Tic-Tac-Toe",b3_text+" Wins")
        disableButtons()
        
    elif(b6_text!=" " and b6_text==b7_text and b7_text==b8_text):
        colorButtons([6,7,8],'RED')
        messagebox.showinfo("Tic-Tac-Toe",b6_text+" Wins")
        disableButtons()
        
    elif(b0_text!=" " and b0_text==b3_text and b3_text==b6_text):
        colorButtons([0,3,6],'RED')
        messagebox.showinfo("Tic-Tac-Toe",b0_text+" Wins")
        disableButtons()
        
    elif(b1_text!=" " and b1_text==b4_text and b4_text==b7_text):
        colorButtons([1,4,7],'RED')
        messagebox.showinfo("Tic-Tac-Toe",b1_text+" Wins")
        disableButtons()
        
    elif(b2_text!=" " and b2_text==b5_text and b5_text==b8_text):
        colorButtons([2,5,8],'RED')
        messagebox.showinfo("Tic-Tac-Toe",b2_text+" Wins")
        disableButtons()
        
    elif(b0_text!=" " and b0_text==b4_text and b4_text==b8_text):
        colorButtons([0,4,8],'RED')
        messagebox.showinfo("Tic-Tac-Toe",b4_text+" Wins")
        disableButtons()
        
    elif(b2_text!=" " and b2_text==b4_text and b4_text==b6_text):
        colorButtons([2,4,6],'RED')
        messagebox.showinfo("Tic-Tac-Toe",b2_text+" Wins")
        disableButtons()
    
        
    

# funcntion when button is clicked
def btn_clicked(b):
    global player1_turn,count,b_list
    if(b["text"]==" " and player1_turn==True):
        b["text"]="X"
        player1_turn=False
        count+=1
        checkWinner()
    elif(b["text"]==" " and player1_turn==False):
        b["text"]="O"
        player1_turn=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("Tic-Tac-Toe","This box is already selected\n Pick another box")
    
    
    
    
# Start over the game!
def reset():
    global b_list
    global player1_turn,count
    global good_move
    player1_turn=True
    count=0
    good_move=True
    # Create game buttons
    b0 =  Button(root, name="b0", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b0)   )
    b1 =  Button(root, name="b1", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b1)   )
    b2 =  Button(root, name="b2", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b2)   )
    b3 =  Button(root, name="b3", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b3)   )
    b4 =  Button(root, name="b4", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b4)   )
    b5 =  Button(root, name="b5", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b5)   )
    b6 =  Button(root, name="b6", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b6)   )
    b7 =  Button(root, name="b7", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b7)   )
    b8 =  Button(root, name="b8", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: btn_clicked(b8)   )
    
    #Grid the buttons
    
    b0.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    
    b3.grid(row=1,column=0)
    b4.grid(row=1,column=1)
    b5.grid(row=1,column=2)
    
    b6.grid(row=2,column=0)
    b7.grid(row=2,column=1)
    b8.grid(row=2,column=2)
    
    b_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8]


reset()


# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Craete Oprions Menu
options_menu = Menu(my_menu, tearoff=False)
options_menu.add_command(label="Reset Game", command=reset)
my_menu.add_cascade(label="Options", menu=options_menu)

quality_menu = Menu(my_menu, tearoff=False)
quality_menu.add_cascade(label="Good Move", command=makeMoveGood)
quality_menu.add_cascade(label="Bad Move", command=makeMoveBad)
my_menu.add_cascade(label="MoveQuality", menu=quality_menu)


root.resizable(False, False)




#create a dropdown carriying goodmove and badmove options.
# Based on if it is a goodmove, we will write the data to dataset.

# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Monday" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )

root.mainloop()