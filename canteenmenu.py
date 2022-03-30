import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Canteen import DbObject
import sys
import os
import date
from time import sleep
d=DbObject()
win=Tk()
win.iconbitmap("SC.ico")
win.eval('tk::PlaceWindow %s center' % win.winfo_toplevel())
win.withdraw()
win.destroy()
win.quit()
win.mainloop
def task():
    sleep(2) 
    root.destroy()
def task1():
    sleep(5) 
    root.destroy()
    sys.exit()
root = Tk()
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
root.title("Welcome")
windowWidth = 800
windowHeight = 500
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2.3 - windowHeight/2)
root.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))
canvas=Canvas(width=800,height=500,bg="blue")
canvas.pack()
fe=PhotoImage(file="Sc.png")
canvas.create_image(0,0, image=fe, anchor=NW)
def clicked(event):
    root.after(200, task)
    print("pressed")
buttonBG=canvas.create_oval(710, 410, 790, 490, outline="#696969",
            fill="#adadad", width=5)
buttonTXT = canvas.create_text(752, 450, text=">",font=("Purisa", 30))
canvas.tag_bind(buttonBG, "<Button-1>", clicked) ## when the square is clicked runs function "clicked".
canvas.tag_bind(buttonTXT, "<Button-1>", clicked) ## same, but for the text.
root.mainloop()
then=0
root=Tk()
root.title("Canteen Menu")
windowWidth = 800
windowHeight = 500
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2.3 - windowHeight/2)
root.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))
photo=PhotoImage(file="C://Users//Aadil//Pictures//Logo for CCA variant 1.png")
root.resizable("True","False")
root.iconbitmap("SC.ico")
mynote=ttk.Notebook(root)
mynote.pack()
Final=Frame(mynote)
wrap5=Frame(mynote)
wrapper4=Frame(mynote)
Final.configure(background='white')
#Intro
#Canteen
wrapper1=LabelFrame(wrapper4, text="Canteen Table")
wrapper2=LabelFrame(wrapper4, text="Search")
wrapper3=LabelFrame(wrapper4, text="Canteen Data")
wrapper4.pack(fill="both",expand="yes",padx=1,pady=1)
wrapper1.pack(fill="both",expand="yes",padx=1,pady=1)
wrapper2.pack(fill="both",expand="yes",padx=1,pady=1)
wrapper3.pack(fill="both",expand="yes",padx=1,pady=1)
#Students
wrap1=LabelFrame(wrap5, text="Students Table")
wrap2=LabelFrame(wrap5, text="Search")
wrap3=LabelFrame(wrap5, text="Students Data")
wrap5.pack(fill="both",expand="yes",padx=1,pady=1)
wrap1.pack(fill="both",expand="yes",padx=1,pady=1)
wrap2.pack(fill="both",expand="yes",padx=1,pady=1)
wrap3.pack(fill="both",expand="yes",padx=1,pady=1)
#Final
Finale1=LabelFrame(Final, text="Canteen Table")
Finale2=LabelFrame(Final, text="Search")
Finale3=LabelFrame(Final, text="Canteen Data")
Finale3.configure(background='#f7f7f7')
Final.pack(fill="both",expand="yes",padx=1,pady=1)
Finale1.pack(fill="both",expand="yes",padx=1,pady=1)
Finale2.pack(fill="both",expand="yes",padx=1,pady=1)
Finale3.pack(fill="both",expand="yes",padx=1,pady=1)
mynote.add(Final, text="Final")
mynote.add(wrapper4, text="Canteen Menu")
mynote.add(wrap5, text="Students Menu")
#FUNCTIONS For Canteen
def update(rows):
    tv.delete(*tv.get_children())
    for i in rows:
        tv.insert('','end',values=i)
def search():
    g=Id.get()
    rws=d.canteenidsearch(g)
    update(rws)
def clear():
    rws=d.canteenidsearch('')
    update(rws)
def getrow(event):
    rowid=tv.identify_row(event.y)
    item=tv.item(tv.focus())
    Idd.set(item['values'][0])
    ItemsName.set(item['values'][1])
    ItemsPrice.set(item['values'][2])
    ItemsStock.set(item['values'][3])
