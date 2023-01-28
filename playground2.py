import tkinter


def button_clicked():
    my_label.config(text=input.get())

def button_clicked_2():
    my_label.config(text="Titlu")

window = tkinter.Tk()
window.title("Playground")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

####LABEL
my_label = tkinter.Label(text="Titlu", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# my_label.config(padx=10, pady=10)

###BUTTON1
button = tkinter.Button(text="Schimba", command=button_clicked)
button.grid(column=0, row=4)

###BUTTON2
button = tkinter.Button(text="Cancel", command=button_clicked_2)
button.grid(column=1, row=4)

###ENTRY
input = tkinter.Entry(width=10)
input.grid(column=0, row=1)

window.mainloop()
