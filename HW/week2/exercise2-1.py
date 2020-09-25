# 2
print (7 ** 2, "== 49")

# 4
print (3 + (4 * 5), "== 23" )

# 6
print (3 * ((-2) ** 5), "== -96")

# 8
print (14 % 4, "== 2")

# 10
print (14 // 4, "== 3")

# 12
print (5 % 5, "== 0")

# 14
print ("'room&Board' is not a valid variable name.")

# 16
print ("'1040B' is not a valid variable name.")

# 18
print ("'INCOME 2008' is not a valid variable name.")


a = 5
b = 3
c = 7
# 20
print (a * (b + c), "== 50")

# 22
print (a ** c, "== 78125")

# 24
print ((c - a) ** b, "== 8")

# 26
print ((3 ** 4) * (4 ** 3), "== 5184")

# 28
print (((2 ** 3) - 1) + 5, "== 12")

# 30
print ((1 / (2 ** 4)) * (2 ** 4), "== 1")

# 32
bal = 100
print ("bal:", bal, "inter: undefined", "withDr: undefined")
inter = .05
print ("bal:", bal, "inter:", inter, "withDr: undefined")
withDr = 25
print ("bal:", bal, "inter:", inter, "withDr:", withDr)
bal += (inter * bal)
print ("bal:", bal, "inter:", inter, "withDr:", withDr)
bal = bal - withDr
print ("bal:", bal, "inter:", inter, "withDr:", withDr)

# 34
d = 5
d -= 1
print (d, d + 1, d - 2)

# 36
points = 30
points += 20 * 10
print (points)

# 38
totalMeters = 30255
kiloMeters = totalMeters // 1000
meters = totalMeters % 1000
print (kiloMeters, meters)

# 40
print ("',' is a special symbol, which is not a part of int.")
print ("'$' is a special symbol, which is not a part of int.")

# 42
print ("Variable name must start with a letter or underscore character.")

# 44
print (int (9 - 2), "== 7")

# 46
print (abs (10 ** (-3)), "== -1000")

# 48
print (round (-2.6), "== -3")

a = 6
b = 4
# 50
print (abs (a - 5), "== 1")

# 52
print (abs (4 - a), "== -2")

# 54
print (int (b * 0.5), "== 2")

# 56
print ("sum *= 2")

# 58
print ("sum -= 7")

# 60
print ("cost //= 3")

# 62 (Stock Purchase)
costPerShare = 25.625
numberOfShares = 400
amount = costPerShare * costPerShare
print (amount)

# 64 (Break Even Point)
fixedCosts = 5000
pricePerUnit = 8
costPerUnit = 6
breakEvenPoint = fixedCosts / (pricePerUnit - costPerUnit)
print (breakEvenPoint)

# 66 (Savings Account)
balance = 100
balance = balance * 1.05 + 100
balance = balance * 1.05 + 100
balance = balance * 1.05
print (round(balance, 2))

# 68 (Profit from Stock)
purchasePrice = 10
sellingPrice = 15
percentProfit  = ((sellingPrice - purchasePrice) / purchasePrice) * 100
print (percentProfit)

# 70 (Projectile Motion)
initialSpeed = 50 # feets per second
initialHeight = 5 # feets
finalTime = 3 # seconds
finalHeight = -16 * (finalTime ** 2) + (initialSpeed * finalTime) + initialHeight
print (finalHeight)

# 72 (Gas Mileage)
firstFill = 23352
secondFill = 23695
filledGallons = 14
milesPerGallon = (secondFill - firstFill) / 14
print (milesPerGallon)

# 74 (Square Deck)
print (432 ** .5, "foot")

# 76 (Population Increase)
pastPopulation = 845
growth = 0.065
currentPopulation = pastPopulation * growth
print (currentPopulation)

# 78 (Calories)
calPerCubicFeet = 48600
calPerCubicMile = 48600 * 5280 * 5280
print (calPerCubicMile)

