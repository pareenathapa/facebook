# from cProfile import label
# from tkinter import *
# root=Tk()
# root.title("login")
# root.iconbitmap("abc.ico")
# # root.maxsize(width=300,height=200)
# # root.minsize(width=300,height=200)
# root.geometry('600x300')
# redbutton=Button(root,text="LEFT",fg="green")
# redbutton.pack(side=LEFT)
# greenbutton=Button(root,text='RIGHT',fg='black')
# name=label(root,text="name").grid(row=0,column=0)
# # el=Entry(root).grid(row=0,column=1)
# # password=label(root,text="password").grid(row=1,column=0)
# # e2=Entry(root).grid(row=1,column=1)

# # submit=Button(root,text="submit").grid(row=4,column=1)


# # # root.mainloop()


# # from cProfile import label
# # from cgitb import text
# # from tkinter import*
# # top=Tk()
# # top.geometry("400x250")
# # top.configure(bg="blue")
# # Username=Label(top,text="Username").place(x=20,y=50)
# # Email=Label(top,text="Email").place(x=30,y=90)
# # Password=Label(top,text="Password").place(x=30,y=130)
# # contact=Label(top,text="confirm password").place(x=30,y=130)
# # pareena=Label(top,text="age").place(x=36,y=210)
# # sign=Button(top,text="sign up").place(x=150,y=250)
# # e1=Entry(top).place(x=80,y=50)
# # e2=Entry(top).place(x=80,y=90)
# # e3=Entry(top).place(x=95,y=130)
# # e4=Entry(top).place(x=145,y=170)
# # e5=Entry(top).place(x=145,y=120)
# # top.mainloop()

# # # from tkinter import Label, Tk
# # # 
# # # from tkinter.tix import Tk


# # # root=Tk
# # # # to rename the title of the window
# # # root.title("GUI")
# # # myLabel=Label(root,text="tkinter",font=("arial bold",50))
# # # # pack is used to show the object in the window
# # # myLabel.pack()
# # # root.mainloop()


# # # from tkinter import Button, Tk


# # # window=Tk()
# # # window.maxsize(width=300,height=300)
# # # window.minsize(width=300,height=300)
# # # def func():
# # #     print("button is clicked")

# # # btn=Button(window,text="login",command=func)
# # # btn.pack(side='top')
# # # window.mainloop()


# # # from tkinter import END, Tk, mainloop
# # # from tkinter.ttk import Button, Label


# # # root=Tk()

# # # def click():
# # #     text1="address:"+ mytext.get('1.0',END)
# # #     lbl.config(text=str(text1))

# # # mytext=Text(root,font=20,width=20,height=10)
# # # mytext.place(x=0,y=50)

# # # btn=Button(root,text="click me",font=30,command=click)
# # # btn.place(x=400,y=300)

# # # lbl=Label(root,text="",font=30)
# # # lbl.place(x=200,y=300)

# # # root,mainloop()

# # # from tkinter.tix import Tk
# # # from tkinter.ttk import Button, Labelframe


# # # window=Tk()
# # # frame=Labelframe(window,text="this is my frame",padx=10,pady=10)
# # # frame.pack(padx=50,pady=50)
# # # b=Button(frame,text="don't click here")
# # # b2=Button(frame,text='....here')
# # # b.grid(row)

# # # from tkinter import Radiobutton, Variable
# # # from tkinter.tix import Tk


# # # window=Tk()
# # # def add():
# # #     print(var.get())
# # # var=IntVar()
# # # r1=Radiobutton(window,text="male",variable=var,value=1,command=add)
# # # r1.pack(anchor=W)
# # # r2=Radiobutton(window,text="female",variable=var,value=2,command=add)
# # # r2.pack(anchor=w)
# # # window.mainloop()

# # from cProfile import label
# # from msilib.schema import RadioButton
# # from tkinter import W, IntVar, Tk


