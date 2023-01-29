from tkinter import *


def convert():
    input_val = miles_input.get()
    if input_val != "":
        input_val = float(miles_input.get())
        if input_val >= 0:
            if checked_state.get() == 0:
                val = input_val * 1.609344
            else:
                val = round(input_val * 1.609344)
            label11.config(text=val)
            label_error = Label(text="                                            ")
            label_error.grid(row=4, column=0)
    elif input_val == "":
        label_error = Label(text="Nu ati introdus o valoare.", fg="red")
        label_error.grid(row=4, column=0)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# ENTRY (0,1) # input miles to convert
miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

# LABEL (0,2) # "Miles"
label02 = Label(text="Miles")
label02.grid(row=0, column=2)

# LABEL (1, 0) # "is equal to"
label10 = Label(text="is equal to ")
label10.grid(row=1, column=0)

# LABEL (1, 1) # calculate and show the converted km
label11 = Label(text="")
label11.grid(row=1, column=1)

# LABEL (1, 2) # "Km"
label12 = Label(text="Km")
label12.grid(row=1, column=2)

# BUTTON (2,1) # action=convert
button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

##
#Checkbutton
checked_state = IntVar()
checkbutton = Checkbutton(text="Round the result?", variable=checked_state, command=convert)
checked_state.get()
checkbutton.grid(row=2, column=2)

window.mainloop()
