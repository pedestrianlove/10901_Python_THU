# Indicies
print ("Python")
print ("Python"[1], "Python"[5], "Python"[2:4])

# Find in str
str1 = "Hello World!"
print (str1.find ('W'))
print (str1.find ('x'))
print (str1.rfind ('l'))

# negative indicies
print ("Python")
print ("Python" [-1], "Python" [-4], "Python" [-5 : -2])

str1 = "spam & eggs"
print (str1 [-2])
print (str1 [-8:-3])
print (str1 [0:-4])

# print to/from the boundary
print ("Python" [2: ], "Python" [ :4], "Python"[ : ])
print ("Python" [-3: ], "Python" [ :-3])

str2 = "Python"
print ("Hello-"*2+str2)
