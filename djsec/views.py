#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Hysia --<hysia@huorui.net>
  Purpose: 
  Created: 12/21/13
"""

from django.http import Http404, HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    '''首页'''
    
    msg = 'test msg'

    return render_to_response('index.html', {
            'index': True,
            'msg': msg,
    }, context_instance=RequestContext(request))