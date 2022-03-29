# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:44:33 2022

@author: SUBHAM SAHOO
"""

from tkinter import *
from tkinter import messagebox

class TicTocToe(Tk):
    player1_turn=True
    count=0
    good_move=True
    b_list=[]

    def makeMoveGood(self):
        self.good_move=True
        self.app_menulists.entryconfigure(2, label="Good Move")
    
    def makeMoveBad(self):
        self.good_move=False
        self.app_menulists.entryconfigure(2, label="Bad Move")
        
    def disableButtons(self):
        for btn in self.b_list:
            btn["state"]="disabled"
        
    def colorButtons(self,indices,color):
        for i in indices:
            self.b_list[i]["bg"]=color
    
    def checkWinner(self):
        
        b0_text=self.b_list[0]["text"]
        b1_text=self.b_list[1]["text"]
        b2_text=self.b_list[2]["text"]
        
        b3_text=self.b_list[3]["text"]
        b4_text=self.b_list[4]["text"]
        b5_text=self.b_list[5]["text"]
        
        b6_text=self.b_list[6]["text"]
        b7_text=self.b_list[7]["text"]
        b8_text=self.b_list[8]["text"]
        
        
        if(b0_text!=" " and b0_text==b1_text and b1_text==b2_text):
            self.colorButtons([0,1,2],'RED')
            messagebox.showinfo("Tic-Tac-Toe",b0_text+" Wins")
            self.disableButtons()
            
        elif(b3_text!=" " and b3_text==b4_text and b4_text==b5_text):
            self.colorButtons([3,4,5],'RED')
            messagebox.showinfo("Tic-Tac-Toe",b3_text+" Wins")
            self.disableButtons()
            
        elif(b6_text!=" " and b6_text==b7_text and b7_text==b8_text):
            self.colorButtons([6,7,8],'RED')
            messagebox.showinfo("Tic-Tac-Toe",b6_text+" Wins")
            self.disableButtons()
            
        elif(b0_text!=" " and b0_text==b3_text and b3_text==b6_text):
            self.colorButtons([0,3,6],'RED')
            messagebox.showinfo("Tic-Tac-Toe",b0_text+" Wins")
            self.disableButtons()
            
        elif(b1_text!=" " and b1_text==b4_text and b4_text==b7_text):
            self.colorButtons([1,4,7],'RED')
            messagebox.showinfo("Tic-Tac-Toe",b1_text+" Wins")
            self.disableButtons()
            
        elif(b2_text!=" " and b2_text==b5_text and b5_text==b8_text):
            self.colorButtons([2,5,8],'RED')
            messagebox.showinfo("Tic-Tac-Toe",b2_text+" Wins")
            self.disableButtons()
            
        elif(b0_text!=" " and b0_text==b4_text and b4_text==b8_text):
            self.colorButtons([0,4,8],'RED')
            messagebox.showinfo("Tic-Tac-Toe",b4_text+" Wins")
            self.disableButtons()
            
        elif(b2_text!=" " and b2_text==b4_text and b4_text==b6_text):
            self.colorButtons([2,4,6],'RED')
            messagebox.showinfo("Tic-Tac-Toe",b2_text+" Wins")
            self.disableButtons()
        elif(self.count==9):
            self.colorButtons([0,1,2,3,4,5,6,7,8],'BLUE')
            messagebox.showinfo("Tic-Tac-Toe","No one wins!")
            self.disableButtons()

    
    # funcntion when button is clicked
    def btn_clicked(self,b):
        if(b["text"]==" " and self.player1_turn==True):
            b["text"]="X"
            self.player1_turn=False
            self.count+=1
            self.checkWinner()
            
        elif(b["text"]==" " and self.player1_turn==False):
            b["text"]="O"
            self.player1_turn=True
            self.count+=1
            self.checkWinner()
            
        else:
            messagebox.showerror("Tic-Tac-Toe","This box is already selected\n Pick another box")
    
    # Start over the game!
    def reset(self):
        
        self.player1_turn=True
        self.count=0
        self.good_move=True
        # Create game buttons
        # Create game buttons
        b0 =  Button(self, name="b0", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b0)   )
        b1 =  Button(self, name="b1", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b1)   )
        b2 =  Button(self, name="b2", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b2)   )
        b3 =  Button(self, name="b3", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b3)   )
        b4 =  Button(self, name="b4", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b4)   )
        b5 =  Button(self, name="b5", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b5)   )
        b6 =  Button(self, name="b6", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b6)   )
        b7 =  Button(self, name="b7", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b7)   )
        b8 =  Button(self, name="b8", text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.btn_clicked(b8)   )
        
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
        
        self.b_list=[b0,b1,b2,b3,b4,b5,b6,b7,b8]
    
    
    # The init method or constructor
    def __init__(self):
        super().__init__()
        self.reset()
        
        
        # Create menu
        self.app_menulists = Menu(self)
        self.config(menu=self.app_menulists)
        
        #Craete Oprions Menu
        self.reset_game__menu = Menu(self.app_menulists, tearoff=False)
        self.reset_game__menu.add_command(label="Reset Game", command=self.reset)
        self.app_menulists.add_cascade(label="Options", menu=self.reset_game__menu)
        
        self.quality_menu = Menu(self.app_menulists, tearoff=False)
        self.quality_menu.add_cascade(label="Good Move", command=self.makeMoveGood)
        self.quality_menu.add_cascade(label="Bad Move", command=self.makeMoveBad)
        self.app_menulists.add_cascade(label="Good Move", menu=self.quality_menu)
        
          
        
   

root = TicTocToe()
root.title('Subham:- Tic-Tac-Toe')
root.resizable(False, False)
root.mainloop()