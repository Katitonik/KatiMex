import model
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

# form
form = tk.Tk()
form.title("El Fuego Cucoracha")

# header variables
header_client = tk.StringVar()
header_contact = tk.StringVar()
header_deliver = tk.BooleanVar()
header_street = tk.StringVar()
header_suburb = tk.StringVar()

# item variables
items = []
items_item = tk.StringVar()
items_spicyness = tk.StringVar()
items_size = tk.StringVar()
items_quantity = tk.IntVar()

# footer constants
footer_sub_label = 'Sub Total:  '
footer_tax_label = 'Tax:  '
footer_delivery_label = 'Delivery Charge:  '
footer_total_label = 'Total:  '


# item events
def add_item():
    dish = model.new_dish(ent_item.get(), model.Spicyness[cbx_spic.get()])
    qty = int(ent_qty.get())
    size = model.Size[ent_size.get()]
    item = model.new_order_item(dish, qty, size)
    items.append(item)
    display_item = f"{item.item.name: <30} " \
        f"{item.item.spicyness.name: <8} " \
        f"{item.size.name: <8} " \
        f"{item.quantity: <3} @ {item.unit_price:6.2f} " \
        f"{item.item_price:20.2f}"
    lst_items.insert(tk.END, display_item)

# f"{}" formats all the values in the {braces} to strings
# simplifying the generation of strings


def remove_item():
    selected_item = lst_items.index(tk.ACTIVE)
    if len(items):
        del(items[selected_item])
    lst_items.delete(selected_item)


# order events
def checkout_order():
    header = model.new_order_header(
        deliver=header_deliver.get(),
        client_name=header_client.get(),
        client_street=header_street.get(),
        client_contact=header_contact.get(),
        client_suburb=header_suburb.get())
    order = model.new_order(header, items)
    lbl_sub['text'] = ''
    lbl_sub['text'] = footer_sub_label + f"{order.footer.subtotal:.2f}"
    lbl_tax['text'] = ''
    lbl_tax['text'] = footer_tax_label + f"{order.footer.tax:.2f}"
    lbl_del['text'] = ''
    lbl_del['text'] = footer_delivery_label + \
        f"{order.footer.delivery_charge:.2f}"
    lbl_ttl['text'] = ''
    lbl_ttl['text'] = footer_total_label + f"{order.footer.total:.2f}"

    print(order)


def cancel_order():
    ent_cust.delete(0, tk.END)
    ent_contact.delete(0, tk.END)
    ent_street.delete(0, tk.END)
    ent_contact.delete(0, tk.END)
    ent_qty.delete(0, tk.END)
    lst_items.delete(0, tk.END)
    lbl_sub['text'] = footer_sub_label
    lbl_tax['text'] = footer_tax_label
    lbl_del['text'] = footer_delivery_label
    lbl_ttl['text'] = footer_total_label


def exit_order():
    import sys
    sys.exit()


# header
lbl_header = tk.Label(master=form, text='Customer Details')
frm_header = tk.Frame(master=form, relief=tk.RAISED, borderwidth=1)

lbl_cust = tk.Label(master=frm_header, text='Customer:')
ent_cust = tk.Entry(master=frm_header, textvariable=header_client)

lbl_contact = tk.Label(master=frm_header, text='Contact:')
ent_contact = tk.Entry(master=frm_header, textvariable=header_contact)

rbtn_collect = tk.Radiobutton(master=frm_header, text='Collect',
                              variable=header_deliver, value=False)
rbtn_deliver = tk.Radiobutton(master=frm_header, text='Deliver',
                              variable=header_deliver, value=True)

lbl_street = tk.Label(master=frm_header, text='Street:')
ent_street = tk.Entry(master=frm_header, textvariable=header_street)

lbl_suburb = tk.Label(master=frm_header, text='Suburb:')
cbx_suburb = ttk.Combobox(
    master=frm_header,
    textvariable=header_suburb,
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
    textvar=items_item,
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
    textvariable=items_spicyness,
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
    textvariable=items_size,
    values=[
        "Small",
        "Medium",
        "Large"
    ])
ent_size.current(0)

lbl_qty = tk.Label(master=frm_items, text='Quantity:')
#ent_qty = tk.Entry(master=frm_items, textvariable=items_quantity)
ent_qty = ttk.Combobox(master=frm_items, textvariable=items_quantity,
                       values=['1', '2', '3', '4', '5'], state='readonly')

btn_add = tk.Button(master=frm_items, command=add_item, text='+')
btn_remove = tk.Button(master=frm_items, command=remove_item, text='-')

fnt_items = Font(family='Consolas', size=12)
lst_items = tk.Listbox(master=frm_items, width=96, font=fnt_items,
                       selectmode=tk.SINGLE)

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
lbl_sub = tk.Label(master=frm_footer, text=footer_sub_label)
lbl_tax = tk.Label(master=frm_footer, text=footer_tax_label)
lbl_del = tk.Label(master=frm_footer, text=footer_delivery_label)
lbl_ttl = tk.Label(master=frm_footer, text=footer_total_label)

lbl_footer.grid(row=8, column=0, sticky=tk.W)
frm_footer.grid(row=9, column=1)
lbl_sub.grid(row=10, column=6, sticky=tk.E)
lbl_tax.grid(row=11, column=6, sticky=tk.E)
lbl_del.grid(row=12, column=6, sticky=tk.E)
lbl_ttl.grid(row=13, column=6, sticky=tk.E)

# buttons
btn_checkout = tk.Button(master=form, command=checkout_order, width=10,
                         text='Checkout')
btn_cancel = tk.Button(master=form, command=cancel_order, width=10,
                       text='Cancel')
btn_exit = tk.Button(master=form, command=exit_order, width=10, text='Exit')

btn_checkout.grid(row=12, column=2)
btn_cancel.grid(row=13, column=2)
btn_exit.grid(row=14, column=2)


form.mainloop()
