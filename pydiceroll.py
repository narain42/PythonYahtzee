import tkinter as tk  
import random
from tkinter import messagebox
from tkinter import *
import sys
from tkinter import simpledialog

def setTable():

        global tbl
## table set up for scoring. row 0 and col 0 for headers
        tbl.set(0,0,"Game")
        tbl.set(0,1,"User1")
        tbl.set(0,2,"User2")
        tbl.set(0,3,"User3")
        tbl.set(0,4,"User4")
        tbl.set(1,0,"One")
        tbl.set(2,0,"Two")
        tbl.set(3,0,"Three")
        tbl.set(4,0,"Four")
        tbl.set(5,0,"Five")
        tbl.set(6,0,"Six")
        tbl.set(7,0,"Bonus")
        tbl.set(8,0,"3 of a kind")
        tbl.set(9, 0,"4 of a kind")
        tbl.set(10,0,"Full House")
        tbl.set(11,0,"Small Straight")
        tbl.set(12,0,"Large Straight")
        tbl.set(13,0,"Chance")
        tbl.set(14,0,"Yahtzee")
        tbl.set(15,0,"Top Sub Total")
        tbl.set(16,0,"Lower Sub Total")
        tbl.set(17,0,"Total")
        tbl.set(18,0,"Best Score")
        tbl.set(19,0,"Score Option")
        

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=20, columns=5):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                ent = Entry(self)
                ent.insert(0, "0")
                ent.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(ent)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.delete(0,END)
        widget.insert(0, value)
        
        
    def get(self, row, column, value):
        widget = self._widgets[row][column]
        value = widget.get()
        return value


    def reset(self, rows, column, value):
        for row in range(rows):
               widget = self._widgets[row][column]
               widget.delete(0,END)
               widget.insert(0, value)

# Class Definitions

class Dice(object):
    def __init__(self):
        self.dice = [0,0,0,0,0]
        self.roll_counter = 0
        self.held = []
        self.message = ''


    def reset(self):
        self.__init__()
        
    def hold(self, keepers):
        for die in keepers:
            if die in self.held:
                self.held.remove(die)
            else:
                self.held.append(die)


    def roll(self):
        self.roll_counter += 1
        for die in range(1,6):
            if str(die) in self.held:
                pass
            else:
                self.dice[die] = str(random.randint(1,6))

    def total(self):
        dice_total = 0
        for die in dice.dice:
            dice_total += int(die)
        return dice_total

class Score(object):
    
    def __init__(self):
        self.dict = createDefaultDict()

    def total(self):
        total = 0
        for item in self.dict.values():
            total += item
        return total

    def update(self, row, new_score):
        self.dict[row] = new_score

    def bonus_check(self):
        top_total = 0
        for i in range(1,7):
            top_total += self.dict[str(i)]
        
        if top_total >= 63:
            self.dict['bon'] = 35
            

def do_nothing():
                """ do nothing """



def click():

                dice_roll()

def dice_pics():

                 global rnx, clmn

                 if rnx == 1:
                     img = tk.PhotoImage(file="11.png")
                     pnx1 = tk.Label(root, image = img)
                     pnx1.image = img
                     pnx1.grid(row=1, column=clmn, pady=2)
                 elif rnx == 2:
                     img = tk.PhotoImage(file="21.png")
                     pnx2 = tk.Label(root, image = img)
                     pnx2.image = img
                     pnx2.grid(row=1, column=clmn, pady=2)
                 elif rnx == 3:
                     img = tk.PhotoImage(file="31.png")
                     pnx3 = Label(root, image = img)
                     pnx3.image = img
                     pnx3.grid(row=1, column=clmn, pady=2)
                 elif rnx == 4:
                     img = tk.PhotoImage(file="41.png")
                     pnx4 = Label(root, image = img)
                     pnx4.image = img
                     pnx4.grid(row=1, column=clmn, pady=2)
                 elif rnx == 5:
                     img = tk.PhotoImage(file="51.png")
                     pnx5 = Label(root, image = img)
                     pnx5.image = img
                     pnx5.grid(row=1, column=clmn, pady=2)
                 elif rnx == 6:
                     img = tk.PhotoImage(file="61.png")
                     pnx6 = Label(root, image = img)
                     pnx6.image = img
                     pnx6.grid(row=1, column=clmn, pady=2)
                   
                   
                                 
