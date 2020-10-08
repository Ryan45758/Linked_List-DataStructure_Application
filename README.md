# Linked_List-DataStructure_Application
### 主要方向: 透過所附加的JSON檔用鏈結串列實作以下操作，JSON可使用的欄位為"姓名/學號"，"朋友清單"，"發表過的文章編號"，"文章按讚表"。
1. 讓使用者可以輸入學號"或"姓名。<br>
2. 使用者輸入特定的文章ID可以對該文章進行按讚，如果與該發文者為朋友的關係，則可按讚，否則顯示無權限。<br>
3. 可供使用者按讚過的文章取消按讚。<br>
4. 顯示欲查詢的學生按過讚的文章。<br>
5. 顯示輸入的文章有哪些人按過讚。<br>
6. 顯示關係最密切的兩人。<br>
### 簡介: 資料結構鏈結串列實作類資料庫CRUD
目錄架構 : <br>
主程式 : Linked_List-DataStructure_Application.py ， 資料表 : data.json
### .JSON 是什麼?<br>
簡單來說JSON就是一種輕量級的資料交換語言，該語言以易於讓人閱讀的文字為基礎，用來傳輸由屬性值或者序列性的值組成的資料物件。<br><br>
舉本例 : <br>
{<br>
&emsp;&emsp;"姓名/學號" : { ["Ada" , 1 ] },<br>
&emsp;&emsp;"朋友清單" : { "1": [3, 4, 6, 10, 19, 20, 23, 25, 26, 28, 29]},<br>
&emsp;&emsp;"發表過的文章編號" : { "1" : ["1A", "1B", "1C", "1D"] },<br>
&emsp;&emsp;"文章按讚表" : { "1A": [3, 4, 6, 10, 25, 29]}<br>
}<br>
這個簡易的第一個鍵儲存著"姓名/學號"，代表著有個人叫Ada且他的學號為1號。第二個鍵"朋友清單"儲存著1號同學總共有[3, 4, 6, 10, 19, 20, 23, 25, 26, 28, 29]這些朋友
### 目的: 對鏈結串列有更深入的理解，動手把玩Linked list。並實作類似資料庫的增刪改查，以及對JSON的操作。