def updatec():
    if messagebox.askyesno("Confirmation !!!","Are you sure you want to Update this item"):
        d.UpdatCanteen(int(Idd.get()),ItemsName.get(),int(ItemsPrice.get()),int(ItemsStock.get()))
    else:
        return True
def addc():
    d.AddCanteenData(int(Idd.get()),ItemsName.get(),int(ItemsPrice.get()),int(ItemsStock.get()))
def deletec():
    if messagebox.askyesno("Confirmation !!!","Are you sure you want to delete this item"):
        d.dropcanteen(int(Idd.get()))
    else:
        return True
#FUNCTIONS For students
def supdate(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('','end',values=i)
def ssearch():
    g=Ids.get()
    rws=d.studentidsearch(g)
    supdate(rws)
def sclear():
    rws=d.studentidsearch('')
    supdate(rws)
def getrow1(event):
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    StudentsGr.set(item['values'][0])
    StudentsName.set(item['values'][1])
    StudentsBalance.set(item['values'][2])
def Supdatec():
    if messagebox.askyesno("Confirmation !!!","Are you sure you want to Update this item"):
        d.UpdatStudent(int(StudentsGr.get()),StudentsName.get(),int(StudentsBalance.get()))
    else:
        return True
def Saddc():
    d.AddStudentData(int(StudentsGr.get()),StudentsName.get(),int(StudentsBalance.get()))
def Sdeletec():
    if messagebox.askyesno("Confirmation !!!","Are you sure you want to delete this item"):
        d.dropstudent(int(StudentsGr.get()))
    else:
        return True
#FUNCTIONS For Final
def fupdate(rows):
    tfv.delete(*tfv.get_children())
    for i in rows:
        tfv.insert('','end',values=i)
def fupdate1(rows):
    tiv.delete(*tiv.get_children())
    for i in rows:
        tiv.insert('','end',values=i)
def fsearch():
    gr=fId.get()
    if not gr:
        messagebox.showerror("Error !!!", "Please type the Student GRNO. in Search and Try Again")
        return True
    rws=d.studentidsearch(gr)
    print(rws)
    try:
        if rws==[]:
            messagebox.showerror("Error !!!", "Please type the Student GRNO. in Search and Try Again")
            pass
        else:
            fupdate1(rws)
    except:
        pass
def fclear():
    rws=d.canteenidsearch('')
    fupdate(rws)
def f1clear():
    rws=d.studentidsearch('')
    fupdate1(rws)
def getrow4(event):
    rowid=tfv.identify_row(event.y)
    item=tfv.item(tfv.focus())
    fIdd.set(item['values'][0])
    fItemsName.set(item['values'][1])
    fItemsPrice.set(item['values'][2])
    fItemsStock.set(item['values'][3])
def Finalize():
    process.set("Initializing Finlaize")

    global then
    if fId.get()=="":
        messagebox.showerror("Warning!!!", "NO ID SELECTED")
        return True
    a=int(fQuantity.get())
    g=int(fItemsStock.get())
    t=g-a
    p=int(fItemsPrice.get())
    if g<=0:
        messagebox.showerror("Warning!!!", "NO STOCK")
        d.dropcanteen(int(fIdd.get()))
        fclear()
        return True
    else:
        d.UpdatCanteen(int(fIdd.get()),fItemsName.get(),int(fItemsPrice.get()),t)
        something=a*p
        then+=something
        fclear()
        last=int(d.FetchLastId())
        thenlast=last+1
        ko=date.givetime()
        print(ko)
        d.adddate(thenlast,int(fId.get()),int(fIdd.get()),a,ko)
        fItemsName.set("")
        fItemsPrice.set("")
        fQuantity.set("")
        process.set("Done or continue")
def Complete():
    global then
    process.set("Initializing Complete")
    v=d.studentbalancesearch(int(fId.get()))
    v=v-then
    d.UpdatStudentbalance(int(fId.get()),v)
    rws=[]
    fupdate1(rws)
    sclear()
    clear()
    then=0
    fId.set("")
    process.set("Completed Successfully")
def Datelog():
    a=d.Fetchdate()
    File=date.givepath()+"\\"+date.dategive()+".txt"
    previous=date.givepath()+"\\"+str(int(date.dategive())-1)+".txt"
    print(File)
    Filename=R"{}".format(File)
    FilenamePre=R"{}".format(previous)
    print(Filename)
    with open(Filename,"w+") as n:
        for inputs in a:
            string="("+"P"+str(inputs[0])+",GR"+str(inputs[1])+",I"+str(inputs[2])+",Q"+str(inputs[3])+","+(inputs[4])+")"
            print(string)
            n.write(string+"\n")
    try:
        if os.path.exists(Filename) and os.path.exists(FilenamePre):
            d.dropdate()
    except:
        pass
    messagebox.showerror("Data LOG!!!", "SAVED SUCCESSFULLY")
tv=ttk.Treeview(wrapper1, columns=(1,2,3,4),show="headings", height="10")
tv.pack()
tv.heading(1,text="ItemsNo")
tv.heading(2,text="ItemsName")
tv.heading(3,text="ItemsPrice")
tv.heading(4,text="ItemsStock")
tv.bind("<Double-1>",getrow)
trv=ttk.Treeview(wrap1, columns=(1,2,3),show="headings", height="10")
trv.pack()
trv.heading(1,text="StudentsGr")
trv.heading(2,text="StudentsName")
trv.heading(3,text="StudentsBalance")
trv.bind("<Double-1>",getrow1)
#treeview for final
tfv=ttk.Treeview(Finale1, columns=(1,2,3,4),show="headings", height="10")
tfv.pack()
tfv.heading(1,text="ItemsNo")
tfv.heading(2,text="ItemsName")
tfv.heading(3,text="ItemsPrice")
tfv.heading(4,text="ItemsStock")
tfv.bind("<Double-1>",getrow4)
tiv=ttk.Treeview(Finale2, columns=(1,2,3),show="headings", height="1")
tiv.pack(side=tk.BOTTOM,pady=3)
tiv.heading(1,text="StudentsGr")
tiv.heading(2,text="StudentsName")
tiv.heading(3,text="StudentsBalance")
#search section
Id=StringVar()
label1=Label(wrapper2, text="Search")
label1.pack(side=tk.LEFT, padx=10)
ent1=Entry(wrapper2,textvariable=Id)
ent1.pack(side=tk.LEFT, padx=6)
btn=Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT, padx=6)
cbtn=Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)
#Data Section
Idd=StringVar()
ItemsName=StringVar()
ItemsPrice=StringVar()
ItemsStock=StringVar()
label1=Label(wrapper3, text="ItemsNo")
label1.grid(row=0,column=1)
ent1=Entry(wrapper3,textvariable=Idd)
ent1.grid(row=0,column=2)
label2=Label(wrapper3, text="ItemsName")
label2.grid(row=1,column=1)
ent2=Entry(wrapper3,textvariable=ItemsName)
ent2.grid(row=1,column=2)
label3=Label(wrapper3, text="ItemsPrice")
label3.grid(row=2,column=1)
ent3=Entry(wrapper3,textvariable=ItemsPrice)
ent3.grid(row=2,column=2)
label4=Label(wrapper3, text="ItemsStock")
label4.grid(row=3,column=1)
ent4=Entry(wrapper3,textvariable=ItemsStock)
ent4.grid(row=3,column=2)
update_btn=Button(wrapper3, text="New", command=addc)
try:
    update_btn.pack(side=tk.LEFT, padx=6)
