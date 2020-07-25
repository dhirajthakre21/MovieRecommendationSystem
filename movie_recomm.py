import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter
from tkinter.ttk import *
from tkinter import *


md=pd.read_csv('movie_database1.csv')



def all_movie():
    print(md.iloc[:,2])
    
 
    
    
def genre_movies(gname):

    gname=gname.title()
    templist = []
    a=1
    Glist = []
    mlist = []
    for i in md.Genre:
        Glist.append(i) 
    count = 0
    for j in Glist:
        templist= j.split(',')
        if gname in templist :
             mlist.append(md.Title[count])
        count=count+1
#    print(mlist)
    T.delete('1.0', END)
    for i in mlist: 
        T.insert(END, "[%d] "%a)
        T.insert(END, " %s \n\n"%i)
        a=a+1



def rmovies():
    print("Movies in range of ratings : ")
    maxr=float(input("max range : "))
    minr=float(input("min range : "))

    rlist = []
    for i in md.IMDB_Score:
        rlist.append(i)
    
    count=0
    for j in rlist:
        if rlist[count]<=maxr and rlist[count]>=minr:
            print(md.Title[count])
        count=count+1


def director_movies():
        
#    tname = input("Enter the Director's name :")
    dname=sname.get()
    
    dname=dname.title()
    Dlist = []
    tlist = []
    for i in md.Director:
        Dlist.append(i) 
    
    count = 0
    a = 1
    for j in Dlist:
        if j==dname :
            tlist.append(md.Title[count])
        count=count+1
        
    T.delete('1.0', END)
    for i in tlist: 
        T.insert(END, "[%d] "%a)
        T.insert(END, " %s \n"%i)
        a=a+1


def movie_rating():

    temp = input("Enter the Movie name :")
    mname=temp.title()

    Mlist = []
    for i in md.Title:
        Mlist.append(i) 
    print(Mlist)

    index = Mlist.index(mname)

    print("Movie : "+mname.upper())
    print("IMDB rating : "+str(md.IMDB_Score[index]))



#plt.hist(md.Year,histtype='barstacked')


##################################################################################






#filename = PhotoImage(file="5.png")
#background_label = Label(root, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
def func():
    text = combo.get()
    genre_movies(text)


def funa():
    director_movies(dname.get())






window = Tk()


window.geometry('1920x1080')
'''Adding_background_Image '''
C = Canvas(window, bg="red", height=100, width=30)
filename = PhotoImage(file="sixth-section-bg.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


C.pack()

window.title("Movie Recommendation") 
window.geometry('555x555')



#scroll bar to show movies based on genre

genreList = ["Animation",'Action','Sci-Fi','Horror','Thriller','Comedy','Family','Drama',
             'Romance','History','Crime','Adventure','Biography','War','fantasy','Music',
             'Sport','Mystery','Music']

l=Label(window,text="Choose the Genre to display the movies", font=("Verdana",13,"bold"))
l.pack()

combo = Combobox(window, values=genreList, width = 25, height = 90 , font=("Verdana",13,"bold"))
combo.current(0)
combo.pack()
 
btn = Button(window,text="Click Here",command=func, font=("Verdana",13,"bold"))
btn.pack()




l2=Label(window,text="")
l2.pack()
l3=Label(window,text="")
l3.pack()
l4=Label(window,text="")
l4.pack()


#search box for Director's name

l1=Label(window,text="Enter the Director's name to show his movies",bg="pink", fg="black",  font=("Verdana",13,"bold"))
l1.pack()

sname = StringVar()

dsearch = Entry(window , textvariable = sname, width = 20,font=("Verdana",16))
dsearch.pack()


btn1 = Button(window,text="Click Here", command =director_movies, font=("Verdana",13,"bold"))
btn1.pack()







s = Scrollbar(window)
T = Text(window , font=("Verdana",17),width=100 , height=100 , fg = "black", bg="grey")

T.focus_set()
s.pack(side=RIGHT, fill=Y ,pady=10 )
T.pack(side=RIGHT, fill=Y , pady=10 )
s.config(command=T.yview)
T.config(yscrollcommand=s.set)



    
    
    
window.mainloop()
































