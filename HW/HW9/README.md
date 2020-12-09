# 10901-Python-THU HW9

## 6.1
`stateCapital`這個list的構造需要用`StateANC.txt`來完成。
### 30 (State Capitals)
假設`stateCapitals`這個list包含了50個美國的洲首府。  
寫一段小程式來跟使用者索取一個洲首府的名字，並把其從該list中移除。
```
Enter a state capital to delete: Chicago
Not a state capital.
Enter a state capital to delete: Springfield
Capital deleted.
```


## 6.2  

### 10 (Perfect Square)
從1~10,000中隨機秀出一個完全平方數(包含端點)。


### 12 (Vowel)
隨機秀出一個母音('a', 'e', 'i', 'o', 'u')。


### 14 (Dice)
拋一雙dice 100,000次，並秀出總和為7的機會。

### 16 (U.S. States)
`StatesAlpha.txt`這個檔案中包含了50個美國的洲名(以字母序排序)，請寫一個程式來打亂其順序並寫入`RandomStates.txt`裡。

### 18 (Rock, Paper, Scissors)
寫一個程式來模擬"剪刀、石頭、布"這個遊戲，並秀出其結果。(兩方出手都是隨機的)
```
Player 1: paper
Player 2: scissors
Player 2 wins.
```

### 20 (Powerball Lottery)
該樂透的中獎號碼的産生方式為：  
隨機從編號1~59的白球中取出5顆，並1~35的紅球中選出一顆(Powerball)。
寫出一個程式來模擬100,000次的白球選取，每次都取出五顆。找出該五顆球具有兩個(含)以上連續的數字的機會。
```
31% of the time there were at least two consecutive numbers in the set of five numbers.
```

### 22 (Locate First Ace)
假設你洗了一疊52張牌的牌組，並一張一張翻開直到看見第一張A為止。  
平均而言，你至少要翻幾次牌才能看到第一張A的出現？  
寫一個程式來洗100,000次牌並根據這100,000次的資料來估計平均要翻開幾張牌才能看到A。  
Note: 你算出來的可能會跟範例不同，但應該會很接近10.6。
```
The average number of cards turned up was 10.61.
```
### 24 (State Capital Quiz)
利用`StatesANC.txt`中包含的洲名、洲名簡寫、洲的小名以及洲首府來製作一個測驗。
寫一個程式來隨機出5個洲名，並問使用者該洲的洲首府為何，並取得使用者的輸入。  
程式的最後要輸出總共錯了幾題，並幫使用者訂正答案。
```
What is the capital of Minnesota? Saint Paul
What is the capital of California? Sacramento
What is the capital of Illinois? Chicago
What is the capital of Alabama? Montgomery
What is the capital of Massachusetts? Boston

You missed 1 question.
Springfield is the capital of Illinois.
```