except:
    update_btn.grid(row=4, column=1, padx=6, pady=3)
abtn=Button(wrapper3, text="Update", command=updatec)
abtn.grid(row=4, column=2, padx=6, pady=3)
dbtn=Button(wrapper3, text="Delete", command=deletec)
dbtn.grid(row=4, column=3, padx=6, pady=3)
#Students search section
Ids=StringVar()
slabel1=Label(wrap2, text="Search")
slabel1.pack(side=tk.LEFT, padx=10)
sent1=Entry(wrap2,textvariable=Ids)
sent1.pack(side=tk.LEFT, padx=6)
sbtn=Button(wrap2, text="Search", command=ssearch)
sbtn.pack(side=tk.LEFT, padx=6)
scbtn=Button(wrap2, text="Clear", command=sclear)
scbtn.pack(side=tk.LEFT, padx=6)
#Students Data Section
StudentsGr=StringVar()
StudentsName=StringVar()
StudentsBalance=StringVar()
slabel1=Label(wrap3, text="StudentsGr")
slabel1.grid(row=0,column=1)
sent1=Entry(wrap3,textvariable=StudentsGr)
sent1.grid(row=0,column=2)
slabel2=Label(wrap3, text="StudentsName")
slabel2.grid(row=1,column=1)
sent2=Entry(wrap3,textvariable=StudentsName)
sent2.grid(row=1,column=2)
slabel3=Label(wrap3, text="StudentsBalance")
slabel3.grid(row=2,column=1)
sent3=Entry(wrap3,textvariable=StudentsBalance)
sent3.grid(row=2,column=2)
supdate_btn=Button(wrap3, text="New", command=Saddc)
try:
    supdate_btn.pack(side=tk.LEFT, padx=6)
