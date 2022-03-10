from tkinter import *
from tkinter import ttk

root = Tk()
root.overrideredirect(True)
root.geometry("400x200+200+200")
root.attributes("-topmost", True)

def get_pos(event):
    global xwin 
    global ywin

    xwin = event.x
    ywin = event.y

def move_window(event):
    root.geometry(f"+{event.x_root - xwin}+{event.y_root - ywin}")

def createList():
    completeButton["state"] = "normal"
    dailyTasks = []
    tName = listbox.curselection()
    for i in tName:
        op = listbox.get(i)
        dailyTasks.append(op)

    for item in range(len(dailyTasks)):
        listbox2.insert(END, dailyTasks[item])
        listbox2.itemconfig(item, bg="#bdc1d6")
    listbox2.pack()
    listbox2.lift()
    selectToDo()
    createButton["state"] = "disabled"

def selectToDo():
    tabControl.select(1)

def selectListTasks():
    tabControl.select(0)
    createButton["state"] = "normal"

def deleteItem():
    if listbox2.size() == 1:
        completeButton["state"] = "disabled"
        listbox2.delete(listbox2.curselection())
    else:
        selected_item= listbox2.curselection()
        for item in selected_item[::-1]:
            listbox2.delete(item)

        if listbox2.size() == 0:
            completeButton["state"] = "disabled"
    
title_bar = Frame(root, bg="grey10", relief="raised", bd=1, cursor="@aero_arrow.cur")
title_bar.pack(expand=1, fill=X)
title_label = Label(title_bar, text="Quest Helper", font="Arial", bg="grey10", fg="light goldenrod")
title_label.pack(side=LEFT)
title_bar.bind("<B1-Motion>", move_window)
title_bar.bind("<Button-1>", get_pos)

close_button = Button(title_bar, text="X", command=root.destroy, cursor="@aero_link.ani", bg="grey10", fg="white")
close_button.pack(side=RIGHT)

tabControl = ttk.Notebook(root, cursor="@aero_arrow.cur")
tab1 = Frame(tabControl)
tabControl.add(tab1,text="Daily Una Tasks")
tabControl.pack(expand=1, fill="both")

tab2 = Frame(tabControl)
tabControl.add(tab2, text="Una Task To-Do")

createButton = Button(tab1, text="Create", command=createList, cursor="@aero_link.ani")
createButton.pack(side=BOTTOM)

completeButton = Button(tab2, text="Complete", command=deleteItem)
completeButton.pack(side=BOTTOM)

homeButton = Button(tab2, text="Home", command= selectListTasks)
homeButton.pack(side=BOTTOM)

taskList = ["nacho", "sandwich", "burger", "pizza", "JOHNSON"]
listbox = Listbox(tab1, selectmode="multiple", height= 20, width=50, bg = "white", activestyle="dotbox", font="Arial", fg = "black", cursor="@aero_arrow.cur")
for item in range(len(taskList)):
    listbox.insert(END, taskList[item])
    listbox.itemconfig(item, bg="#bdc1d6")
listbox.pack()

listbox2 = Listbox(tab2, selectmode="multiple", height= 20, width=50, bg = "white", activestyle="dotbox", font="Arial", fg = "black", cursor="@aero_arrow.cur")

root.mainloop()