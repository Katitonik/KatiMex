import tkinter as tk
import tkinter.ttk as ttk


def new_order():
    pass


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