def dice_roll():
                """
                display a randomly selected dice value
                """
                global x
                global pcol
                global rolls
                global numx, tnum
                global rowUsed
                global rows_to_check
                global rnx, clmn
                
##  x is number of dice throw. t is arbitrary time               
                t = 2
                root.title("Yahtzee Rolls") 
                x = x + 1    
                rnx = 0
                numx = [0,0,0,0,0]
                tnum = 0
                
                if cvar1.get() == 0:
                   y = random.randint(1,6)
                   rnx = y
                   clmn = 0
                   dice_pics()
                   var1.set(str(y))
                   dice.dice[0] = (y)
                                            
                if cvar2.get() == 0:
                   z = random.randint(1,6)
                   rnx = z
                   clmn = 1
                   dice_pics()
                   var2.set(str(z))
                   dice.dice[1] = (z)
                      
                if cvar3.get() == 0:                   
                   z1 = random.randint(1,6)
                   rnx = z1
                   clmn = 2
                   dice_pics()
                   var3.set(str(z1))
                   dice.dice[2] = (z1)
                    
                if cvar4.get() == 0:
                   z2 = random.randint(1,6)
                   rnx = z2
                   clmn = 3
                   dice_pics()
                   var4.set(str(z2))
                   dice.dice[3] = (z2)

                if cvar5.get() == 0:                    
                   z3 = random.randint(1,6)
                   rnx = z3
                   clmn = 4
                   dice_pics()
                   var5.set(str(z3))
                   dice.dice[4] = (z3)

                root.update()
                root.after(t, do_nothing)   
                   
                var.set("throw" + " " + str(x))
                   
                     
                if x == 3:
                   for j in range(5):
                      numx[j] = dice.dice.count(dice.dice[j])
                      if tnum < numx[j]:
                         tnum = numx[j]
                   
                   for row in rows_to_check:
                     score.dict[row] = 0
                   auto_checkStraights()
                   auto_score()

## Algorithm to score the highest available value in a thorw
                     
                   maxVal = score.dict["1"]
                   selStr = "1"
                   for rowk in rows_to_check:
                     if score.dict[rowk] >= maxVal and rowk not in rowUsed[1:][pcol]:
                           maxVal = score.dict[rowk]
                           selStr = rowk
                   tbl.set(19,pcol,selStr)
                   rowx = simpledialog.askstring("Input", "Do you want to override, then enter row",
                                parent=application_window)
                   if rowx != "":
                       selStr = rowx    
                       rowUsed[1:][pcol].append(selStr)
                   else:
                       rowUsed[1:][pcol].append(selStr)
                   
                   tbl.set(19,pcol,selStr)
                   
                   messagebox.showinfo("Entering score", names[pcol-1])
                   rolls += 1
                   process_score()
                   reset()

def play():
                global pcol
                global numpl
                global numCpu
                global rolls
                global names
                global nn
                global nyats
                global namesf
                global rowUsed
                
                pcol += 1
                
                jend = 13*int(numpl)
                
## plays all the cpu hands
                
                if names[pcol-1] == "cpu" and rolls < jend:
                       rolls += 1
                       nn = pcol - 1
                       print(nn, rolls)
                       auto_card()
                       reset()
                
