import Tkinter as Tk
import Tix

root = Tix.Tk()

order_list = Tix.HList(root, columns = 5, header = True)
order_list.header_create(0, text = "File")
order_list.header_create(1, text = "Date")
order_list.header_create(2, text = "Size")
order_list.add_row("row0", text = "filename.txt")
order_list.item_create(entry_path, 1, text = "2009-03-26 21:07:03")
order_list.item_create(entry_path, 2, text = "200MiB")

app = Tk()
