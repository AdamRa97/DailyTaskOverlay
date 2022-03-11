from tkinter import *
from tkinter import ttk
from webbrowser import get
from playsound import playsound

root = Tk()
style = ttk.Style()
style.theme_create("yummy", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2,5,2,0]}},
    "TNotebook.Tab": {
        "configure": {"foreground":"white","background": "RoyalBlue3", "font": ("Arial", "11", "bold")},
        "map":       {"background": [("selected", "RoyalBlue3")],
                      "expand": [("selected", [1,1,1,0])]}
    }
})
style.theme_use("yummy")
root.overrideredirect(True)
root.geometry("450x300+200+200")
root.configure(background="grey99",cursor="@aero_arrow.cur")
root.attributes("-topmost", True)
root.attributes("-alpha", 1)

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
    
    # if tName[0] != None:
    try: 
        if tName[0] != None:
            for item in range(len(dailyTasks)):
                listbox2.insert(END, dailyTasks[item])
            listbox2.pack()
            listbox2.lift()
            selectToDo()
            createButton["state"] = "disabled"
    except Exception:
        pass


def selectToDo():
    tabControl.select(1)
    tabControl.hide(0)

def selectListTasks():
    tabControl.select(0)
    createButton["state"] = "normal"
    listbox2.delete(0,END)
    tabControl.hide(1)

def deleteItem():
    if listbox2.size() == 1 and listbox2.curselection():
        completeButton["state"] = "disabled"
        listbox2.delete(listbox2.curselection())
    else:
        selected_item= listbox2.curselection()
        for item in selected_item[::-1]:
            listbox2.delete(item)

        if listbox2.size() == 0:
            completeButton["state"] = "disabled"

def tranSlideVal(val):
    root.attributes("-alpha", int(val)*.1)

def clickPlayList(e):
    playsound("click.mp3",False)

def hoverPlay(event):
    playsound("hover.mp3", False)

def getTxtInput():
    input = addTxtBox.get("1.0", "end-1c")
    return input

def addCharTab():
    newTab = Frame(tabControl)
    if getTxtInput() != "":
        tabControl.add(newTab,text=getTxtInput())
    
    
titleBar = Frame(root, bg="grey10", relief="raised", bd=1, cursor="@aero_arrow.cur")
titleBar.pack(expand=1, fill=X)
titleLabel = Label(titleBar, text="Quest Helper", font="Arial", bg="grey10", fg="light goldenrod")
titleLabel.pack(side=LEFT)
versionLabel = Label(titleBar, text="v0.3 Alpha", font="Arial", bg="grey10", fg="light goldenrod")
versionLabel.pack(side=LEFT)
titleBar.bind("<B1-Motion>", move_window)
titleBar.bind("<Button-1>", get_pos)

closeButton = Button(titleBar, text="X", command=root.destroy, cursor="@aero_link.ani", bg="grey10", fg="white")
closeButton.bind("<Enter>", hoverPlay)
closeButton.bind("<Button-1>",clickPlayList)
closeButton.pack(side=RIGHT)

currentValue = DoubleVar()
transLabel = Label(root, text="Transparency", font="Arial", cursor="@aero_arrow.cur")
transLabel.pack(anchor="w", side="bottom")
tranSlider = Scale(root, from_=1, to= 10, font="Arial", orient="horizontal", cursor="@aero_arrow.cur", variable=currentValue, command=tranSlideVal,background="grey99")
tranSlider.bind("<Button-1>",clickPlayList)
tranSlider.bind("<Enter>",hoverPlay)
tranSlider.set(10)
tranSlider.pack(anchor="sw", side="bottom")

scrollBar= Scrollbar(root, cursor="@aero_arrow.cur",background="grey99")
scrollBar.bind("<Button-1>",clickPlayList)
scrollBar.pack(side=RIGHT,fill=Y)

tabControl = ttk.Notebook(root, cursor="@aero_arrow.cur")
tab1 = ttk.Frame(tabControl)
tabControl.bind("<Button-1>", clickPlayList)
tabControl.add(tab1,text="Daily Una Tasks")
tabControl.pack()

tab2 = Frame(tabControl)
tabControl.add(tab2, text="Una Task To-Do")
tabControl.hide(1)

addChar = Button(tab1, text="Add Char", font="Arial", command=addCharTab)
addChar.bind("<Enter>",hoverPlay)
addChar.bind("<Button-1>",clickPlayList)
addChar.pack(anchor="ne", side="right")
addTxtBox = Text(tab1, height=2, width=15)
addTxtBox.pack(anchor="ne",side="right")

createButton = Button(tab1, text="Create", font="Arial", command=createList, cursor="@aero_link.ani")
createButton.bind("<Enter>",hoverPlay)
createButton.bind("<Button-1>",clickPlayList)
createButton.pack(anchor="s", side="bottom")

completeButton = Button(tab2, text="Complete", font="Arial", command=deleteItem, cursor="@aero_link.ani")
completeButton.bind("<Enter>",hoverPlay)
completeButton.bind("<Button-1>",clickPlayList)
completeButton.pack(side=BOTTOM)

homeButton = Button(tab2, text="Home", font="Arial", command=selectListTasks, cursor="@aero_link.ani")
homeButton.bind("<Enter>",hoverPlay)
homeButton.bind("<Button-1>",clickPlayList)
homeButton.pack(side=BOTTOM)

taskList = ["nacho", "sandwich", "burger", "pizza", "tacos", "Madness Piles on the Altar", "Fairy's Friend", "Bleak Night Fog"]
taskList.sort()
listbox = Listbox(tab1, yscrollcommand = scrollBar.set, selectmode="multiple", height= 30, width=50, bg = "grey99", activestyle="dotbox", font="Arial", fg = "black", cursor="@aero_arrow.cur")
listbox.bind("<Button-1>", clickPlayList)
for item in range(len(taskList)):
    listbox.insert(END, taskList[item])
listbox.pack()

listbox2 = Listbox(tab2, selectmode="multiple", height= 20, width=50, bg = "grey99", activestyle="dotbox", font="Arial", fg = "black", cursor="@aero_arrow.cur")
listbox2.bind("<Button-1>", clickPlayList)
root.mainloop()