## checks for the end of the game and sets scores                 
                
                value = tk.StringVar()
                             
                if rolls == jend:
                         for i in range(int(numpl)):
                           j = 0
                           nx = 0
                           pcol = i + 1
                           Bonus = 0
                           for k in range(7):
                             j = j + 1
                             nx  = nx + int(tbl.get(j, pcol,value))
                             if nx >= 63:
                               Bonus = 35
                             BonusUpd = Bonus + 100*(nyats[i] - 1)
                             tbl.set(7,i+1,BonusUpd)
                             testBest = tbl.get(17,i+1,value)
                             
                             tbl.set(0,i+1,namesf[i]) 
                             process_score()
                             if (testBest) > (tbl.get(18,i+1,value)):
                                tbl.set(18,i+1,testBest)
                         messagebox.showinfo("Game Over", "Start a new game")
                         
## Restart a new game without interupting the process                       
                         rolls = 0
                         pcol = 0
                         nyats = 4*[1]
                         asx = simpledialog.askstring("Input", "Enter re to restart",
                                parent=application_window)
                         if asx == "re":
                          del rowUsed[:][:]           
                          rowUsed = [[0 for j in range(20)] for i in range(6)]
                          for i in range(int(numpl)):
                             tbl.reset(17, i+1, '0')
                             tbl.set(0,i+1,namesf[i])
                          play()
                         else:
                          sys.exit(0)
                 
                
def process_score():

## Process all the scores

                   global tbl
                   
                   global pcol
                   global numpl
                   global rows_to_check
                   
                   nx = 0
                   ny = 0
                   
                   value = tk.StringVar()
                   

                   if names[pcol-1] == "cpu":
                   
                     maxVal = score.dict["1"]
                     selStr = "1"
                     for rowk in rows_to_check:
                       if score.dict[rowk] > maxVal and rowk not in rowUsed[1:][pcol]:
                         maxVal = score.dict[rowk]
                         selStr = rowk
                     rowUsed[1:][pcol].append(selStr)
                     
                     tbl.set(19,pcol,selStr)

                   chosen = tbl.get(19,pcol,value)
                   
                   j = 0
                   for row in rows_to_check:
                       j = j + 1
                       if row == str(chosen):
                          if tbl.get(j,pcol,value) == "0":
                             tbl.set(j,pcol,str(score.dict[row]))
                        
                   j = 0
                   for row in rows_to_check:
                       j = j + 1
                       if j <= 7:
                         nx  = nx + int(tbl.get(j, pcol,value))
                       else:
                        if  row != "dum":
                          ny =  ny + int(tbl.get(j,pcol,value))

                   tbl.set(15,pcol,str(nx))
                   tbl.set(16,pcol,str(ny))
                   tbl.set(17,pcol,str(nx+ny))
                   
                   

def reset():
    global x
    global pcol
    global numpl
    
    x = 0
    cb1.deselect()
    cb2.deselect()

    cb3.deselect()
    cb4.deselect()
    cb5.deselect()
    if pcol == int(numpl):
       pcol = 0
       
    play()
                   
def auto_checkStraights():
    
    global tbl
    global pcol
    global numpl
    global dice
    
   
    dice_copy = dice.dice
    dice_copy.sort()
    value = tk.StringVar()
    
                 
    if  tbl.get(11,pcol,value) == "0":
            poss   = [1, 2, 3, 4]
            poss1  = [2, 3, 4, 5]
            poss2  = [3, 4, 5, 6]
            
            for i in range(1,7):
                if dice_copy.count(str(i)) >= 2:
                    dice_copy.remove(str(i))
            
            if (dice_copy[0:4] == poss) or (dice_copy[0:4] == poss1) or (dice_copy[0:4] == poss2):
                print ("Small Straight used")
                tbl.set(19,pcol,"sm")
                roll_score = 30
                score.update("sm", roll_score)
             
            if (dice_copy[1:5] == poss) or (dice_copy[1:5] == poss1) or (dice_copy[1:5] == poss2):
                
                print ("Small Straight used")
                tbl.set(19,pcol,"sm")
                roll_score = 30
                score.update("sm", roll_score)

    if  tbl.get(12,pcol,value) == "0":
            pos  = [1, 2, 3, 4, 5]
            pos1 = [2, 3, 4, 5, 6]
            
            if (dice_copy[0:] == pos) or (dice_copy[0:] == pos1):
                print ("Large Straight used")
                tbl.set(19,pcol,"lg")
                roll_score = 40
                score.update("lg", roll_score)

            
                   
