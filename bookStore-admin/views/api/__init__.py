# -*- coding: utf-8 -*-

from functools import wraps
from bookStore import app


def exports(rule, **options):
    """
    无签名验证的 API 使用这个装饰器，自动添加 /webapi/ 前缀
    """
    def decorator(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            app.logger.debug("Web API: %s.%s" % (fn.__module__, fn.__name__))
            return fn(*args, **kwargs)

        api_rule = '{}/webapi{}'.format(app.config['APPLICATION_ROOT'], rule)
        endpoint = options.pop('endpoint', api_rule)
        app.add_url_rule(api_rule, endpoint,
                         view_func=decorated_view, **options)
        return decorated_view
    return decorator
