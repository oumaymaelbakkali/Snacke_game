# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 06:15:55 2022

@author: Oumayma
"""

from tkinter import *
from random import *

#paramètres
largeur, nbCaseX, nbCaseY = 20,40,20
colorBg, colorLine ='black','gray'
colorHeader, colorbody, colorRepas,colorObstacle = 'red','lightgreen','blue','white'
repas=[]
body=[]
obstacle=[]
direction ='Right'
ID = None

def designGrid():
    #design line vertical
    for i in range(nbCaseX+1):
        canvas.create_line(largeur*i,0 ,largeur*i,largeur*nbCaseY,fill=colorLine)
    #design line vertical
    for i in range(nbCaseY+1):
        canvas.create_line(0,largeur*i ,largeur*nbCaseX,largeur*i,fill=colorLine)
        
def designCellule(x,y,couleur):
    objGraph=canvas.create_rectangle(x*largeur,y*largeur,(x+1)*largeur,(y+1)*largeur,fill=couleur)
    return objGraph 

def deleteCellule(cellule):
    canvas.delete(cellule)

    
def initialiserJeu():
    #design grid
    designGrid()
    # create 5 cellule pour le serpont
    body.append([designCellule(6,2,colorHeader),6,2,colorHeader])
    body.append([designCellule(5,2,colorbody),5,2,colorbody])
    body.append([designCellule(4,2,colorbody),4,2,colorbody])
    body.append([designCellule(3,2,colorbody),3,2,colorbody])
    body.append([designCellule(2,2,colorbody),2,2,colorbody])
    #generer repas
    Repas()
    #create obstacle
    for i in range(nbCaseX//4,3*(nbCaseX//4)):
        obstacle.append([designCellule(i,nbCaseY//3,colorObstacle),i,nbCaseY//3,colorObstacle])
        obstacle.append([designCellule(i,2*nbCaseY//3,colorObstacle),i,2*nbCaseY//3,colorObstacle])

    
def Repas():
    #generer un repas aléatoirement en evitant de le mettre sur le serpant/dimension de canvas
    x=6
    y=2
    listeX=[]
    listeY=[]
    for i in range(len(obstacle)):
        listeX.append(obstacle[i][1])
    for i in range(len(obstacle)):
        listeY.append(obstacle[i][2])
    for i in range(len(body)):
        listeX.append(body[i][1])
    for i in range(len(body)):
        listeY.append(body[i][2])
    while x in listeX:
        x=randint(0,nbCaseX-1)
    while y in listeY:
        y=randint(0,nbCaseY-1)
    repas.append([designCellule(x,y,colorRepas),x,y,colorbody])
    
    
def changerDirection(event):
    global direction
    if(event.keysym == 'Right' and direction!="Left"):
        direction='Right'
    if(event.keysym == 'Left'and direction!="Right"):
        direction='Left'
    if(event.keysym == 'Up' and direction!="Down"):
        direction='Up'
    if(event.keysym == 'Down' and direction!="Up"):
        direction='Down'
    print(direction)
    
def SnakeUpdate():
    for cellule in body:
        canvas.coords(cellule[0],cellule[1]*largeur,cellule[2]*largeur,(cellule[1]+1)*largeur,(cellule[2]+1)*largeur)


def Stop():
    global ID
    window.after_cancel(ID)
    

def Move():
    # souvgarder les position de la tete avant de la deplacer
    teteX=body[0][1]
    teteY=body[0][2]
    
    #calcul la nouvel position des cellules
    if direction=='Right':
        body[0][1]+=1
        
    if direction=='Left':
        body[0][1]-=1
        
    if direction=='Down':
        body[0][2]+=1
        
    if direction=='Up':
        body[0][2]-=1
        
    if body[0][1]==nbCaseX:
        body[0][1]=0
    if body[0][1]==-1:
        body[0][1]=nbCaseX-1
    
    if body[1][1]==nbCaseX:
        body[1][1]=0
    if body[1][1]==-1:
        body[1][1]=nbCaseX-1
        
    if body[2][1]==nbCaseX:
        body[2][1]=0
    if body[2][1]==-1:
        body[2][1]=nbCaseX-1
        
    if body[3][1]==nbCaseX:
        body[3][1]=0
    if body[3][1]==-1:
        body[3][1]=nbCaseX-1
        
    if body[4][1]==nbCaseX:
        body[4][1]=0
    if body[4][1]==-1:
        body[4][1]=nbCaseX-1
        
    if body[0][2]==nbCaseY:
        body[0][2]=0
    if body[0][2]==-1:
        body[0][2]=nbCaseY-1
    
    if body[1][2]==nbCaseY:
        body[1][2]=0
    if body[1][2]==-1:
        body[1][2]=nbCaseY-1
        
    if body[2][2]==nbCaseY:
        body[2][2]=0
    if body[2][2]==-1:
        body[2][2]=nbCaseY-1
        
    if body[3][2]==nbCaseY:
        body[3][2]=0
    if body[3][2]==-1:
        body[3][2]=nbCaseY-1
        
    if body[4][2]==nbCaseY:
        body[4][2]=0
    if body[4][2]==-1:
        body[4][2]=nbCaseY-1
        
    #deplacer le retse de cors
    for i in range (len(body)-1,1,-1):
        body[i][1]=body[i-1][1]
        body[i][2]=body[i-1][2]
        
    #coinsidance avec repas
    X=len(repas)-1
    if body[0][1] == repas[X][1] and body[0][2] == repas[X][2]:
        body.append([designCellule(repas[X][1],repas[X][2],colorbody),repas[X][1],repas[X][2],colorbody])
        deleteCellule(repas[X][0])
        Repas()
        
    for cellule in body:
        if teteX == cellule[1] and teteY == cellule[2]:
            GameOver()
    
    for cellule in obstacle:
        if teteX == cellule[1] and teteY == cellule[2]:
            GameOver()
        
    # cellule 2 doit prendre les position de la tete avant de 
    body[1][1]=teteX
    body[1][2]=teteY
    SnakeUpdate()
    global ID
    ID=window.after(300,Move)
    
def yes():
    print("yes")
    initialiserJeu()

       
def GameOver():
    
    myWindow = Tk()
    window.destroy()
    myWindow.title('Game Over')
    myWindow.configure(bg='black')
    label1 = Label(myWindow,text='Game over !',fg='red',font='bold',bg='black')
    
    b3 = Button(myWindow,text ='OK',width=8,command=myWindow.destroy)
    
    #place components
    label1.place(x=55,y=55)
    b3.place(x=70,y=150)
   

    myWindow.mainloop()
    
#declaration of components  
window = Tk()
window.title('Snake Game')

canvas = Canvas(window,width=largeur*nbCaseX,height=largeur*nbCaseY,bg=colorBg)
b1 = Button(window,text ='Start',width=25,command=Move)
b2 = Button(window,text ='Stop',width=25,command=Stop)
label = Label(window,text='Made by Oumayma EL Bakkali',fg='blue',font='bold')

#place components
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
canvas.grid(row=2,column=0,columnspan=2)
label.grid(row=3,column=0 ,columnspan=2)
#window.bind('<q>',func)

#init jeu
initialiserJeu()

window.bind('<Key>',changerDirection)
window.mainloop()