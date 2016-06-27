from tkinter import *
from tkinter import ttk
import hmac
import hashlib
import time

#CONSTANTS
ENTRY_WIDTH = 30

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.title("HASH CALCULATOR: ULTRA EDITION")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

transaction_key = StringVar()
x_login = StringVar()
x_fp_timestamp = StringVar()
x_fp_sequence = StringVar()
x_amount = StringVar()
x_currency = StringVar()
x_fp_hash = StringVar()

#set timestamp
def calculate_timestamp(*args):
	time_now = str(int(time.time()))
	x_fp_timestamp.set(time_now)

#calculates hash with hmac-md5 algorithm.
def calculate_hash(*args):
	try:
		transaction_key_value = transaction_key.get().encode()
		hmac_md5_digest = hmac.new(transaction_key_value, b'', hashlib.md5)
		format = "%(x_login)s^%(x_fp_sequence)s^%(x_fp_timestamp)s^%(x_amount)s^%(x_currency)s"
		x_login_value = x_login.get()
		print("x_login: ", x_login_value)
		x_fp_timestamp_value = x_fp_timestamp.get()
		print("timestamp: ", x_fp_timestamp_value)
		x_fp_sequence_value = x_fp_sequence.get()
		print("x_fp_sequence: ", x_fp_sequence_value)
		x_amount_value = x_amount.get()
		print("x_amount: ", x_amount_value)
		x_currency_value = x_currency.get()
		print("x_currency ", x_currency_value)
		data = format % {'x_login' : x_login_value,'x_fp_sequence' : x_fp_sequence_value,'x_fp_timestamp' : x_fp_timestamp_value,'x_amount' : x_amount_value,'x_currency' : x_currency_value}
		data = data.encode()
		hmac_md5_digest.update(data)
		x_fp_hash.set(hmac_md5_digest.hexdigest())
		print("x_fp_hash: ", x_fp_hash.get())
	except ValueError:
		pass

#FIELD ENTRY AND TIMESTAMP/HASH VALUE OUTPUT ENTRIES
transaction_key_entry = ttk.Entry(mainframe, width=ENTRY_WIDTH, textvariable=transaction_key)
transaction_key_entry.grid(column=2, row=1, sticky=(W, E))

x_login_entry = ttk.Entry(mainframe, width=ENTRY_WIDTH, textvariable=x_login)
x_login_entry.grid(column=2, row=2, sticky=(W, E))

x_fp_timestamp_entry = ttk.Entry(mainframe, width=ENTRY_WIDTH, textvariable=x_fp_timestamp)
x_fp_timestamp_entry.grid(column=2, row=3, sticky=(W, E))

x_fp_sequence_entry = ttk.Entry(mainframe, width=ENTRY_WIDTH, textvariable=x_fp_sequence)
x_fp_sequence_entry.grid(column=2, row=4, sticky=(W, E))

x_amount_entry = ttk.Entry(mainframe, width=ENTRY_WIDTH, textvariable=x_amount)
x_amount_entry.grid(column=2, row=5, sticky=(W, E))

x_currency_entry = ttk.Entry(mainframe, width=ENTRY_WIDTH, textvariable=x_currency)
x_currency_entry.grid(column=2, row=6, sticky=(W, E))

x_fp_hash_entry = ttk.Entry(mainframe, width=ENTRY_WIDTH, textvariable=x_fp_hash)
x_fp_hash_entry.grid(column=2, row=7, sticky=(W, E))

#LABELS
ttk.Label(mainframe, text="transaction key").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="x_login").grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="Calculate Timestamp", command=calculate_timestamp).grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="x_fp_sequence").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="x_amount").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="x_currency").grid(column=1, row=6, sticky=W)
ttk.Button(mainframe, text="Calculate Hash Value", command=calculate_hash).grid(column=1, row=7, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

x_login_entry.focus()
root.bind('<Return>', calculate_hash)

root.mainloop()
