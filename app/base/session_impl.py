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
from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict
import os
import pickle

class SessionData(CallbackDict, SessionMixin):
    def __init__(self, initial=None, sid=None, cookie_id=None, new=False):
        def on_update(session_obj):
            session_obj.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        self.new = new
        self.cookie_id = cookie_id
        self.modified = False


class Session_impl(SessionInterface):
    session_class = SessionData
    serializer = pickle

    @classmethod
    def generate_sid(cls, cookie_session_id, request):
        # remote_addr = request.remote_addr
        # if remote_addr is None:
        #     remote_addr = 'localhost'
        # memcache_session_id = hashlib.md5('@'.join([remote_addr,  cookie_session_id])).hexdigest()
        # return memcache_session_id
        return cookie_session_id

    def open_session(self, app, request):
        cookie_session_id = request.cookies.get(app.session_cookie_name, None)
        if cookie_session_id is None:
            cookie_session_id = os.urandom(40).encode('hex')
            cache_session_id = self.generate_sid(cookie_session_id, request)
            return self.session_class(sid=cache_session_id, cookie_id=cookie_session_id, new=True)
        cache_session_id = self.generate_sid(cookie_session_id, request)
        val = app.session.get(cache_session_id)
        if val:
            data = self.serializer.loads(val)
            return self.session_class(data, cache_session_id, cookie_session_id)
        else:
            cookie_session_id = os.urandom(40).encode('hex')
            cache_session_id = self.generate_sid(cookie_session_id, request)
        return self.session_class(sid=cache_session_id, cookie_id=cookie_session_id, new=True)

    def save_session(self, app, session, response):
        expires = self.get_expiration_time(app, session)
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        if not session:
            app.session.delete(session.sid)
            if session.modified:
                response.delete_cookie(app.session_cookie_name,
                                       domain=domain)
            return
        # if session.modified: # all request update session
        dict_session = dict(session)
        dict_session['sid'] = session.sid
        val = self.serializer.dumps(dict_session)
        app.session.set(session.sid, val, ex=15*60)
        if session.new:
            response.set_cookie(app.session_cookie_name, session.cookie_id,
                                path=path, httponly=httponly, secure=secure, domain=domain)