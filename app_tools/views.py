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
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def tools_index(request):
    '''Tools page'''
    
    msg = 'tools'

    return render_to_response('tools/index.html', {
            'msg': msg,
    }, context_instance=RequestContext(request))