def auto_score():

    global tbl
    global pcol
    global numpl
    global dice
    global nyats
    global rolls
    global nn
    global tnum
    global numx, tnum

    dice_copy = dice.dice
    dice_copy.sort()
    value = tk.StringVar()
            
    unique = []
    [unique.append(item) for item in dice_copy if item not in unique]
    dice_copy = unique   
                    
    
            
    if tnum >= 2:
          nj =  int(dice.dice.count(6))
          if nj >= 2  and tbl.get(6,pcol,value) == "0":
           print("returns 6s")
           tbl.set(19,pcol,"6")
           roll_score = nj*6
           score.update("6", roll_score)
           
          nj = int( dice.dice.count(5))
          if nj >= 2 and  tbl.get(5,pcol,value) == "0":
           print("returns 5s")
           tbl.set(19,pcol,"5")
           roll_score = nj*5
           score.update("5", roll_score)
           
          nj = int( dice.dice.count(4))
          if nj >= 2 and  tbl.get(4,pcol,value) == "0":
           print("returns 4s")
           tbl.set(19,pcol,"4")
           roll_score = nj*4
           score.update("4", roll_score)
           
          nj = int( dice.dice.count(3))
          if nj >= 2 and  tbl.get(3,pcol,value) == "0":
           print("returns 3s")
           tbl.set(19,pcol,"3")
           roll_score = nj*3
           score.update("3", roll_score)
           
          nj = int( dice.dice.count(2))
          if nj >= 2 and  tbl.get(2,pcol,value) == "0":
           print("returns 2s")
           tbl.set(19,pcol,"2")
           roll_score = nj*2
           score.update("2", roll_score)
           
          nj = int( dice.dice.count(1))
          if nj >= 2  and tbl.get(1,pcol,value) == "0":
           print("returns 1s")
           tbl.set(19,pcol,"1")
           roll_score = nj*1
           score.update("1", roll_score)
           
    if tnum >= 1 and rolls >= 7*int(numpl):
          nj =  int(dice.dice.count(6))
          if nj >= 1  and tbl.get(6,pcol,value) == "0":
           print("returns 6s")
           tbl.set(19,pcol,"6")
           roll_score = nj*6
           score.update("6", roll_score)
           
          nj = int( dice.dice.count(5))
          if nj >= 1 and  tbl.get(5,pcol,value) == "0":
           print("returns 5s")
           tbl.set(19,pcol,"5")
           roll_score = nj*5
           score.update("5", roll_score)
           
          nj = int( dice.dice.count(4))
          if nj >= 1 and  tbl.get(4,pcol,value) == "0":
           print("returns 4s")
           tbl.set(19,pcol,"4")
           roll_score = nj*4
           score.update("4", roll_score)
           
          nj = int( dice.dice.count(3))
          if nj >= 1 and  tbl.get(3,pcol,value) == "0":
           print("returns 3s")
           tbl.set(19,pcol,"3")
           roll_score = nj*3
           score.update("3", roll_score)
           
          nj = int( dice.dice.count(2))
          if nj >= 1 and  tbl.get(2,pcol,value) == "0":
           print("returns 2s")
           tbl.set(19,pcol,"2")
           roll_score = nj*2
           score.update("2", roll_score)
           
          nj = int( dice.dice.count(1))
          if nj >= 1  and tbl.get(1,pcol,value) == "0":
           print("returns 1s")
           tbl.set(19,pcol,"1")
           roll_score = nj*1
           score.update("1", roll_score)
      
    if tnum == 4  and  tbl.get(9,pcol,value) == "0":
           print("return four of a kind")
           tbl.set(19,pcol,"4k")
           roll_score = dice.total()
           score.update("4k", roll_score)
 
           
               
    if tnum == 3   and tbl.get(8,pcol,value) == "0":
        if len(dice_copy) >= 2:
              print("return 3of a kind")
              tbl.set(19,pcol,"3k")
              roll_score = dice.total()
              score.update("3k", roll_score)

    if tnum >= 0 and dice.total() > 20 and tbl.get(13,pcol,value) == "0":
           print ( "returns Chance ")
           tbl.set(19,pcol,"ch")
           roll_score = dice.total()
           score.update("ch", roll_score)

    if tnum >= 2  and tbl.get(10,pcol,value) == "0":
      if dice.dice.count(dice.dice[0]) == 4 or dice.dice.count(dice.dice[1]) == 4:
              pass
      elif len(dice_copy) == 2:
              print("return Full House")
              tbl.set(19,pcol,"fh")
              roll_score = 25
              score.update("fh", roll_score) 

    auto_checkStraights()       
 
                 
    if tnum == 5  and tbl.get(14,pcol,value) == "0":
             print("return Yahtzee")
             tbl.set(19,pcol,"yat")
             roll_score = 50
             score.update("yat", roll_score)
             
    if tnum == 5 and tbl.get(10,pcol,value) == "yat":
             nyats[nn] += 1
           
        
