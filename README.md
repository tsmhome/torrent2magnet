# torrent2magnet

分析 BT 下載大站，btbtt12.com，批量轉成 magnet，跳過下載 torrent 步驟，並支援批量轉換。

#如何使用？
1. 需安裝這些依賴包
pip install bencode.py
pip install hashlib
pip install beautifulsoup4

2. Double click 執行 torrent2magnet.py
3. 
====================

**案例 1**<br>
torrent 直接轉換，輸入 torrent 直接網址<br>
e.g : https://domain/xxx.torrent

**案例 2**<br>
btbtt12.com 下載頁面網址，如下載內容 > 只有一個表格，會自動把表格內容轉換成 magnet<br>
e.g : http://btbtt12.com/thread-index-fid-951-tid-4684816.htm

**案例 3**<br>
btbtt12.com 下載頁面網址，如下載內容 > 多於一個表格，出現 "**表格號碼**" 輸入框，就會把輸入的 "**表格號碼**" 內容轉換成 magnet<br>
e.g : http://btbtt12.com/thread-index-fid-981-tid-4663100.htm
