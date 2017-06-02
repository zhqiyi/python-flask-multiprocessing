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

class Language_IMPL:
    com_msg = {}

    def __init__(self):
        self.lang_set = 'zh'
        self.core_class = ["language_impl"]

    def init_language(self, lang_set=None):

        '''

        :param lang_set: ZH,zh:中文(default) EN,en:英文
        :return:
        '''
        if lang_set is not None:
            self.lang_set = lang_set.lower()

        import os, sys
        import pkgutil
        import inspect

        lang_path = os.path.dirname(inspect.getfile(sys.modules[__name__]))
        for _, name, is_package in pkgutil.iter_modules([lang_path]):
            if name not in self.core_class:
                package = 'app.languages.' + name
                module = __import__(package, fromlist=['msg_*'])
                item = getattr(module, name)
                child_obj = item[self.lang_set]
                language['messages'].append(child_obj)

    def release_language(self, ):


language = {
    'messages': []
}