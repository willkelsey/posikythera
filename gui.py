from tkinter import *

def display_info(planet):
    ourMessage = ''+planet+''
    messageVar = Message(root, text=ourMessage)
    messageVar.config(bg='lightgreen')
    # messageVar.pack()

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
var1 = IntVar()
Checkbutton(root, text='Earth', variable=var1, command=display_info("Earth")).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(root, text='Moon', variable=var2, command=display_info("Moon")).grid(row=1, sticky=W)
# w = Scale(root, from_=0, to=2020, orient=HORIZONTAL)
# w.pack()
mainloop()