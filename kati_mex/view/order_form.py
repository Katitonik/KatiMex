from tkinter import Tk
# from tkinter import  *
from tkinter import ttk


app = Tk()
app.title("El Fuego Cucaracha")
app.geometry("500x400")

# this will be implemented by the button


def client_info():
    client_name = client.get()
    client_number = number.get()
    client_address = address.get()
    client_display = client_name + ", " + client_number + ", " + client_address
    displayed_info = ttk.Label(app)
    displayed_info["text"] = client_display, receiving_method.current()
    displayed_info.grid(column=5, row=5)


# restuarant name
label_top = ttk.Label(app, text="El Fuego Cucaracha")
label_top.grid(column=0, row=0)

# client name
label_client = ttk.Label(app, text="client")
label_client.grid(column=0, row=2)

# client number (phone)
label_number = ttk.Label(app, text="number")
label_number.grid(column=0, row=3)

# client address
label_address = ttk.Label(app, text="address")
label_address.grid(column=0, row=4)

# entry fields
client = ttk.Entry(app,)
number = ttk.Entry(app,)
address = ttk.Entry(app,)
add = ttk.Button(app, text="add", command=client_info)

# where the widgets will apear
client.grid(column=1, row=2)
number.grid(column=1, row=3)
address.grid(column=1, row=4)
add.grid(column=5, row=4)

# combobox programming section
receiving_method = ttk.Combobox(app, values=("pick up", "delivery"))
print(dict(receiving_method))
receiving_method.grid(column=5, row=2)
receiving_method.current(0)
print(receiving_method.current(), receiving_method.get())


# def chosen_item():
#    menu_order = menu_items.get()
#   side_order = side_items.get()
#    display_order = menu_order + ", " + side_order
#    display_order = ttk.Label(app)
#    display_order["text"] = display_order
#    display_order.grid(column=1, row=9)


# order information begins here
menu_items = ttk.Combobox(app, values=["Nachos",
                                       "Hard Shell Tacos",
                                       "Soft Shell Tacos",
                                       "Chimichangas",
                                       "Mole",
                                       "Enchiladas",
                                       "Aguachile",
                                       "Cochnita Pibli",
                                       "Sopa de Cameron",
                                       "Chilato de Polo",
                                       "Chiles Rellenos"])

print(dict(menu_items))
menu_items.grid(column=1, row=6)
menu_items.current(1)
print(menu_items.current(), menu_items.get(),)

# side menu items
side_items = ttk.Combobox(app, values=["Guacamole",
                                       "Salsa",
                                       "Salad",
                                       "Chips",
                                       "Soda"])

print(dict(side_items))
side_items.grid(column=1, row=7)
side_items.current(1)
print(side_items.current(), side_items.get(),)

# ordered_item = ttk.Button(app, text="add item", command=chosen_item)
# ordered_item.grid(column=2, row=7)


app.mainloop()