# # window=Tk()
# # def add():
# #     selection="you have selected the option"+str(var.get())
# #     label.config(text=selection)
# # var=IntVar()
# # r1=RadioButton(window,text="option 1",variable=var,value=1,command=add)
# # r1.pack(anchor=W)
# # r2=RadioButton(window,text="option 2",variable=var,value=2,command=add)
# # r2,pack(anchor=W)
# # r3=RadioButton(window,text="option 3",variable=var,value=1,command=add)
# # r3.pack(anchor=W)
# # label=label(window)
# # label.pack()
# # window.mainloop()



# from tkinter import *
# root = Tk()
# # defining title of the project
# root.title("Simple Calculator")
# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# def button_click(number):
#     current = e.get()
#     e.delete(0, END)
#     e.insert(0, str(current) + str(number))


# def button_clear():
#     e.delete(0, END)


# def button_add():
#     global f_num
#     first_number = e.get()
#     global math
#     math="add"
#     f_num = int(first_number)
#     e.delete(0, END)

# def button_sub():
#     global f_num
#     first_number=e.get()
#     global math
#     math="sub"
#     f_num = int(first_number)
#     e.delete(0, END)

# def button_div():
#     global f_num
#     first_number=e.get()
#     global math
#     math="div"
#     f_num = int(first_number)
#     e.delete(0, END)

# def button_mult():
#     global f_num
#     first_number=e.get()
#     global math
#     math="div"
#     f_num = int(first_number)
#     e.delete(0, END)



# def button_equal():
#     second_number = e.get()
#     e.delete(0, END)
#     e.insert(0, f_num+int(second_number))


# def button_equal():
#     second_number = e.get()
#     e.delete(0, END)
#     if math=="add":
#         e.insert(0, f_num+int(second_number))
#     elif math=="sub":
#         e.insert(0,f_num-int(second_number))
#     elif math=="mult":
#         e.insert(0,f_num*int(second_number))
#     elif math=="div":
#         e.insert(0,f_num/int(second_number))
    


# # Defining the buttons
# button_1 = Button(root, text="1", padx=40, pady=20,
#                   command=lambda: button_click(1))
# button_2 = Button(root, text="2", padx=40, pady=20,
#                   command=lambda: button_click(2))
# button_3 = Button(root, text="3", padx=40, pady=20,
#                   command=lambda: button_click(3))
# button_4 = Button(root, text="4", padx=40, pady=20,
#                   command=lambda: button_click(4))
# button_5 = Button(root, text="5", padx=40, pady=20,
#                   command=lambda: button_click(5))
# button_6 = Button(root, text="6", padx=40, pady=20,
#                   command=lambda: button_click(6))
# button_7 = Button(root, text="7", padx=40, pady=20,
#                   command=lambda: button_click(7))
# button_8 = Button(root, text="8", padx=40, pady=20,
#                   command=lambda: button_click(8))
# button_9 = Button(root, text="9", padx=40, pady=20,
#                   command=lambda: button_click(9))
# button_0 = Button(root, text="0", padx=40, pady=20,
#                   command=lambda: button_click(0))
# button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
# button_sub = Button(root,text="_",padx=41,pady=20,command=button_sub)
# button_div = Button(root,text="/",padx=41,pady=20,command=button_div)
# button_mult = Button(root,text="*",padx=40,pady=20,command=button_mult)
# button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
# button_clear = Button(root, text="clear ", padx=79,
#                       pady=20, command=button_clear)
# # Putting buttons on the screen
# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)
# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)
# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)
# button_0.grid(row=4, column=0)
# button_clear. grid(row=4, column=1, columnspan=2)
# button_add. grid(row=5, column=0)
# button_sub.grid(row=6,column=0)
# button_div.grid(row=6,column=1)
# button_mult.grid(row=6,column=2)
# button_equal.grid(row=5, column=1, columnspan=2)
# root . mainloop()