except:
    supdate_btn.grid(row=4, column=1, padx=6, pady=3)
sabtn=Button(wrap3, text="Update", command=Supdatec)
sabtn.grid(row=4, column=2, padx=6, pady=3)
sdbtn=Button(wrap3, text="Delete", command=Sdeletec)
sdbtn.grid(row=4, column=3, padx=6, pady=3)
#search section for Final
fId=StringVar()
flabel1=Label(Finale2, text="Search")
flabel1.pack(side=tk.LEFT, padx=10)
fent1=Entry(Finale2,textvariable=fId)
fent1.pack(side=tk.LEFT, padx=6)
fbtn=Button(Finale2, text="Search", command=fsearch)
fbtn.pack(side=tk.LEFT, padx=6)
fcbtn=Button(Finale2, text="Clear", command=f1clear)
fcbtn.pack(side=tk.LEFT, padx=6)
#Data Section for Final
fIdd=StringVar()
fItemsName=StringVar()
fItemsPrice=StringVar()
fItemsStock=StringVar()
fQuantity=StringVar()
process=StringVar()
'''flabel1=Label(Finale3, text="ItemsNo")
flabel1.grid(row=0,column=1)
fent1=Label(Finale3,textvariable=fIdd)
fent1.grid(row=0,column=2)'''
flabel2=Label(Finale3, text="ItemsName")
flabel2.grid(row=0,column=1)
fent2=Label(Finale3,textvariable=fItemsName)
fent2.grid(row=0,column=2)
flabel3=Label(Finale3, text="ItemsPrice")
flabel3.grid(row=1,column=1)
fent3=Label(Finale3,textvariable=fItemsPrice)
fent3.grid(row=1,column=2)
flabel4=Label(Finale3, text="Quantity")
flabel4.grid(row=2,column=1)
fent4=Entry(Finale3,textvariable=fQuantity)
fent4.grid(row=2,column=2)
flabel9=Label(Finale3, text="Process > ")
flabel9.grid(row=2,column=8,padx=1)
flabel9=Label(Finale3, textvariable=process)
process.set("Welcome, GET to display Canteen Items")
flabel9.grid(row=2,column=9)
fibtn=Button(Finale3, text="Finalize", command=Finalize)
fibtn.grid(row=3,column=2,pady=5)
ficbtn=Button(Finale3, text="Done and Clear", command=Complete)
ficbtn.grid(row=3,column=3,pady=5)
fsbtn=Button(Finale3, text="SAVE DATE LOG", command=Datelog)
fsbtn.grid(row=3,column=13,pady=5)
fidbtn=Button(Finale3, text="GET", command=fclear)
fidbtn.grid(row=3,column=7,padx=40,pady=5)
root.mainloop()
root = Tk()
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
root.title("Welcome")
windowWidth = 800
windowHeight = 500
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2.3 - windowHeight/2)
root.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,positionRight, positionDown))
canvas=Canvas(width=800,height=500,bg="blue")
canvas.pack()
fej=PhotoImage(file="Doneby.png")
canvas.create_image(0,0, image=fej, anchor=NW)
root.after(1000, task1)
root.mainloop()



