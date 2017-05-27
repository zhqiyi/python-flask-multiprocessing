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
import pkgutil
import logging
import app

class Register_impl(object):
    def __init__(self, app, exclude_packages=list()):
        core_packages = ["base"]
        core_packages.extend(exclude_packages)
        self.flask_app = app
        self.core_packages = core_packages
        self.reg_apps_packages = []
        self.run()

    def get_reg_packages(self):
        app_path = os.path.dirname(app.__file__)
        for _, name, is_package in pkgutil.iter_modules([app_path]):
            if is_package and name not in self.core_packages:
                self.reg_apps_packages.append(name)

    def register(self):

        for package in self.reg_apps_packages:
            module_name = "app." + package
            try:
                module = __import__(module_name, fromlist=["views"])
                reg = getattr(module, package)
                self.flask_app.register_blueprint(reg, url_prefix="/pfm/" + package,
                                                  template_folder='/Users/yizhq/工作/02-项目/04-selfcodes/pfm/app/templates/',
                                                  static_folder='/Users/yizhq/工作/02-项目/04-selfcodes/pfm/app/static') if reg and package else None

            except Exception, e:
                logging.warn("Register: " + str(module_name) + ":" + str(e), exc_info=1)

    def run(self):
        self.get_reg_packages()
        self.register()
