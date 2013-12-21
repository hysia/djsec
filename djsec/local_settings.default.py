#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Hysia --<hysia@huorui.net>
  Purpose: 
  Created: 12/21/13
  
Django local settings for djsec project.

For more information about djsec project, see
https://github.com/hysia/djsec/

"""

import os

DEBUG = True

TEMPLATE_DEBUG = DEBUG

# 线上域名 (DEBUG=False)
ALLOWED_HOSTS = []

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 数据库目录
DATABASE_DIR = os.path.join(BASE_DIR, 'database')

# 邮箱（默认、报错、管理员 发信邮箱）
EMAIL = ''

# 时区
TIME_ZONE = 'Asia/Shanghai'

# 语言
LANGUAGE_CODE = 'zh-cn'

# 每周的第一天
FIRST_DAY_OF_WEEK = 1

# 时间格式化
DATETIME_FORMAT = 'Y/m/d H:i:s'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATABASE_DIR, 'djsec.db'),
    }
}


#--- 以下配置不要改动 ---#

# 静态文件目录 
# 线上环境配置 Webserver 静态文件目录
STATICFILES_DIRS = (
    os.path.join(BASE_DIR , 'static'),
)

# 模板文件目录
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ADMINS = (
    ('admin', EMAIL),
)

# 默认发信邮箱
DEFAULT_FROM_EMAIL = EMAIL

MANAGERS = ADMINS