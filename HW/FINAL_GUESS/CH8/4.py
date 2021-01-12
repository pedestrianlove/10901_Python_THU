import tkinter as tk
import tkinter.font

def verbalizeNumber (number):
	num_single_list = number.strip ().split (',')
	num_single_list.reverse ()
	num_list = [[" "], ["thousand"], ["million"], ["billion"], ["trillion"], ["quadrillion"], ["quintillion"], ["sextillion"], ["septillion"]]
	for i in range (len (num_list)):
		if i < len (num_single_list) and num_single_list[i] != '000':
			print ("Appending", num_single_list[i], end='')
			num_list[i].append (eval (num_single_list[i].lstrip ('0')))
			print ("...Done.")
		else:
			num_list[i].append (0)
	num_list.reverse ()
	output = ""
	for num_pos in num_list:
		output = output + "{:3d} ".format (num_pos[1]) + num_pos[0] + "\n"
	return output

def click ():
	print ("Clicked")
	number = entry.get ()
	output_area.delete (1.0, tk.END)
	output_area.insert (tk.END, verbalizeNumber (number))


# init window
width = 800
height = 600
window = tk.Tk ()
window.title ('Verbalize')
#window.geometry ('{}x{}'.format (width, height))
#window.columnconfigure ((0,1,2,3,4), weight=1)
#window.rowconfigure ((0,1,2,3,4), weight=1)

# make text area
font = tk.font.Font (window, family="Source Code Pro", size=24)
text = tk.StringVar ()
label = tk.Label (window, font=font, height=1, width=35, textvariable=text, relief=tk.FLAT)
text.set ("Enter a number having at most\n27 digits (include commas).")
label.grid (column=1, row=0, ipadx=10, ipady=10, sticky=tk.N)

# make entry area
entry = tk.Entry (window, font=font, width=35, state=tk.NORMAL)
entry.grid (column=1, row=1, stick = tk.N)


# make button
btnText = "Verbalize\nNumber"
btn = tk.Button (window, font=font, text=btnText, command=click)
btn.grid (column=1, row=2, stick = tk.N + tk.W)


# make output text area
output_area = tk.Text (window, font=font, width=15, height=9, state=tk.NORMAL)
output_area.grid (column=1, row=2, stick = tk.N + tk.E)

# start window
window.mainloop ()
