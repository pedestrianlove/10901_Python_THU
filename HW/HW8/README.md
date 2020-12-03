# 10901-Python-HW8

## 5.2



### 目前8、10題意不明，可能是根據某個檔案來做數據的分析，但沒看到那個檔案。

#### 8

#### 10



### 12、14請利用`Justices.txt`的檔案來作答。
每一筆資料的格式依序為: first name, last name, 指名的總統, 他們被指定的洲, 指定的年份, 離職的年份。
(以現仼的法官而言，離職的年份會被設為0)

#### 12
寫一個程式來秀出所有現仼的法官的名單。(以他們上仼的年份做排序)
如下所示：
```
Current Justices:
Antonin Scalia
Anthony Kennedy
Clarence Thomas
Ruth Ginsburg
Stephen Breyer
John Roberts
Samuel Alito
Sonia Sotomayor
Elena Kagen
```

#### 14
寫一個程式來索取洲的簡寫，並秀出所有於該洲被指定的法官。
（以服務年份來遞減排序，並假設今年為2015年）
輸出也應包含指名其的總統的last name。
如下所示：
```
Enter a state abbreviation: NH
Justice		Appointing Pres		Yrs Served
David Souter	Bush			19
Levi Woodbury	Polk			6
```


#### 16
`Pioneers.txt`這個檔案包含了一些電腦創新者的名字以及他們的成就。
檔案的前三行為：
```
Charles Babbage,is called the father of the computer.
Augusta Ada Byron,was the first computer programmer.
Alan Turing,was a prominent computer science theorist.
```
寫一個程式來秀出他們的名字，並索取一個名字當輸入，再輸出該人物的事蹟。
如下所示：
```
Charles Babbage    Augusta Ada Byron    Alan Turing	    John V. Atanasoff
Grace M. Hopper    John Machley	        J. Presper Eckert	
...
Marc Andreessen    James Gosling        Linus Torvalds      Guido van Rossum

Enter the name of a computer pioneer: Augusta Ada Byron.
Augusta Ada Byron was the first computer programmer.

```



### 18題使用`Colleges.txt`這個檔案。
`Colleges.txt`內每筆資料的格式依序為：名字、州、成立年份。
該檔案的前四行為：
```
Harvard University,MA,1636
William and Mary College,VA,1693
Yale University,CT,1701
University of Pennsylvania,PA,1740
```
#### 18
寫一個程式來索取洲的簡寫，並輸出該洲在1800年前最後成立的大學。
如下所示：
```
Enter a state abbreviation: PA
Last college in PA founded before 1800:
Univeristy of Pittsburgh
```

### 20題使用`StatesANC.txt`這個檔案。
`StatesANC.txt`內每筆資料的格式依序為：洲名、洲名簡寫、外號、洲首府。

#### 20
寫一個程式來索取洲名，並顯示它的簡寫、外號以及洲首府。
如下所示：
```
Enter the name of a state: Ohio
Abbreviation: OH
Nickname: Buckeye State
Capital: Columbus
```

### 22題使用`Oscars.txt`這個檔案。
`Oscars.txt`內每筆資料的格式依序為：得獎作品名、得獎作品種類。

#### 22
寫一個程式來索取年份，並秀出該年份的最佳得獎作品名及其種類。
如下所示：
```
Enter year from 1928-2013: 2012
Best Film: Argo
Genre: drama
```


### 24、26參見下方表格。
Item		|	Price ($)|
:---------------|---------------:|
Colt Peacemaker |	12.20    |
Holster		|	2.00	 |
Levi Strauss jeans |	1.35	 |
Saddle		|	40.00	 |
Stetson		|	10.00	 |

生成一個包含上述表格資訊的檔案`Cowboy.txt`，並用於24、26的作答。

#### 24
假設saddle打了八折。使用`Cowboy.txt`建立一個新檔案：`Cowboy2.txt`來放入新的價位表。

#### 26
寫一個程式來在`Cowboy.txt`的最後一行加上`Winchester Rifle,20.50`。



## 5.3
#### 50
(這應該是個題組的最後一題，所以如果有人有前面的題目請再拍給我)
寫一個程式來找出三人中的最高累計打擊數。該程式要用max來實作。
如下所示：
```
The most hits by one of the baseball players was 2873.
```

### 52、54題會用到`JusticesDict.dat`
該檔案格式為：
```
法官名:{'pres':"總統名", 'yrLeft':"離職年份", 'yrAppt':"上崗年份", 'state':"指定的洲"}
```
注意dictionary沒有順序!

#### 52
寫一個程式來索取洲名簡寫並秀出該洲所有法官的名字、上崗年份。
如下所示：
```
Enter a state abbreviation: NH
David Souter		1990
Levi Woodbury		1845
```

#### 54
寫一個程式來秀出所有產生過法官的洲、及其數量。輸出應以字母排序。
如下所示：
```
31 states have produced justices.
    AL: 3
    AZ: 2
    CA: 5
    CO: 1
    CT: 3
    ...
```