def auto_card():

    global dice
    global nn
    global numx, tnum
    global rows_to_check
    global tnum
    # draws all single value dice
    
    numx = [0,0,0,0,0]
    tnum = 0

    for rowk in rows_to_check:
      score.dict[rowk] = 0
    
   
    for i in range(5):
       dice.dice[i] = random.randint(1,6)
    print("First roll", dice.dice)

    auto_checkStraights()
    tnum = 0

    if nn == 1:               
      for j in range(5):
        numx[j] = dice.dice.count(dice.dice[j])
        if numx[j] == 1:
            dice.dice[j] = random.randint(1,6)
      print("Second roll", dice.dice)
      for j in range(5):
        numx[j] = dice.dice.count(dice.dice[j])
        if numx[j] == 1:
            dice.dice[j] = random.randint(1,6)
      print("Third roll", dice.dice)
    elif nn == 0:
      for j in range(5):
        numx[j] = dice.dice.count(dice.dice[j])
      cmax = max(dice.dice)
      for j in range(5):
        if dice.dice[j] != int(cmax):
           dice.dice[j] = random.randint(1,6)
      print("Second roll", dice.dice)
      
      for j in range(5):
        numx[j] = dice.dice.count(dice.dice[j])
      cmax = max(dice.dice)
      for j in range(5):
        if dice.dice[j] != int(cmax):
          dice.dice[j] = random.randint(1,6)
      print("Third roll", dice.dice)
        
    elif nn == 2:
      for j in range(5):
        numx[j] = dice.dice.count(dice.dice[j])
      cmax = max(numx)
      for j in range(5):
        if numx[j] != int(cmax):
            dice.dice[j] = random.randint(1,6)
      print("Second roll", dice.dice)
      
      for j in range(5):
        numx[j] = dice.dice.count(dice.dice[j])
      cmax = max(numx)
      for j in range(5):
       if numx[j] != int(cmax):
         dice.dice[j] = random.randint(1,6)
      print("Third roll", dice.dice)
      
    elif nn == 3:
            
      for i in range(5):
       dice.dice[i] = random.randint(1,6)
      print("Second roll", dice.dice)

      for i in range(5):
       dice.dice[i] = random.randint(1,6)
      print("Third roll", dice.dice)
      

    for j in range(5):
        numx[j] = dice.dice.count(dice.dice[j])
        if tnum < numx[j]:
                tnum = numx[j]
                
    if score.dict["sm"]  == 30 or score.dict["lg"] == 40:
       do_nothing()
    else:
       auto_score()

    process_score()


    

  

