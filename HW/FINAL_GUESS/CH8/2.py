import tkinter as tk
import tkinter.font
import pickle

def getDict ():
	infile = open ("UNDict.dat", 'rb')
	nation = pickle.load (infile)
	infile.close ()
	return nation

def choose (event):
	selection = nation_list.get (tk.ANCHOR)
	cont_text.set (nations[selection]["cont"])
	popl_text.set ("{:,.0f}".format (nations[selection]["popl"] * 1000000))
	area_text.set ("{:,.2f}".format (nations[selection]["area"]))


# init dataset
nations = getDict ()

# init window
width = 800
height = 600
window = tk.Tk ()
window.title ('Members of U.N.')
#window.geometry ('{}x{}'.format (width, height))
#window.columnconfigure ((0,1,2,3,4), weight=1)
#window.rowconfigure ((0,1,2,3,4), weight=1)

# scrollable listbox
## nations listbox
font = tk.font.Font (window, family="Source Code Pro", size=24)
nation_list = tk.Listbox (window, selectmode=tk.SINGLE, font=font)
nation_list.bind ("<<ListboxSelect>>", choose)
i = 0
for nation in nations:
	nation_list.insert (i, nation)
	i += 1
nation_list.grid (column = 0, row = 0)

## scrollbar
scrollbar = tk.Scrollbar (window)
nation_list.config (yscrollcommand = scrollbar.set)
scrollbar.config (command = nation_list.yview)
scrollbar.grid (column = 1, row = 0)

def make_output (window, font, text_str, rowsy):
	font["size"] = 12
	desc = tk.Label (window, font = font, text=text_str)
	desc.grid (row=rowsy, column=2)

	font["size"] = 18
	output_text = tk.StringVar ()
	output_output = tk.Entry (window, font=font, textvariable=output_text, state=tk.DISABLED)
	output_output.grid (row=rowsy, column=3, padx=10, pady=10)
	return output_text



# read-only text and its descriptions
## Continent
cont_text = make_output (window, font, "Continent: ", 0)

## Populations
popl_text = make_output (window, font, "Population: ", 1)

## Area
area_text = make_output (window, font, "Area (sq. miles): ", 2)


# start window
window.mainloop ()
