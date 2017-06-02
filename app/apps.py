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

import os
import logging
# from common.redis_impl import Redis_impl
# from common.session_impl import Session_impl
from app.base.register_impl import Register_impl
# from settings import APP_CACHE, APP_SESSION
from flask import Flask, g
from utils.db.postgredb import DbClass
from configs import config
from .languages.language_impl import Language_IMPL, language
from .decorators import pfm_debug_logging

global db

class WingsAppHolder(object):
    def __init__(self, app, db):
        """init before request"""
        self.app = app
        self.db = db

        self.app.before_request(self.before_request)
        self.app.after_request(self.after_request)
        self.app.teardown_request(self.teardown_request)

    '''
        每一个请求之后绑定一个函数，如果请求没有异常
    '''
    def after_request(self, response):
        """handle after request"""
        session = g.pg_db
        if session:
            session.close()

        if response is not None:
            return response

    '''
        在请求收到之前绑定一个函数做一些事情
    '''
    def before_request(self):
        """handle before request"""
        session = self.db.make_session()
        g.pg_db = session()

        # initialize es
        # g.es = EsBase.create_es_client()
        # g.es_post = EsBase.create_es_post(url_prefix=ES_POST_PREFIX)
        # g.es_dsl = EsBase.create_es_dsl()

    '''
        每一个请求之后绑定一个函数，即使遇到了异常
    '''
    def teardown_request(self, exception):
        """handle teardown request"""
        if exception is not None:
            logging.warn("[{0} {1}] an exception occurred to this request: {2}".
                         format("app.py", "WingsAppHolder", exception), exc_info=1)

def _bind_database(app, db):
    """bind database"""
    return WingsAppHolder(app, db)


def _init_database(app, db):
    """init database"""
    pass

@pfm_debug_logging
def init_app(app_name=None, config_name=None):
    """create app"""

    # initialize app
    if app_name is None:
        app_name = __name__
    app = Flask(app_name,
                template_folder="app/templates",
                static_folder="app/static")
    app.config.from_object(config[config_name])

    # init language
    Language_IMPL().init_language(app.config.__getitem__("LANGUAGE_SET"))
    # app.lang.from_object(language)

    # initialize database
    db = DbClass(app.config.__getitem__("POSTGRESQL_DATABASE_URI"))
    with app.config.__getitem__("PROCESS_FILE_LOCK"):
        _init_database(app, db)
    _bind_database(app, db)

    return app, db

"""create flask app."""
def create_app(app_name=None, config_name=None):
    app, db = init_app(app_name, config_name)
    # app.cache = Redis_impl(**APP_CACHE)
    # app.session = Redis_impl(**APP_SESSION)
    # app.session_interface = Session_impl()
    Register_impl(app)

    return app, db

