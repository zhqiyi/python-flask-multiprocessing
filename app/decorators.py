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
import sys
import logging
import uuid
import hashlib
import inspect, os
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

def pfm_debug_logging(f):
    @wraps(f)
    def make_logging(*args, **kwargs):

        caller_file = inspect.stack()[1][1]
        script_path = os.path.abspath(os.path.dirname(caller_file))

        logging.debug('\ncurrent method: %s;\ncurrent script: %s;\n'
                      % (f.__name__, script_path), exc_info=True)

        return f(*args, **kwargs)
    return make_logging
