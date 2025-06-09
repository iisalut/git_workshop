
from tkinter import *
from tkmacosx import Button # needed for bg to appear cuz mac overides some stuff
from tkinter import ttk
# count=0
# def click():
#     global count
#     count+=1
#     lcount.configure(text=count)# actually updates the count
#     if count==10:
#         lcount.configure(text="kaboom")
#         button.configure(state=DISABLED)
#
#
window = Tk() # instance of a window
window.geometry("420x420") # size

window.title("app") # gives title # all attributes need to come  before mainloop to actually show up
window.configure(bg="#fce172") # background color
photo= PhotoImage(file="wave_border_beyondwords.png")
label= Label(window, text="Tulasii APP",
             font=('Arial',40,'italic'),
             fg='blue',
             bg='yellow',
             relief="sunken",
             bd= 20,
             padx=20,
             pady=20)  # just makes label but doesnt add it to the window itself

label.pack()#label.place(x=100, y=100) # actually places it into the window


#label to show count inc
lcount= Label(window, text=count,padx=20,pady=20, bg="#fce172",font=('Arial',20,'bold'))
lcount.pack()


#button that inc the count
button = Button(window,text='click me')
button.pack()
button.config(command=click)# uses def click
button.config(font=('Ink Free', 30, 'bold'))
button.config(bg='#fce172')  # Button background color
button.config(fg='#ed9a2d')  # Button text color
button.config(activebackground='#FF0000')  # Highlight background
button.config(activeforeground='pink')
button.config(focuscolor='', borderless=1)# removes that annoying blue ring
#button.config(image=photo)
button.config(relief="flat")# Active text color when clicked

#ENTRY WIDGET
entry=Entry()
entry.pack()
entry.config(font=('Ink Free',15))
#entry.insert(0,'hello :)') # default text appears
#entry.config(show='*')# when you type in password
entry.configure(bg='#a47fdb',fg='#ed9a2d')
#submit button

def submit():
    global username
    username=entry.get()#gets userinput
    userlab.configure(text="hi "+username+" pleasure to meet you !")




submit=Button(window,text='submit',command=submit)
submit.pack()
userlab=Label(window,text=" ",font=('Arial',20,'bold'), bg='#fce172',fg='#ed9a2d')
userlab.pack()


notebook=ttk.Notebook(window) #widget that manages collections of windows
tab1= Frame(notebook)#tab1
tab2=Frame(notebook)
notebook.add(tab1, text='tab1')
notebook.add(tab2, text='tab2')
notebook.pack()
Label(tab1, text="hello", width= 50, height=25).pack()
Label(tab2, text="there", width= 50, height=25).pack()


# # --- Functions to switch pages ---
# page1=Frame(window)
# page1.config(bg='blue',width=300,height=300)
# page2=Frame(window)
# page2.config(bg='red',width=300,height=300)
#
# for frame in (page1,page2):
#     frame.grid(row=0, column=0, sticky='nsew')
# def show(frame):
#     frame.tkraise()
# show(page1)
# btn1=Button(page1,text='click for pg2',command=lambda:show(page2)).grid(row=0,column=0,sticky='w')
# btn2=Button(page2,text='click for pg1',command=lambda:show(page1)).grid(row=0,column=0,sticky='w')
# window.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand vertically
# window.grid_columnconfigure(0, weight=1) # Allow column 0 to expand horizontally






window.mainloop() # place window on computer screen

