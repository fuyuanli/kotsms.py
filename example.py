#!/usr/local/env python3
# -*- coding: utf-8 -*-

from kotsms import *

sms = kotsms()
sms.login("username", "passwd")
sms.sendMsg("phone", "Hello! Sent from kotsms.py")
