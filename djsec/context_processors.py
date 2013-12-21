#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Hysia --<hysia@huorui.net>
  Purpose: 
  Created: 12/21/13
"""

from django.conf import settings

def consts(request):
        ret = {}
        for i in ('THEME', 'EMAIL'):
                ret[i] = getattr(settings, i)
        return ret