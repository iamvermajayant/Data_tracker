from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id = e_id.get()
    pname = e_pname.get()
    tno = e_tno.get()
    amount =e_amount.get()
    date = e_date.get()
    id = str(id)
    if(id == "" or pname == "" or tno == "" or amount == "" or len(id) > 9):
        MessageBox.showinfo("ERROR", "please fill all the information or check the policy no length")
    else:
        con = mysql.connect(host = "localhost", user="root", password = "Pizza@13", database = "lms")
        cursor = con.cursor()
        cursor.execute("insert into detail values ('"+ id +"','"+ pname +"', '"+ tno +"', '"+ amount +"','"+ date +"')")
        cursor.execute("commit")

        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_tno.delete(0,'end')
        e_amount.delete(0,'end')
        e_date.delete(0,'end')
        show()
        MessageBox.showinfo("insert status", "inserted sucessfully")
        con.close()

def delete():
    if(e_id.get() == "" and e_pname.get() == ""):
        MessageBox.showinfo("Delete status", "id is compulsory for delete")
    else:
        con = mysql.connect(host = "localhost", user="root", password = "Pizza@13", database = "lms")
        cursor = con.cursor()
        cursor.execute("delete from detail where id = ('"+ e_id.get() +"')")
        cursor.execute("delete from detail where name = ('"+ e_pname.get() +"')")
        cursor.execute("commit")

        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_tno.delete(0,'end')
        e_amount.delete(0,'end')
        e_date.delete(0,'end')
        show()
        MessageBox.showinfo("Delete status", "Deleted sucessfully")
        con.close()

def update():
    id = e_id.get()
    pname = e_pname.get()
    tno = e_tno.get()
    amount =e_amount.get()
    date = e_date.get()

    if(id == "" or pname == "" or tno == "" or amount == ""):
        MessageBox.showinfo("update status", "all information is compulsory for updation")
    else:
        con = mysql.connect(host = "localhost", user="root", password = "Pizza@13", database = "lms")
        cursor = con.cursor()
        cursor.execute("update detail set name = '"+ pname +"', regno ='"+ tno +"', dept = '"+ amount +"', date = '"+ date +"' where id = '"+ id +"' ")
        cursor.execute("commit")

        e_id.delete(0,'end')
        e_pname.delete(0,'end')
        e_tno.delete(0,'end')
        e_amount.delete(0,'end')
        e_date.delete(0,'end')

        show()
        MessageBox.showinfo("Update status", "Updated sucessfully")
        con.close()

def get():
    if(e_id.get() == ""):
        MessageBox.showinfo("Fetch status", "desired result shown")
    else:
        con = mysql.connect(host = "localhost", user="root", password = "Pizza@13", database = "lms")
        cursor = con.cursor()
        cursor.execute("select * from detail where id = '"+e_id.get()+"' ")
        rows = cursor.fetchall()

        for row in rows:
        #    e_id.insert(0,row[1])
            e_pname.insert(0,row[1])
            e_tno.insert(0,row[2])
            e_amount.insert(0,row[3])
            e_date.insert(0,row[4])
        con.close()
#        MessageBox.showinfo("Delete status", "Deleted sucessfully")
#        con.close()

def clear():
    e_id.delete(0,'end')
    e_pname.delete(0,'end')
    e_tno.delete(0,'end')
    e_amount.delete(0,'end')
    e_date.delete(0,'end')
    MessageBox.showinfo("clear status", "all fields are clear")

def show():
    con = mysql.connect(host = "localhost", user="root", password = "Pizza@13", database = "lms")
    cursor = con.cursor()
    cursor.execute("select * from detail")
    rows = cursor.fetchall()
    list.delete(0,list.size())

    for row in rows:
        insertData =str(row[0])+'      '+str(row[1])+'      '+str(row[2])+'      '+str(row[3])+'       '+str(row[4])
        list.insert(list.size(), insertData)

    con.close()

def newwindow():
    newwindow = Toplevel(root)
    newwindow.title("About us")
    newwindow.geometry("350x200")

    l = Label(newwindow, text= "About us",font =("arial",25,"bold"))
    l1 = Label(newwindow, text ="This application will help you in\n keeping the tracks of your daily LIC \n Transaction",font=("arial",10))
    l1.place(x=20, y= 50)
    l.place(x=20,y=15)



root = Tk()
root.geometry("900x400")
root.title("LIC DATA ENTRY")
root.configure(bg='orange')

lbl = Label(root, text="LIC of India",bg=('yellow'),fg=("Blue"), font=("helvetica",25,"bold"))
lbl.place(x=300, y = 5)
id = Label(root, text = "Policy no : ", font = ("bold", 15))
id.place(x= 20 , y=70)

pname = Label(root, text = "Name : ", font = ("bold", 15))
pname.place(x= 20 , y=100)

tno = Label(root, text = "Transaction no : ", font = ("bold", 15))
tno.place(x= 20 , y=130)

amount = Label(root, text = "Amount : ", font = ("bold", 15))
amount.place(x= 20 , y=160)

date = Label(root, text ="Date : ", font =("bold",15))
date.place(x=20, y =190)
e_id = Entry(bd=4)
e_id.place(x=180, y=70)

e_pname = Entry(bd=4)
e_pname.place(x=180, y=100)

e_tno = Entry(bd=4)
e_tno.place(x=180, y=130)

e_amount = Entry(bd=4)
e_amount.place(x=180, y=160)

e_date = Entry(bd=4)
e_date.place(x=180, y= 190)

insert = Button(root, text = "Insert Data", font=("italic",10), bg="Red", command= insert)
insert.place(x=20, y =230 )

delete = Button(root, text = "Delete Data", font=("italic",10), bg="Red", command= delete)
delete.place(x=110, y =230 )

update = Button(root, text = "Update Data", font=("italic",10), bg="Red", command= update)
update.place(x=205, y =230 )

get = Button(root, text = "Fetch Data", font=("italic",10), bg="Red", command= get)
get.place(x=110, y =300 )

clear = Button(root, text = "clear Data", font=("italic",10), bg="Red", command= clear)
clear.place(x=20, y =300 )

list = Listbox(root, height = 15, width = 65, bd = 5, bg = "cadet blue", font = ("arial", 11))
list.place(x = 340 , y = 70 )
show()

nwindow = Button(root, text = "About  Us", font=("italic",10), bg="Red", command= newwindow)
nwindow.place(x = 205, y =300 )

#root.resizable(0, 0)


mainloop()
