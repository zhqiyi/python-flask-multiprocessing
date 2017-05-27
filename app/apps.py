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
from configs import config

class WingsAppHolder(object):
    def __init__(self, app, db):
        """init before request"""
        self.app = app
        self.db = db
        self.app.before_request(self.before_request)
        self.app.teardown_request(self.teardown_request)

    def before_request(self):
        """handle before request"""

    def teardown_request(self, exception):
        """handle after request"""
        # session = g.apt_db
        session = g.pg_db
        if session:
            session.close()
        if exception is not None:
            logging.warn("[{0} {1}] an exception occurred to this request: {2}".format("app.py","WingsAppHolder",exception), exc_info=1)


def _bind_database(app, db):
    """bind database"""
    return WingsAppHolder(app, db)


def _init_database(app, db):
    """init database"""
    pass


def init_app(app_name=None, config_name=None):
    """create app"""

    if app_name is None:
        app_name = __name__
    app = Flask(app_name,
                template_folder="app/templates",
                static_folder="app/static")
    app.config.from_object(config[config_name])

    return app

"""create flask app."""
def create_app(app_name=None, config_name=None):
    app = init_app(app_name, config_name)
    # app.cache = Redis_impl(**APP_CACHE)
    # app.session = Redis_impl(**APP_SESSION)
    # app.session_interface = Session_impl()
    Register_impl(app)

    return app

def run_app():
    flask_app = create_app('pfm_flask_app', os.getenv('XXXX_CONFIG') or 'default')
    flask_app.secret_key = os.urandom(24)
    flask_app.run(host='0.0.0.0', port=5001)
