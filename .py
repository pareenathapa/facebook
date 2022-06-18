
# from tkinter import *
# # from PIL import ImageTk, Image
# from tkinter import messagebox
# # from tkinter import filedialog
# import sqlite3

# root = Tk()
# root.title('Database GUI')
# # root.iconbitmap('E:/images/global.ico')
# root.geometry('300x480')

# # Databases

# # Create a databases or connect to one
# conn = sqlite3.connect('address_book.db')

# # Create cursor
# c = conn.cursor()

# # Create table
# # c.execute(""" CREATE TABLE addresses(
# #       first_name text,
# #       last_name text,
# #       address text,
# #       city text,
# #       state text,
# #       zipcode integer
# # ) """)


# # Creating a function to delete a record

# def delete():
#     # create database
#     conn = sqlite3.connect('address_book.db')

#     # create cursor
#     c = conn.cursor()

#     # delete a record
#     c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
#     print('Deleted Successfully')

#     # query of the database
#     c.execute("SELECT *, oid FROM addresses")

#     records = c.fetchall()
#     # print(records)

#     # Loop through the results
#     print_record = ''
#     for record in records:
#         # str(record[6]) added for displaying the id
#         print_record += str(record[0]) + ' ' + str(record[1]) + \
#             ' ' + '\t' + str(record[6]) + "\n"

#     query_label = Label(root, text=print_record)
#     query_label.grid(row=12, column=0, columnspan=2)

#     conn.commit()

#     conn.close()

# # Creating an update function


# def update():
#     # Create a databases or connect to one
#     conn = sqlite3.connect('address_book.db')

#     # Create cursor
#     c = conn.cursor()

#     record_id = delete_box.get()

#     c.execute(""" UPDATE addresses SET
#          first_name = :first,
#          last_name = :last,
#          address = :address,
#          city = :city,
#          state = :state,
#          zipcode = :zipcode
#          WHERE oid = :oid""",
#               {'first': f_name_editor.get(),
#                'last': l_name_editor.get(),
#                'address': address_editor.get(),
#                'city': city_editor.get(),
#                'state': state_editor.get(),
#                'zipcode': zipcode_editor.get(),
#                'oid': record_id

#                }
#               )
#     conn.commit()
#     conn.close()
#     # Destroying all the data and closing window
#     editor.destroy()


# # Create edit function to update a record
# def edit():

#     global editor

#     editor = Tk()
#     editor.title('Update Data')
#     # editor.iconbitmap('E:/images/global.ico')
#     editor.geometry('300x480')

#     # Create a databases or connect to one
#     conn = sqlite3.connect('address_book.db')

#     # Create cursor
#     c = conn.cursor()

#     record_id = delete_box.get()

#     # query of the database
#     c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

#     records = c.fetchall()
#     # print(records)

#     # Creating global variable for all text boxes
#     global f_name_editor
#     global l_name_editor
#     global address_editor
#     global city_editor
#     global state_editor
#     global zipcode_editor

#     # Create text boxes
#     f_name_editor = Entry(editor, width=30)
#     f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

#     l_name_editor = Entry(editor, width=30)
#     l_name_editor.grid(row=1, column=1)

#     address_editor = Entry(editor, width=30)
#     address_editor.grid(row=2, column=1)

#     city_editor = Entry(editor, width=30)
#     city_editor.grid(row=3, column=1)

#     state_editor = Entry(editor, width=30)
#     state_editor.grid(row=3, column=1)

#     zipcode_editor = Entry(editor, width=30)
#     zipcode_editor.grid(row=4, column=1)

#     # Create textbox labels
#     f_name_label = Label(editor, text="First Name")
#     f_name_label.grid(row=0, column=0, pady=(10, 0))

#     l_name_label = Label(editor, text="Last Name")
#     l_name_label.grid(row=1, column=0)

#     address_label = Label(editor, text="Address")
#     address_label.grid(row=2, column=0)

#     city_label = Label(editor, text="City")
#     city_label.grid(row=3, column=0)

#     state_label = Label(editor, text="State")
#     state_label.grid(row=3, column=0)

#     zipcode_label = Label(editor, text="Zip Code")
#     zipcode_label.grid(row=4, column=0)

#     # loop through the results
#     for record in records:
#         f_name_editor.insert(0, record[0])
#         l_name_editor.insert(0, record[1])
#         address_editor.insert(0, record[2])
#         city_editor.insert(0, record[3])
#         state_editor.insert(0, record[4])
#         zipcode_editor.insert(0, record[5])

#     # Create a update button
#     edit_btn = Button(editor, text=" SAVE ", command=update)
#     edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


# # Create submit button for databases

# def submit():
#     # Create a databases or connect to one
#     conn = sqlite3.connect('address_book.db')

#     # Create cursor
#     c = conn.cursor()

#     # Insert into table
#     c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", {
#         'f_name': f_name.get(),
#         'l_name': l_name.get(),
#         'address': address.get(),
#         'city': city.get(),
#         'state': state.get(),
#         'zipcode': zipcode.get()
#     })
#     # showinfo messagebox
#     messagebox.showinfo("Adresses", "Inserted Successfully")