#### 56
`Rosebowl.txt`這個檔案包含了直至2014所有Rose Bowl的winner(以年份排序)。
寫一個程式秀出所有win了四場以上的隊伍。隊伍應以勝出場數遞減排序。
如下所示：
```
Teams with four or more Rose Bowl wins as of 2014:
    USC: 24
    Washington: 8
    Michigan: 8
    Ohio State: 7
    Stanford: 6
    UCLA: 5
    Alabama: 4
    Michigan State: 4
```

#### 58
使用`USpresStatesDict.dat`這個檔案，索取一個first name並秀出所有符合的總統名。如果找不到的話就print找不到。
如下所示：
```
Enter a first name: John
    John Adams
    John Q. Adams
    John Kennedy
    John Tyler
```

### 60題應使用`LargeCitiesDict.dat`來作答
該檔案的格式為：
```
洲名:該洲的大城市
```
#### 60
寫一個程式來索取洲名並秀出其所包含的大城市。
如下所示：
```
Enter the name of a state: Arizona
Large cities: Phoenix Tucson Mesa
```
```
Enter the name of a state: Alabama
There are no large cities in Alabama.
```


## Programming Projects

#### 1 (Equivalent lengths, 長度單位換算)

|1 inch = .083333 foot | 1 rod = 16.5 feet|
|----------------------|------------------|
|1 yard = 3 feet       | 1 furlongg = 660 feet |
|1 meter = 3.28155 feet| 1 kilometer = 3281.5 feet|
|1 fathom = 6 feet | 1 mile = 5280 feet |

寫一個程式來秀出九種不同的長度單位名稱，並向使用者索取要轉換的來源及目的單位名稱，再把使用者所指定的長度轉換成指定的單位。
如下所示：
```
UTINS OF LENGTH
inches	furlongs	yards
rods	miles		fathoms
meters	kilometers	feet

Units to convert  from: yards
Units to convert to: miles
Enter length in yards: 555
Length in miles: 0.3153
```

#### 2 (Curve Grades)
\[avg = \frac{x_1+x_2+\cdots +x_n}{n}\]
\[std = \sqrt {\frac{(x_1-avg)^2+(x_2-avg)^2+\cdots +(x_n-avg)^2}{n}}\]
`Scores.txt`這個檔案包含了考試的成績。  
寫一個程式來計算出他們的平均值和成績，並依以下的公式來換算成等第：
\[ES \geq m + 1.5s\] --> A
\[m + .5s \leq ES < m + 1.5s\] --> B
\[m - .5s \leq ES < m + .5s\] --> C
\[m - 1.5s \leq ES < m - .5s\] --> D
\[ES < m - 1.5s\] --> F

如下所示：
```
Number of scores: 14
Average score: 71.0
Standard deviation of scores: 14.42
GRADE DISTRIBUTION AFTER CURVING GRADES:
A: 2	B: 1	C: 6	D: 4	F: 1
```
像是，如果avg = 70, s = 12，則88分以上都會得到A等第。


#### 3 (Baseball)
`ALE.txt`這個檔案包含了以下的資訊：

|Team 			| Won			|Lost			|
|-----------------------|-----------------------|-----------------------|
|Baltimore       	| 96			|66			|
|Boston			| 71			|91			|
|New York		| 84			|78			|
|Tampa Bay 		| 77			|85			|
|Toronto		| 83			|79			|

寫一個程式來把`ALE.txt`改寫成如下：

|Team 			| Won			|Lost			|%  |
|-----------------------|-----------------------|-----------------------|----|
|Baltimore       	| 96			|66			|0.593|
|New York		| 84			|78			|0.512|
|Toronto		| 83			|79			|0.438|
|Tampa Bay 		| 77			|85			|0.475|
|Boston			| 71			|91			|0.519|

%為勝的百分比。請依此數值遞減排列。

#### 4 (U.S. Senate)
`Senate113.txt`這個檔案包含了所有第113屆的美國立法會成員名字，也就是2014選前的立法會成員。每一筆資料都包含了：(名字、洲別、黨別)
`RetiredSen.txt`這個檔案包含了所有第113屆因敗選、退休或死亡而離開的美國立法會成員名字，也就是2014選後離開的立法會成員。每一筆資料都包含了：(名字、洲別、黨別)
`NewSen.txt`這個檔案包含了所有第114屆因勝選而加入的美國立法會成員名字，也就是2014選後加入的立法會成員。每一筆資料都包含了：(名字、洲別、黨別)

##### a
寫一個程式來建立`Senate114.txt`這個檔案。裡面應包含114屆的立法會成員。（參考`Senate113.txt`）

##### b
寫一個程式來計算出黨員的分佈數量。
如下：
```
Party Affiliations:
  Republicans: 54
  Democrats: 44
  Independents: 2
```

##### c
寫一個程式來找出代表立法會成員都是同黨派的洲數。

##### d
寫一個程式來索取洲名，並print出該洲所代表的兩名立法會成員。

#### 5 (Bachelor Degrees, 學士學位)

