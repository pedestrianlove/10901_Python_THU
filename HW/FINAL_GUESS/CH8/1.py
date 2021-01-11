import tkinter as tk
import tkinter.font


def invest ():
	rate_str = rate_list.get (tk.ANCHOR)
	rate = rate_list_val[rate_list_str.index (rate_str)] * 0.01
	times_str = periods_list.get (tk.ANCHOR)
	times = periods_list_val[periods_list_str.index (times_str)]
	val = 10000 * (1 + (rate / times)) ** (5 * times)
	output_text.set ("${:,.2f}".format (val))

# init window
width = 800
height = 600
window = tk.Tk ()
window.title ('Investment')
window.geometry ('{}x{}'.format (width, height))
window.columnconfigure ((0,1,2,3,4), weight=1)
window.rowconfigure ((0,1,2,3,4), weight=1)

# make text area
font = tk.font.Font (window, family="Source Code Pro", size=24)
text = tk.StringVar ()
label = tk.Label (window, font=font, height=1, textvariable=text, relief=tk.RAISED)
text.set ("Invest $10,000")
label.grid (column=1, row=0, ipadx=10, ipady=10)

# listboxes
## rate
rate_list_val = [2, 2.5, 3, 3.5, 4]
rate_list_str = []
for i in range (len (rate_list_val)):
	if isinstance (rate_list_val[i], int):
		rate_list_str.append ("{:d}%".format (rate_list_val[i]))
	else:
		rate_list_str.append ("{:.1f}%".format (rate_list_val[i]))
rate_list = tk.Listbox (window, exportselection=False, selectmode=tk.SINGLE, font=font)
for i in range (len (rate_list_str)):
	rate_list.insert (i, rate_list_str[i])
rate_list.grid (column=1, row=1)



## compound periods
font["size"] = 14
periods_list_str = ["annually", "semi-annually", "quarterly", "monthly", "weekly"]
periods_list_val = [1, 2, 4, 12, 52]
periods_list = tk.Listbox (window, exportselection=False, selectmode=tk.SINGLE, font=font)
for i in range (len (periods_list_str)):
	periods_list.insert (i, periods_list_str[i])
periods_list.grid (column=2, row=1)


# compute button
font["size"] = 12
btnText = "Calculate\nAmount\nAfter 5\nYears"
computeBtn = tk.Button (window, font=font, text=btnText, command=invest)
computeBtn.grid (column=3, row=1)





# read only text and its description
font["size"] = 12
desc = tk.Label (window, font = font, text="Amount after 5 years: ")
desc.grid (row=2, column=1)
font["size"] = 18
output_text = tk.StringVar ()
output = tk.Entry (window, font=font, textvariable=output_text, state=tk.DISABLED)
output.grid (row=2, column=2, padx=10, pady=10)



# start window
window.mainloop ()
