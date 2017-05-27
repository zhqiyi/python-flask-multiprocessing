# -*- coding: utf-8 -*-
'''
# Author: Dave
# Email: yizhqi@gmail.com
#             
#                       __------__  
#                     /~           ~\  
#                    |     //^\\//^\|  
#                  /~~\   ||   o| |o|:~\  
#                 | |6    ||___|_|_||:|  
#                  \__.   /       o   \/'  
#                   |    (        O    )  
#          /~~~~\     `\   \          /  
#         | |~~\ |      )   ~------~`\  
#        /' |   | |    /      ____ /~~~)\  
#       (_/'    | | |      /'     |     ( |  
#              | | |      \     /    __)/ \  
#              \   \ \       \/     /' \    `\  
#                \   \|\         /    | |\___|  
#                  \ |   \____/      | |  
#                  /^~>   \         _/ <  
#                 |   |          \        \  
#                 |   | \         \         \  
#                 -^-\   \        |         )  
#                      `\_______/^\______/  
#
#               Please, Do not go wrong!!!
'''
import logging
import uuid
import hashlib
from datetime import datetime
from functools import wraps
from flask import g, session, request, jsonify, current_app, render_template

def generate_csrf_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'csrf_token' not in session:
            session['csrf_token'] = token_uuid()
        session['csrf_timeout'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f(*args, **kwargs)
    return decorated_function

def token_uuid():
    uid = ''
    uname = ''
    uid = str(uuid.uuid1())
    uname = session.get('username', '')
    return hashlib.md5(uid+uname).hexdigest()