import httplib
import logging

import tornado.web
from tornado.options import options


def server_settings(handler):
    handler.set_header('Server', options.server)
    handler.add_header('X-Frame-Options', options.x_frame_options)
    handler.add_header('X-XSS-Protection', options.x_xss_protection)
    handler.add_header('X-Content-Type-Options',
                       options.x_content_type_options)


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        server_settings(self)

    def write_error(self, status_code, **kwargs):
        reason = httplib.responses[status_code]
        self.render('errors/general.html',
                    status_code=status_code,
                    reason=reason)

    def get_current_user(self):
        return self.get_secure_cookie('user')

    def info(self, message):
        logging.info(message)

    def warn(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)