#     conn.commit()

#     conn.close()

#     # clear the text boxes
#     f_name.delete(0, END)
#     l_name.delete(0, END)
#     address.delete(0, END)
#     city.delete(0, END)
#     state.delete(0, END)
#     zipcode.delete(0, END)


# def query():
#     # Create a databases or connect to one
#     conn = sqlite3.connect('address_book.db')

#     # Create cursor
#     c = conn.cursor()

#     # query of the database
#     c.execute("SELECT *, oid FROM addresses")

#     records = c.fetchall()
#    # print(records)

#     # Loop through the results
#     print_record = ''
#     for record in records:
#         # str(record[6]) added for displaying the id
#         print_record += str(record[0]) + ' ' + str(record[1]) + \
#             ' ' + '\t' + str(record[6]) + "\n"

#     query_label = Label(root, text=print_record)
#     query_label.grid(row=12, column=0, columnspan=2)

#     conn.commit()
#     conn.close()


# # Create text boxes
# f_name = Entry(root, width=30)
# f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

# l_name = Entry(root, width=30)
# l_name.grid(row=1, column=1)

# address = Entry(root, width=30)
# address.grid(row=2, column=1)

# city = Entry(root, width=30)
# city.grid(row=3, column=1)

# state = Entry(root, width=30)
# state.grid(row=3, column=1)

# zipcode = Entry(root, width=30)
# zipcode.grid(row=4, column=1)

# delete_box = Entry(root, width=30)
# delete_box.grid(row=9, column=1, pady=5)

# # Create textbox labels
# f_name_label = Label(root, text="First Name")
# f_name_label.grid(row=0, column=0, pady=(10, 0))

# l_name_label = Label(root, text="Last Name")
# l_name_label.grid(row=1, column=0)

# address_label = Label(root, text="Address")
# address_label.grid(row=2, column=0)

# city_label = Label(root, text="City")
# city_label.grid(row=3, column=0)

# state_label = Label(root, text="State")
# state_label.grid(row=3, column=0)


# zipcode_label = Label(root, text="Zip Code")
# zipcode_label.grid(row=4, column=0)

# delete_box_label = Label(root, text="Delete ID")
# delete_box_label.grid(row=9, column=0, pady=5)


# # Create submit button

# submit_btn = Button(root, text="Add Records", command=submit)
# submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# # Create query button

# query_btn = Button(root, text="Show Records", command=query)
# query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# # Create a delete button
# delete_btn = Button(root, text="Delete", command=delete)
    # # delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

    # # # Create a update button
    # # edit_btn = Button(root, text="Update", command=edit)
    # # edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


    # # # commit change
    # # conn.commit()

    # # # close connection
    # # conn.close()


    # # mainloop()

    # from tkinter import *
    # import sqlite3
    # root = Tk()
    # root.title('Facebook')
    # conn = sqlite3.connect('facebook.db')
    # c = conn.cursor()

    # c.execute(""" CREATE TABLE User(
    #       FirstName text,
    #       LastName text,
    #       age integer,
    #       address text,
    #       city text,
    #       zipcode integer,
    #       password text,
    #       gender text
    # ) """)

    # root.mainloop()

from tkinter import*
import sqlite3
from tkinter import ttk,messagebox
root=Tk()


com=sqlite3.connect('facebook.db')


# c=com.cursor()
# c.execute(''' Create table user(
# #     firstName text,
# #     lastName text,
# #     age text,
# #     adress text,
# #     city text,
# #     Zipcode text,
# #     password text,
# #     gender text
# # )
# # ''')


fb=Label(root,text='FACEBOOK',fg='blue',font=20)
fb.grid(row=0,column=0,columnspan=2)

#commands
def submit():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('''insert into user values(:firstName, :lastName,:age,:adress,:city,:Zipcode,:password,:gender)''',{'firstName':firstname.get(),'lastName':lastname.get(),'age':age.get(), 'adress':address.get(),'city':city.get(),'Zipcode':zipcode.get(),'password':password.get(),'gender':gender.get()}
    )
    messagebox.showinfo('success','Inserted sucessfully')
    
    conn.commit()
    conn.close()




def show():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('select *,oid from user')
    messagebox.showinfo('success','showed')
    record=c.fetchall()
    print(record)
    conn.commit()
    conn.close()



def delete():
    conn= sqlite3.connect('facebook.db')

    c=conn.cursor()
    c.execute('delete from user where oid ='+delete_entry.get())
    print('success','deleted')
    conn.commit()
    conn.close()
def update():
    conn= sqlite3.connect('facebook.db')
    rec=delete_entry.get()
    c=conn.cursor()
    c.execute('''UPDATE user SET
                firstName=:firstName,
                lastName=:lastName,
                age =:age,
                adress =:adress,
                city =:city,
                Zipcode =:Zipcode,
                password =:password,
                gender =:gender
                WHERE oid= :oid''',
            {'firstName':firstname_edit.get(),
            'lastName':lastname_edit.get(),
            'age':age_edit.get(),
            'adress':address_edit.get(),
            'city':city_edit.get(),
            'Zipcode':zipcode_edit.get(),
            'password':password_edit.get(),
            'gender':gender_edit.get(),
            'oid':rec
            }
        )
        # print('success','deleted')
        # c.execute('select *,oid from user_data')
        # record=c.fetchall()
        # print(record)
    conn.commit()
    conn.close()
    editor.destroy()






