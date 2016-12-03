#!/usr/local/env python3
# -*- coding: utf8 -*-
import requests
import logging

class kotsms:
    def __init__(self):
        self.API_URL = "https://api2.kotsms.com.tw/kotsmsapi-2.php"
        self.API_POINT_URL = "https://api.kotsms.com.tw/memberpoint.php"

        logging.basicConfig(filename="kotsms.log", level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')
        self.logger = logging.getLogger("kotsms")

    def login(self, username, passwd):
        self.USERNAME = username
        self.PASSWORD = passwd

    def sendMsg(self, phone, sms):
        self.smslen = len(sms)
        self.PHONE = phone
        self.SMS = sms
        data = {
            "username" : self.USERNAME,
            "password" : self.PASSWORD,
            "dstaddr" : phone,
            "smbody" : sms.encode("big5"),
            "dlvtime" : 0
        }
        response = requests.get(self.API_URL, params=data)
        points = requests.get(self.API_POINT_URL, params={"username" : self.USERNAME, "password" : self.PASSWORD})
        self.points = int(points.text)
        self.responseDecoder(response.text)


    def responseDecoder(self, res):
        code = res.split("=")[1].split("\n")[0]
        errorMsg = {
            "-1" : "CGI string error ，系統維護中或其他錯誤 ,帶入的參數異常,伺服器異常",
            "-2" : "授權錯誤(帳號/密碼錯誤)",
            "-4" : "A Number違反規則 發送端 870短碼VCSN 設定異常",
            "-5" : "B Number違反規則 接收端 門號錯誤 ",
            "-6" : "Closed User 接收端的門號停話異常090 094 099 付費代號等",
            "-20" : "Schedule Time錯誤 預約時間錯誤 或時間已過",
            "-21" : "Valid Time錯誤 有效時間錯誤",
            "-1000" : "發送內容違反NCC規範",
            "-59999" : "帳務系統異常 簡訊無法扣款送出",
            "-60002" : "您帳戶中的點數不足",
            "-60014" : "該用戶已申請 拒收簡訊平台之簡訊 ( 2010 NCC新規)",
            "-999959999" : "在12 小時內，相同容錯機制碼",
            "-999969999" : "同秒, 同門號, 同內容簡訊",
            "-999979999" : "鎖定來源IP",
            "-999989999" : "簡訊為空"
        }
        if(int(code) < 0):
            msg = "[錯誤] %s : 點數剩餘 %d : %s" % (code, self.points, errorMsg[code])
            print(msg)
            self.logger.error(msg)
        else:
            msg = "[成功] %s : 點數剩餘 %d : 發送至 %s 傳送成功，簡訊長度為 %d 字, 內容為 : 「%s」 。" % (code, self.points, self.PHONE, self.smslen, self.SMS)
            print(msg)
            self.logger.info(msg)
