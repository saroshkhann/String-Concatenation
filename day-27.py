# from tkinter import *
#
# window = Tk()
# window.title("My first GUI Program")
# window.minsize(width=500, height= 300)
#
#
# my_label = Label(text= "I Am a label", font= ("Arial", 24))
# my_label.pack()
#
# my_label["text"] = "Label"
#
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text = new_text)
#
#
# # my_label.config(command = button_clicked)
#
#
#
# button = Button(text = "Click Me", command = button_clicked)
# button.pack()
#
# input = Entry(width = 10)
# input.pack()
# print(input.get())
#
#
# window.mainloop()

from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx = 20, pady = 20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text= "is squal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command = miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()