fullName = input ( "enter your fullname(first last):" )

n = fullName.rfind ( " " )
print ( "Last name: ", fullName[ n+1 :  ] )
print ( "First name(s): ", fullName[  : n ] )

