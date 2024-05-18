from tkinter import *
import tkinter.messagebox

root= Tk()

root.geometry("500x440") #to set the window dimensions
root.title("Calculator by Sagarika")
f= Frame(root, bg= 'gray')
f.pack()
screen = Entry(f, bg= "light gray", font= "arial 30",fg= "blue", relief= SUNKEN, borderwidth=4) #claculator screen
screen.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)

def myclick(number):
    screen.insert(END, number)

def equal():
    try:
        y = str(eval(screen.get()))
        screen.delete(0, END)
        screen.insert(0,y)

    except: 
        tkinter.messagebox.showinfo("Error", "Syntex Error")

def clear():
    screen.delete(0, END)


b1= Button(f, text= "1", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=3, command= lambda: myclick(1))
b1.grid(row=1, column =0,columnspan=1)
b2= Button(f, text= "2", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=3, command= lambda: myclick(2))
b2.grid(row=1, column =1)
b3= Button(f, text= "3", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=2, command= lambda: myclick(3))
b3.grid(row=1, column =2)
b4= Button(f, text= "4", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=2, command= lambda: myclick(4))
b4.grid(row=1, column =3)
b5= Button(f, text= "5", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=2, command= lambda: myclick(5))
b5.grid(row=2, column =0)
b6= Button(f, text= "6", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=2, command= lambda: myclick(6))
b6.grid(row=2, column =1)
b7= Button(f, text= "7", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=2, command= lambda: myclick(7))
b7.grid(row=2, column =2)
b8= Button(f, text= "8", font= "arial 20 bold",  relief=RAISED, borderwidth=4,padx=15, pady=2, command= lambda: myclick(8))
b8.grid(row=2, column =3)
b9= Button(f, text= "9", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=2, command= lambda: myclick(9))
b9.grid(row=3, column =0)
b0= Button(f, text= "0", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=2, command= lambda: myclick(0))
b0.grid(row=3, column =1)
b_p1= Button(f, text= "(", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=5, command= lambda: myclick('('))
b_p1.grid(row=3, column =2)
b_p2= Button(f, text= ")", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=5, command= lambda: myclick(')'))
b_p2.grid(row=3, column =3)

b_add = Button(f, text="+",font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15,pady=5, width=3, command=lambda: myclick('+'))
b_add.grid(row=4, column=0)

b_sub =Button(master=f, text="-",font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=5, width=3, command=lambda: myclick('-'))
b_sub.grid(row=4, column=1)

b_multiply =Button(master=f, text="*", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=5, width=3, command=lambda: myclick('*'))
b_multiply.grid(row=4, column=2)

b_div =Button(master=f, text="/",font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=5,pady=15, width=3, command=lambda: myclick('/'))
b_div.grid(row=4, column=3)
 
b_clear = Button(master=f, text="clear", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15, pady=5, width=12, command=clear)
b_clear.grid(row=5, column=0, columnspan=2)
 
b_equal = Button(master=f, text="=", font= "arial 20 bold", relief=RAISED, borderwidth=4, padx=15,pady=5, width=9, command=equal)
b_equal.grid(row=5, column=2, columnspan=2)


root.mainloop()