import model as model
import tkinter as tk
import tkinter.ttk as ttk


# form
form = tk.Tk()

# header variables
var_cust = tk.StringVar()
var_contact = tk.StringVar()
var_deliver = tk.BooleanVar()
var_street = tk.StringVar()
var_suburb = tk.StringVar()

# item variables
var_items = []
var_item = tk.StringVar()
var_spic = tk.StringVar()
var_size = tk.StringVar()
var_qty = tk.IntVar()


# item events
def add_item():
    dish = model.new_dish(ent_item.get(), model.Spicyness[cbx_spic.get()])
    qty = int(ent_qty.get())
    size = model.Size[ent_size.get()]
    item = model.new_order_item(dish, qty, size)
    var_items.append(item)
    display_item = f"{item.item.name} " \
        f"{item.item.spicyness.name} " \
        f"{item.size.name} " \
        f"{item.quantity} " \
        f"{item.item_price:.2f}"
    lst_items.insert(tk.END, display_item)

# f"{}" formats all the values in the {braces} to strings
# simplifying the generation of strings


def remove_item():
    selected_item = lst_items.index(tk.ACTIVE)
    if len(var_items):
        del(var_items[selected_item])
    lst_items.delete(selected_item)

# order events


def cancel_order():
    pass


def ok_order():
    pass


def exit_order():
    import sys
    sys.exit()


# header
lbl_header = tk.Label(master=form, text='Customer Details')
frm_header = tk.Frame(master=form, relief=tk.RAISED, borderwidth=1)

lbl_cust = tk.Label(master=frm_header, text='Customer:')
ent_cust = tk.Entry(master=frm_header, textvariable=var_cust)

lbl_contact = tk.Label(master=frm_header, text='Contact:')
ent_contact = tk.Entry(master=frm_header, textvariable=var_contact)

rbtn_collect = tk.Radiobutton(master=frm_header, text='Collect',
                              variable=var_deliver, value=False)
rbtn_deliver = tk.Radiobutton(master=frm_header, text='Deliver',
                              variable=var_deliver, value=True)

lbl_street = tk.Label(master=frm_header, text='Street:')
ent_street = tk.Entry(master=frm_header, textvariable=var_street)

lbl_suburb = tk.Label(master=frm_header, text='Suburb:')
cbx_suburb = ttk.Combobox(
    master=frm_header,
    textvariable=var_suburb,
    values=[
        "Browns Bay",
        "Torbay",
        "Long Bay"
    ])
cbx_suburb.current(0)

lbl_header.grid(row=0, column=0, sticky=tk.W)
frm_header.grid(row=1, column=1)
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
frm_items = tk.Frame(master=form, relief=tk.RAISED)

lbl_items.grid(row=5, column=0)
frm_items.grid(row=6, column=0)

lbl_item = tk.Label(master=frm_items, text='Item')
ent_item = ttk.Combobox(
    master=frm_items,
    textvar=var_item,
    values=[
        "Nachos",
        "Hard Shell Tacos",
        "Soft Shell Tacos",
        "Chimichangas",
        "Chiles Rellenos",
        "Chilato de Pollo",
        "Sopa de Cameron",
        "Cochnita pibli",
        "Mole",
        "Aquachile",
        "Enchiladas"
    ])
ent_item.current(0)

lbl_spic = tk.Label(master=frm_items, text='Spicyness:')
cbx_spic = ttk.Combobox(
    master=frm_items,
    textvariable=var_spic,
    values=[
        "Mild",
        "Hot",
        "Flaming",
        "Hell"
    ])
cbx_spic.current(0)

lbl_size = tk.Label(master=frm_items, text='Size: ')
ent_size = ttk.Combobox(
    master=frm_items,
    textvariable=var_size,
    values=[
        "Small",
        "Medium",
        "Large"
    ])
ent_size.current(0)

lbl_qty = tk.Label(master=frm_items, text='Quantity:')
ent_qty = tk.Entry(master=frm_items, textvariable=var_qty)

btn_add = tk.Button(master=frm_items, command=add_item, text='+')
btn_remove = tk.Button(master=frm_items, command=remove_item, text='-')

lst_items = tk.Listbox(master=frm_items, width=96, selectmode=tk.SINGLE)

lbl_items.grid(row=4, column=0, sticky=tk.W)
frm_items.grid(row=5, column=1)
lbl_item.grid(row=6, column=0)
ent_item.grid(row=6, column=1)
lbl_spic.grid(row=6, column=2)
cbx_spic.grid(row=6, column=3)
lbl_size.grid(row=6, column=4)
ent_size.grid(row=6, column=5)
lbl_qty.grid(row=6, column=6)
ent_qty.grid(row=6, column=7)
btn_add.grid(row=6, column=8)
btn_remove.grid(row=7, column=6, sticky=tk.N)
lst_items.grid(row=7, columnspan=6)


# footer
lbl_footer = tk.Label(master=form, text='Summary')
frm_footer = tk.Frame(master=form, relief=tk.GROOVE)
lbl_sub = tk.Label(master=frm_footer, text='Sub Total:')
lbl_tax = tk.Label(master=frm_footer, text='Tax:')
lbl_del = tk.Label(master=frm_footer, text='Delivery Charge:')
lbl_ttl = tk.Label(master=frm_footer, text='Total:')

lbl_footer.grid(row=8, column=0, sticky=tk.W)
frm_footer.grid(row=9, column=1)
lbl_sub.grid(row=10, column=6, sticky=tk.E)
lbl_tax.grid(row=11, column=6, sticky=tk.E)
lbl_del.grid(row=12, column=6, sticky=tk.E)
lbl_ttl.grid(row=13, column=6, sticky=tk.E)

# buttons
btn_ok = tk.Button(master=form, command=ok_order, width=10, text='Ok')
btn_cancel = tk.Button(master=form, command=cancel_order,
                       width=10, text='Cancel')
btn_exit = tk.Button(master=form, command=exit_order, width=10, text='Exit')

btn_ok.grid(row=12, column=2)
btn_cancel.grid(row=13, column=2)
btn_exit.grid(row=14, column=2)


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
