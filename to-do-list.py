from tkinter import *
import sqlite3 as db
import time

win=Tk()
win.title('To-Do-List')
win.config(bg='#5c74e4')
win.geometry('750x560')
win.resizable(0,0)

# function to add task in the task-listbox
def add():
    to_do=textfield.get(1.0,END)
    task.insert(END,to_do)
    
    con=db.connect("test.db")
    cur=con.cursor()
    query="insert into task values (:todo)"
    insert={'todo':to_do}
    cur.execute(query,insert)
    con.commit()
    con.close()
    
    textfield.delete(1.0,END)
    
# function to add task in the task-listbox using enter
def add_enter(event):
    to_do=textfield.get(1.0,END)
    task.insert(END,to_do)

    con=db.connect("test.db")
    cur=con.cursor()
    query="insert into task values (:todo)"
    insert={'todo':to_do}
    cur.execute(query,insert)
    con.commit()
    con.close()

    textfield.delete(1.0,END)
    
# function to delete task from the task-listbox
def delete():
    to_delete=task.get(ANCHOR)
    task.delete(ANCHOR)
    
    con=db.connect("test.db")
    cur=con.cursor()
    query="delete from task where title='"+to_delete+"'"
    cur.execute(query)
    con.commit()
    con.close()

# function to delete all the task from the task-listbox
def delete_all():
    task.delete(0,END)

    con=db.connect("test.db")
    cur=con.cursor()
    query="delete from task"
    cur.execute(query)
    con.commit()
    con.close()

# function to retrieve data of task list-box from the database
def retrieve():
    con=db.connect("test.db")
    cur=con.cursor()
    query="select * from task"
    cur.execute(query)
    result=cur.fetchall()
    for rec in result:
        task.insert(END,rec[0])  
    con.commit()
    con.close()

# function to display date and time
def date_and_time():
    date=time.strftime('%A, %B %d')
    mycanvas.create_text(150,100,text=date,font=('times 20 bold'),fill='white')
    
# canvas for head title
mycanvas=Canvas(win,width=415,height=140,bg='#122b63',highlightthickness=0)
mycanvas.pack(anchor=NW,padx=30,pady=30)

# create text in canvas
mycanvas.create_text(150,40,text='Task-To-Do',font=('times 40 bold'),fill='white')

# frame for task
task_frame=Frame(win,bg='#122b63')
task_frame.place(x=30,y=190)

# Declaring Scrollbar for the task-listbox
myScrollbar=Scrollbar(task_frame,orient=VERTICAL)

# listbox for tasks
task=Listbox(task_frame,font=('Helvetica 20 bold'),width=25,activestyle='none',selectbackground='#122b63',yscrollcommand=myScrollbar.set,highlightthickness=0)

# configuring the Scrollbar and pack on the window
myScrollbar.config(command=task.yview)
myScrollbar.pack(side=RIGHT,fill=Y)

# Packing task-listbox 
task.pack(padx=10,pady=10)

# textbox to write task
textfield=Text(win,height=2,width=30,font=('Helvetica 12 bold'),bd=3,)
textfield.place(x=460,y=30)

# button to add task
add_task=Button(win,text='Add Task',width=14,font=('Helvetica 12 bold'),bd=5,bg='#122b63',fg='white',command=add)
add_task.place(x=525,y=100)

# button to delete task
delete_task=Button(win,text='Delete Task',width=14,font=('Helvetica 12 bold'),bd=5,bg='#122b63',fg='white',command=delete)
delete_task.place(x=525,y=160)

# button to delete all the task
delete_all_task=Button(win,text='Delete All Task',width=14,font=('Helvetica 12 bold'),bd=5,bg='#122b63',fg='white',command=delete_all)
delete_all_task.place(x=525,y=220)

# button to close the application
close=Button(win,text='Close',width=14,font=('Helvetica 12 bold'),bd=5,bg='#122b63',fg='white',command=win.quit)
close.place(x=525,y=280)

# binding enter key to add task in task-listbox
win.bind('<Return>',add_enter)

# Retreiving data of task list-box from the database
retrieve()


date_and_time()

# mainloop to keep the window open
win.mainloop()