def edit():
    global editor 
    editor=Toplevel()
    editor.title('Update data')
    editor.geometry('300x400')

    conn=sqlite3.connect('facebook.db')
    c=conn.cursor()
    rec=delete_entry.get()
    c.execute("select * from user where oid="+rec)
    records=c.fetchall()
    print(records)

    global firstname_edit
    global lastname_edit
    global age_edit
    global address_edit
    global city_edit
    global zipcode_edit
    global password_edit
    global gender_edit

    firstname_edit= Entry(editor, width=30)
    firstname_edit.grid(row=1,column=1,padx=20,pady=5)

    lastname_edit=Entry(editor,width=30)
    lastname_edit.grid(row=2,column=1,pady=5)

    age_edit=Entry(editor,width=30)
    age_edit.grid(row=3,column=1,pady=5)

    address_edit=Entry(editor,width=30)
    address_edit.grid(row=4,column=1,pady=5)

    city_edit=Entry(editor,width=30)
    city_edit.grid(row=5,column=1,pady=5)

    zipcode_edit=Entry(editor,width=30)
    zipcode_edit.grid(row=6,column=1,pady=5)

    password_edit=Entry(editor,width=30)
    password_edit.grid(row=7,column=1,pady=5)

    gender_edit=Entry(editor,width=30)
    gender_edit.grid(row=8,column=1,pady=5)

    fnamelabel= Label(editor,text="firstname")
    fnamelabel.grid(row=1,column=0)

    lastnamelabel= Label(editor,text="lastname")
    lastnamelabel.grid(row=2,column=0)

    agelabel= Label(editor,text="age")
    agelabel.grid(row=3,column=0)

    addresslabel= Label(editor,text="address")
    addresslabel.grid(row=4,column=0)

    citylabel= Label(editor,text="city")
    citylabel.grid(row=5,column=0)

    zipcodelabel= Label(editor,text="zipcode")
    zipcodelabel.grid(row=6,column=0)

    passwordlabel= Label(editor,text="password")
    passwordlabel.grid(row=7,column=0)

    genderlabel= Label(editor,text="gender")
    genderlabel.grid(row=8,column=0)

    sub_btn=Button(editor,text='Submit',command=update)
    sub_btn.grid(row=9,column=0,columnspan=2)
    for record in records:
        firstname_edit.insert(0,record[0])
        lastname_edit.insert(0,record[1])
        age_edit.insert(0,record[2])
        address_edit.insert(0,record[3])
        city_edit.insert(0,record[4])
        zipcode_edit.insert(0,record[5])
        password_edit.insert(0,record[6])
        gender_edit.insert(0,record[7])


    conn.commit()
    conn.close()




firstname= Entry(root, width=30)
firstname.grid(row=1,column=1,padx=20,pady=5)

lastname=Entry(root,width=30)
lastname.grid(row=2,column=1,pady=5)

age=Entry(root,width=30)
age.grid(row=3,column=1,pady=5)

address=Entry(root,width=30)
address.grid(row=4,column=1,pady=5)

city=Entry(root,width=30)
city.grid(row=5,column=1,pady=5)

zipcode=Entry(root,width=30)
zipcode.grid(row=6,column=1,pady=5)

password=Entry(root,width=30)
password.grid(row=7,column=1,pady=5)

gender=Entry(root,width=30)
gender.grid(row=8,column=1,pady=5)

fnamelabel= Label(root,text="firstname")
fnamelabel.grid(row=1,column=0)

lastnamelabel= Label(root,text="lastname")
lastnamelabel.grid(row=2,column=0)

agelabel= Label(root,text="age")
agelabel.grid(row=3,column=0)

addresslabel= Label(root,text="address")
addresslabel.grid(row=4,column=0)

citylabel= Label(root,text="city")
citylabel.grid(row=5,column=0)

zipcodelabel= Label(root,text="zipcode")
zipcodelabel.grid(row=6,column=0)

passwordlabel= Label(root,text="password")
passwordlabel.grid(row=7,column=0)

genderlabel= Label(root,text="gender")
genderlabel.grid(row=8,column=0)

deletelabel= Label(root,text="delete")
deletelabel.grid(row=10,column=0)

sub_btn=Button(root,text='Submit',command=submit)
sub_btn.grid(row=9,column=0,columnspan=2)

delete_entry=Entry(root,width=30)
delete_entry.grid(row=10,column=1,pady=5)


sub_btn=Button(root,text='delete',command=delete)
sub_btn.grid(row=11,column=0,columnspan=2)
sub_btn=Button(root,text='show',command=show)
sub_btn.grid(row=12,column=0,columnspan=2)
sub_btn=Button(root,text='edit',command=edit)
sub_btn.grid(row=13,column=0,columnspan=2)



com.commit()
com.close()

root.mainloop()