def createDefaultDict():
    global rows_to_check
    rows_to_check  = '1 2 3 4 5 6 bon 3k 4k fh sm lg ch yat dum'.split()
    
    template = {}

    for item in rows_to_check:
        template[str(item).lower()] = 0
    return template

def cls():
    print ( '\n' * 10)


    
# create the window form
root = tk.Tk()
global x
global pcol
global numpl
global numCpu

global rolls
global names
global dice
global nyats
global namesf
global tbl
global rowUsed
global rows_to_check

nyats = 4*[1]
score = Score()
dice = Dice()
rolls = 0
dice_list = [0, 1, 2, 3, 4, 5]
names = [" " for i in range(5)]
namesf = [" " for i in range(5)]
rowUsed = [[0 for j in range(20)] for i in range(6)]

createDefaultDict()

# StringVar() updates result label automatically
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var =  tk.StringVar()
cvar1 = tk.IntVar()
cvar2 = tk.IntVar()
cvar3 = tk.IntVar()
cvar4 = tk.IntVar()
cvar5 = tk.IntVar()

# create chkboxes for dices
cb1 = tk.Checkbutton(root, text="Dice1", variable=cvar1)
cb1.grid(row=5, column =0)
cb2 = tk.Checkbutton(root, text="Dice2", variable=cvar2)
cb2.grid(row=5, column =1)
cb3 = tk.Checkbutton(root, text="Dice3", variable=cvar3)
cb3.grid(row=5, column =2)
cb4 = tk.Checkbutton(root, text="Dice4", variable=cvar4)
cb4.grid(row=5, column =3)
cb5 = tk.Checkbutton(root, text="Dice5", variable=cvar5)
cb5.grid(row=5, column =4)

# create the result label
result = tk.Label(root, textvariable=var1, fg='red')
result.grid(row=6, column=0, columnspan=1)
result = tk.Label(root, textvariable=var2, fg='green')
result.grid(row=6, column=1, columnspan=1)
result = tk.Label(root, textvariable=var3, fg='blue')
result.grid(row=6, column=2, columnspan=1)
result = tk.Label(root, textvariable=var4, fg='magenta')
result.grid(row=6, column=3, columnspan=1)
result = tk.Label(root, textvariable=var5, fg='red')
result.grid(row=6, column=4, columnspan=1)
result = tk.Label(root, textvariable=var, fg='red')
result.grid(row=6, column=5, columnspan=1)




# start with an empty canvas

var1.set("")
var2.set("")
var3.set("")
var4.set("")
var5.set("")
cls()
x = 0


button1 = tk.Button(root, text="Press me", command=click)
button1.grid(row=3, column=0, pady=3)

Label(text="Yahtzee Roll Scoring Table", fg = "blue", bg = "yellow", font = "Helvetica 16 bold italic" 
		 ).grid(row = 7, column = 0, columnspan = 5, sticky = W+E+N+S)
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.grid(row = 8, column = 0, columnspan = 5, sticky = W+E+N+S)
        
tbl = SimpleTable(root,20,5)
tbl.grid(row = 9, rowspan = 27, column = 0, columnspan = 5, sticky = W+E+N+S)
setTable()

numCpu = 0
pcol = 0

application_window = tk.Tk()

numpl = simpledialog.askstring("Input", "Number of players?",
                                parent=application_window,
                                minvalue="1", maxvalue="4")

for i in range(int(numpl)):
  namesf[i] = simpledialog.askstring("Input", "What is your name?",
                                 parent=application_window)

for i in range(int(numpl)):
    tbl.set(0,i+1,namesf[i])
    stx = namesf[i][:3]
    
    if stx.lower() == "cpu":
      numCpu = numCpu +1
      names[i] = "cpu"
play()   
root.mainloop()


