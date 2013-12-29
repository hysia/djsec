#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Hysia --<hysia@huorui.net>
  Purpose: 
  Created: 12/21/13
"""

from datetime import datetime 
from django.conf import settings
from django.db import models

class XssData(models.Model):
	id = models.AutoField(null=False, primary_key=True, blank=True)
	uid = models.IntegerField(max_length=10, null=False,help_text="user id")
	created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	ip = models.CharField(max_length=30, null=False, help_text="client ip")
	cookies = models.TextField(default='')
	domain = models.CharField(max_length=100,null=False)
	flash = models.CharField(max_length=30,null=True)
	lang = models.CharField(max_length=10,null=True)
	location = models.CharField(max_length=300,null=False)
	platform = models.CharField(max_length=30,null=True)
	referrer = models.CharField(max_length=300,null=True)
	screen = models.CharField(max_length=10,null=True)
	title = models.CharField(max_length=300,null=True)
	toplocation = models.CharField(max_length=300,null=True)
	opener = models.CharField(max_length=300,null=True)
	ua = models.CharField(max_length=300,null=True)
	extra = models.TextField(default='')
	
	class Meta:
		db_table = '%s_xss_data' %settings.TABLE_PREFIX
		
class XssSnippers(models.Model):
	id = models.AutoField(null=False, primary_key=True, blank=True)
	uid = models.IntegerField(max_length=10, null=False,help_text="user id")
	share_with = models.CharField(max_length=300,null=False)
	is_public = models.NullBooleanField(null=True, default=False)
	codz = models.TextField(default='')
	desc = models.CharField(max_length=300,null=False, blank=True)
	
	class Meta:
		db_table = '%s_xss_snippers' %settings.TABLE_PREFIX
		