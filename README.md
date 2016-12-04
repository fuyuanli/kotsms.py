簡訊王 Python 非官方 API
===

## 簡介

簡訊王 API，使用 requests 搭配官方 [全功能進階技術介接 - 簡訊 API](https://www.kotsms.com.tw/index.php?selectpage=pagenews&kind=4&viewnum=238)串接。

Log 功能：
- 時間
- 手機號碼
- 簡訊內容
- 剩餘點數
- 錯誤訊息
- 簡訊字數

皆會保存於 kotsms.log 中。

```txt=
[INFO] 2016-12-04 21:03:48,958 - [成功] 12345678 : 點數剩餘 13 : 發送至 0912345678 傳送成功，簡訊長度為 20 字, 內容為 : 「kotsms Python API 發送」 。
[ERROR] 2016-12-04 21:03:49,128 - [錯誤] -999989999 : 點數剩餘 13 : 簡訊為空
```


## 安裝

### 建立 Virtual Environment

```bash
$ virtualenv -p python3 env
$ source env/bin/activate
```
### 安裝 requests, kotsms

```bash
$ pip install requests
$ pip install kotsms
```

## 使用

```python3=
#!/usr/local/env python3
# -*- coding: utf-8 -*-

from kotsms import *

USERNAME = "帳號"
PASSWORD = "密碼"

PHONE = "手機號碼"
MESSAGE = "簡訊內容"

sms = kotsms()
sms.login(USERNAME, PASSWORD)
sms.sendMsg(PHONE, MESSAGE)
```

![](http://i.imgur.com/glFEm3D.png)
