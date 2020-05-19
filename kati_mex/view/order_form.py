import tkinter.ttk as ttk
import tkinter as tk
from tkinter import ttk
from tkinter import Tk
<< << << < HEAD
# from tkinter import  *


app = Tk()
app.title("El Fuego Cucaracha")
app.geometry("500x400")
== == == =


def new_order():
    pass


>>>>>> > d7e874298d1c0330a5e2695a3eb8894236aaf463

# this will be implemented by the button

<< << << < HEAD


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
== == == =


def clear_order():
    pass


def clear_order_header():
    pass


def clear_order_items():
    pass


def clear_order_footer():
    pass


def _get_order_header():
    pass


def _get_order_items():
    pass


def _get_order_footer():
    pass


def save_order():
    pass


form = tk.Tk()

# header
lbl_header = tk.Label(master=form, text='Customer Details')
frm_header = tk.Frame(master=form, relief=tk.RAISED, borderwidth=1)

var_cust = tk.StringVar()
lbl_cust = tk.Label(master=frm_header, text='Customer:')
ent_cust = tk.Entry(master=frm_header, textvariable=var_cust)

var_contact = tk.StringVar()
lbl_contact = tk.Label(master=frm_header, text='Contact:')
ent_contact = tk.Entry(master=frm_header, textvariable=var_contact)

var_deliver = tk.BooleanVar()
rbtn_collect = tk.Radiobutton(master=frm_header, text='Collect',
                              variable=var_deliver, value=False)
rbtn_deliver = tk.Radiobutton(master=frm_header, text='Deliver',
                              variable=var_deliver, value=True)

var_street = tk.StringVar()
lbl_street = tk.Label(master=frm_header, text='Street:')
ent_street = tk.Entry(master=frm_header, textvariable=var_street)

var_suburb = tk.StringVar()
lbl_suburb = tk.Label(master=frm_header, text='Suburb:')
cbx_suburb = ttk.Combobox(master=frm_header, textvariable=var_suburb)

lbl_header.grid(row=0, column=0)
frm_header.grid(row=1, column=0)
lbl_cust.grid(row=1, column=0)
ent_cust.grid(row=1, column=1)
lbl_contact.grid(row=1, column=2)
ent_contact.grid(row=1, column=3)
rbtn_collect.grid(row=1, column=4)
rbtn_deliver.grid(row=1, column=5)
lbl_street.grid(row=3, column=0)
ent_street.grid(row=3, column=1)
lbl_suburb.grid(row=3, column=2)
cbx_suburb.grid(row=3, column=3)

# items
lbl_items = tk.Label(master=form, text='Items')
frm_items = tk.Frame(master=form, relief=tk.GROOVE)

lbl_items.grid(row=5, column=0)
frm_items.grid(row=6, column=0)

var_item = tk.StringVar()
lbl_item = tk.Label(master=frm_items, text='Item')
ent_item = ttk.Combobox(master=frm_items, textvar=var_item)

var_spic = tk.StringVar()
lbl_spic = tk.Label(master=frm_items, text='Spicyness:')
cbx_spic = ttk.Combobox(master=frm_items, textvariable=var_spic)

var_qty = tk.IntVar()
lbl_qty = tk.Label(master=frm_items, text='Quantity:')
ent_qty = tk.Entry(master=frm_items, textvariable=var_qty)

btn_add = tk.Button(master=frm_items, text='+')
btn_remove = tk.Button(master=frm_items, text='-')

lst_items = tk.Listbox(master=frm_items, width=96, selectmode=tk.SINGLE)

lbl_item.grid(row=7, column=0)
ent_item.grid(row=7, column=1)
lbl_spic.grid(row=7, column=2)
cbx_spic.grid(row=7, column=3)
lbl_qty.grid(row=7, column=4)
ent_qty.grid(row=7, column=5)
btn_add.grid(row=7, column=6)
btn_remove.grid(row=8, column=6, sticky=tk.N)
lst_items.grid(row=8, columnspan=6)

for i in "1,2,3,4".split(','):
    lst_items.insert(tk.END, i)

# footer
lbl_footer = tk.Label(master=form, text='Summary')
frm_footer = tk.Frame(master=form, relief=tk.GROOVE)
lbl_sub = tk.Label(master=frm_footer, text='Sub Total:')
lbl_tax = tk.Label(master=frm_footer, text='Tax:')
lbl_del = tk.Label(master=frm_footer, text='Delivery Charge:')
lbl_ttl = tk.Label(master=frm_footer, text='Total:')

lbl_footer.grid(row=9, column=0)
frm_footer.grid(row=10, column=0)
lbl_sub.grid(row=11, column=6, sticky=tk.E)
lbl_tax.grid(row=12, column=6, sticky=tk.E)
lbl_del.grid(row=13, column=6, sticky=tk.E)
lbl_ttl.grid(row=14, column=6, sticky=tk.E)

# buttons
btn_ok = tk.Button(master=form, width=10, text='Ok')
btn_cancel = tk.Button(master=form, width=10, text='Cancel')
btn_ok.grid(row=15, column=2)
btn_cancel.grid(row=15, column=3)


form.mainloop()

# order_window
#   lbl_header
#   frm_header
#     lbl_cust| ent_cust| lbl_contact| ent_contact
#     lbl_collect| rbtn_collect
#     lbl_street| ent_street| lbl_suburb| dd_suburb
#   lbl_items
#   frm_items
#     lbl_item| dd_item| lbl_spic| dd_spic| lbl_qty| ent_qty
#     btn_ok| btn_cancel
#     order table
#   lbl_summary
#   frm_summary
#     lbl_sub| lbl_subn
#     lbl_tax| lbl_taxn
#     lbl_del| lbl_deln
#     lbl_ttl| lbl_ttln
#   frm_btn
#     bnt_ok| btn_cancel
>>>>>> > d7e874298d1c0330a5e2695a3eb8894236aaf463
