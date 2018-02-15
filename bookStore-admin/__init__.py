# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from . import default_settings

db = SQLAlchemy()

class Application(Flask):

    def __init__(self):
        super(Application, self).__init__(
            __name__, static_folder='../static'
        )
        self.config.from_object(default_settings)

        # 生产环境配置
        if 'APP_CONFIG' in os.environ:
            self.config.from_envvar('APP_CONFIG', silent=False)
        else:
            dev_cfg = os.path.abspath(os.path.join(
                os.path.basename(__file__), '../dev.cfg'))
            self.config.from_pyfile(dev_cfg, silent=True)

        if os.path.exists('config_local.py'):
            self.config.from_pyfile('../config_local.py')

    def prepare_login_manager(self):
        login_manager = LoginManager()
        login_manager.init_app(self)

        @login_manager.user_loader
        def load_user(id):
            from bookStore.service.user.user import UserService
            return UserService.get(id)

    def ready(self):
        db.init_app(self)
        self.prepare_login_manager()

        if not app.debug:
            import logging
            from logging import StreamHandler
            import sys

            hdl = StreamHandler(sys.stderr)
            fmt = logging.Formatter((
                '[%(asctime)s %(levelname)-9s '
                '%(module)s:%(lineno)d <%(process)d>] %(message)s'))

            hdl.setFormatter(fmt)
            hdl.setLevel(logging.INFO)
            app.logger.addHandler(hdl)
            app.logger.setLevel(logging.INFO)

app = Application()
