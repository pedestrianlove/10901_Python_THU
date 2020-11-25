# 1091-Python-THU HW7

### 24
如果這個程式跑第二次會發生什麼？(假設執行目錄下原本沒有"ABC.txt"這個檔案)
``` python
import os.path
if os.path.isfile ("ABC.txt"):
	print ("File already exists.")
else:
	infile = open ("ABC.txt", 'w')
	infile.write ("a\nb\nc\n")
	infile.close ()
```

## 26、28 使用sets簡化下列函數，不用考慮list中的順序。
### 26
``` python
def findItemsInBoth (list1, list2):
	list3 = []
	for item in list1:
		if (item in list2) and (item not in list3):
			list3.append (item)
	return list3
```
[list to set](https://stackoverflow.com/questions/15768757/how-to-construct-a-set-out-of-list-items-in-python)
[set to list](https://www.geeksforgeeks.org/python-convert-set-into-a-list/)

### 28
``` python
names = ["Donald Shell", "Harlan Mills", "Donald Knuth", "Alan Kay"]
setLN = set ()	# empty set
for name in names:
	setLN.add (name.split ()[-1])
print (setLN)
```

## 34 ~ 42 不可使用list來完成指定的目標
### 34
print出`Numbers.txt`中數字的數量，如下：
```
The file Numbers.txt contains 6 numbers.
```

### 36
print出`Numbers.txt`中最小的數字，如下：
```
The smallest number in the file Numbers.txt is 2.
```

### 38
print出`Numbers.txt`中數字的平均值，如下：
```
The average of the numbers in the file Numbers.txt is 5.0.
```

### 40
檔案`SomeMonths.txt`包含了12個月份的名稱。寫出一個程式移除檔案中所有不含r字元的月份。

### 42
檔案`SomePlayers.txt`包含了30名美式足球選手的名字。寫一個程式移除檔案中所有不以母音開頭的名字。



### 44
`PresStates.txt`中包含了44行曾出過美國總統的洲名。前四行依序為：
```
Virginia
Massachusetts
Virginia
Virginia
...
```
寫一個程式來去除檔案中所有重複的洲名，並顯示出共有幾個洲産生過總統。如下：
```
18 different states have produced presidents of the United States.
```

### 46
`Names.txt`檔案包含了一些以字母順排序的first name。
寫一個程式來跟使用者索取名字，並把名字放入檔案中適當的位置。
如果檔案中已有該姓名，則不可放入。
