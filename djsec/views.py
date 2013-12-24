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
def home(request):
    '''首页'''
    
    msg = 'test msg'

    return render_to_response('index.html', {
            'index': True,
            'msg': msg,
    }, context_instance=RequestContext(request))

@login_required
def show_dashboard(request):
    '''Dashboard page'''
    
    msg = 'dashboard'

    return render_to_response('index.html', {
            'msg': msg,
    }, context_instance=RequestContext(request))

def show_profile(request):
    '''Profile page'''
    
    return render_to_response('profile.html', {
            'index': True,
    }, context_instance=RequestContext(request))

def show_settings(request):
    '''Settings page'''
    
    return render_to_response('settings.html', {
            'index': True,
    }, context_instance=RequestContext(request))

def do_login(request):
    '''login page'''
    
    msg = "Sign in to continue to DjSec"
    username = password = ""
    next = "/"
    if request.GET:
        next = request.GET.get('next')
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        next = request.POST.get('next','/')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                msg = "You're successfully logged in!"
                return redirect(next)
            else:
                msg = "Your account is not active, please contact the site admin."
        else:
            msg = "Your username and/or password were incorrect."
             
    return render_to_response('login.html', {
            'msg': msg,
            'next': next,
    }, context_instance=RequestContext(request))

def do_logout(request):
    """logout"""
    
    logout(request)
    return redirect('/')
    
    