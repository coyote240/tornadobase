import tornado
from tornado.testing import AsyncHTTPTestCase
from tornadobase.handlers import BaseHandler
from tornadobase.application import Application


class TestApplication(AsyncHTTPTestCase):

    def get_app(self):
        class TestHandler(BaseHandler):
            def get(self):
                self.write('Test Handled')

        class TestApp(Application):
            def init_handlers(self):
                self.handlers = [
                    (r'/', TestHandler)]

        return TestApp()

    def test_index(self):
        response = self.fetch('/')
        server = response.headers.get('Server')

        self.assertEqual(response.code, 200)
        self.assertEqual(server, 'TornadoServer/{}'.format(tornado.version))
