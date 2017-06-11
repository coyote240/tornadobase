import signal
import logging
import tornado.web
import tornado.ioloop
import tornado.autoreload
from tornado.httpserver import HTTPServer
from tornado.options import define, options


define('server', default='TornadoServer/{}'.format(tornado.version),
       help='The Server header returned with HTTP responses.')
define('port', type=int, default=8888,
       help='The port on which this app will listen.')
define('login_url', default='/login', help='Path to login form')
define('template_path', help='Location of template files.')
define('static_path', help='Location of static files.')
define('cookie_secret', help='Cookie secret key')
define('xsrf_cookies', default=True)
define('x_frame_options', default='DENY')
define('x_xss_protection', default=1)
define('x_content_type_options', default='nosniff')
define('debug', default=True)
define('config', help='Path to config file',
       callback=lambda path: options.parse_config_file(path,
                                                       final=False))


class Application(tornado.web.Application):

    def __init__(self):
        self.init_handlers()
        self.init_signal_handlers()

        settings = self.init_settings()

        tornado.web.Application.__init__(self, self.handlers, **settings)

    def init_settings(self):
        settings = {
            'debug': options.debug,
            'login_url': options.login_url,
            'template_path': options.template_path,
            'static_path': options.static_path,
            'xsrf_cookies': options.xsrf_cookies,
            'cookie_secret': options.cookie_secret}

        return settings

    def init_handlers(self):
        '''Assign handler objects to self.handlers'''

        raise NotImplementedError

    def init_signal_handlers(self):
        signal.signal(signal.SIGINT, self.interrupt_handler)
        if hasattr(signal, 'SIGQUIT'):
            signal.signal(signal.SIGQUIT, self.interrupt_handler)

    def interrupt_handler(self, signum, frame):
        logging.info('Shutting down server...')
        tornado.ioloop.IOLoop.instance().add_callback_from_signal(
            lambda: tornado.ioloop.IOLoop.instance().stop())

    def start(self):
        logging.info('Starting server...')
        options.parse_command_line()

        server = HTTPServer(self)

        if options.debug:
            server.listen(options.port)
            tornado.ioloop.IOLoop.instance().start()
        else:
            server.bind(options.port)
            server.start(0)
            tornado.ioloop.IOLoop.current().start()

        logging.info('Server instance running on port {}'.format(options.port))
