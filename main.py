import tkinter

window = tkinter.Tk()
window.title("Unit converter")
window.minsize(width=500, height=300)

####LABEL
my_label = tkinter.Label(text="Convertor", font=("Arial", 24, "bold"))
my_label.pack(side="top")

# import turtle
# tim = turtle.Turtle()
# tim.write("Some text")

# my_label["text"] = "New text"
# my_label.config(text="New text 2")


###BUTTON

def button_clicked():
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()


###ENTRY
input = tkinter.Entry(width=10)
input.pack()
# print(input.get())

window.mainloop()