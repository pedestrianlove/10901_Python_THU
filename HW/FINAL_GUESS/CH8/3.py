import tkinter as tk
import tkinter.font
def pension (highest, years, months, age):
	if age>= 55 and (years + months / 12) >= 20:
		ave = sum (highest) / 3
		yrs = years + (months / 12)
		if yrs <= 5:
			perRate = 0.015 *  yrs
		elif yrs <= 10:
			perRate = 0.075 + 0.0175 * (yrs - 5)
		else:
			perRate = 0.075 + 0.0875 + 0.02 * (yrs - 10)
		p = min (perRate, 0.8)
		return p * ave
	else:
		return 0


def click ():
	print ("Clicked")
	age = eval (age_entry.get ())
	years = eval (years_entry.get ())
	months = eval (months_entry.get ())
	highest = []
	for salary in salaries_entries:
		highest.append (eval (salary.get ()))
	# output to the read-only entry
	output_text.set ("${:,.2f}".format (pension (highest, years, months, age)))



# init window
width, height = 800, 600
window = tk.Tk ()
window.title ('Pension')
#window.geometry ('{}x{}'.format (width, height))
#window.columnconfigure ((0,1,2,3,4), weight=1)
#window.rowconfigure ((0,1,2,3,4), weight=1)

# make label - three salaries
font = tk.font.Font (window, family="Source Code Pro", size=24)
salaries_text = tk.StringVar ()
salaries_label = tk.Label (window, font=font, textvariable=salaries_text, relief=tk.FLAT)
salaries_text.set ("Three\nHighest\nAnnual\nSalaries")
salaries_label.grid (column=1, row=0, ipadx=10, ipady=10, sticky=tk.N + tk.W)


## function to be used
def make_entries (window, font, rowies, colies):
	entry = tk.Entry (window, font=font, width=10, state=tk.NORMAL)
	entry.grid (column=colies, row=rowies, stick = tk.N + tk.W)
	return entry
# make entry - three salaries
salaries_entries = []
for i in range (3):
	salaries_entries.append (make_entries (window, font, i, 2))

# make label - age
age_text = tk.StringVar ()
age_text.set ("     Age: ")
age_label = tk.Label (window, font=font, height=1, textvariable=age_text)
age_label.grid (column=1, row=3, sticky=tk.N + tk.W)

# make entry - age
age_entry = make_entries (window, font, 3, 2)

# make label - Service
Service_text = tk.StringVar ()
Service_text.set ("Service")
Service_label = tk.Label (window, font=font, height=1, textvariable=Service_text)
Service_label.grid (column=3, row=0, sticky=tk.N + tk.W)


# make label - Years
years_text = tk.StringVar ()
years_text.set ("Years: ")
years_label = tk.Label (window, font=font, height=1, textvariable=years_text)
years_label.grid (column=3, row=1, sticky=tk.N + tk.W)

# make entry - Years
years_entry = make_entries (window, font, 1, 4)

# make label - Months
months_text = tk.StringVar ()
months_text.set ("Months: ")
months_label = tk.Label (window, font=font, height=1, textvariable=months_text)
months_label.grid (column=3, row=2, sticky=tk.N + tk.W)

# make entry - Months
months_entry = make_entries (window, font, 2, 4)


# make button - Calculate Pension
btnText = "Calculate Pension"
btn = tk.Button (window, font=font, text=btnText, command=click)
btn.grid (column=3, row=4, stick = tk.N + tk.W)

# make label - output text area
output_label_text = tk.StringVar ()
output_label_text.set ("Pension: ")
output_label = tk.Label (window, font=font, height=1, textvariable=output_label_text)
output_label.grid (column=1, row=5, sticky=tk.S + tk.E)

# make entry (read-only) -  output text area
output_text = tk.StringVar ()
output_area = tk.Entry (window, font=font, width=15, textvariable = output_text, state=tk.DISABLED)
output_area.grid (column=2, row=5, stick = tk.S + tk.E)

# start window
window.mainloop ()
