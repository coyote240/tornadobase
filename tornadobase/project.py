import argparse
'''
Project

Basic command controller to facilitate easy setup of new
tornadobase applications.

tornadobase new <path>
* base application with single hello world handler
* base hello world handler
* templates directory with hello world template
* default configuration file
* base tests for application and handlers
* directories for models, assets, etc.
* console script for starting server
'''


class Command(object):
    '''Command function decorator.
    '''
    commands = {}

    def __init__(self, label, *args):
        self.label = label

    def __call__(self, command):
        def wrapped_command(**kwargs):
            command(**kwargs)

        self.__class__.commands[self.label] = wrapped_command
        return wrapped_command

    @classmethod
    def call(cls, **kwargs):
        cmd = cls.commands.get(kwargs.get('command'))
        if cmd is None:
            raise Exception('Command not defined')
        cmd(**kwargs)


@Command('hello')
def hello(**kwargs):
    print('Hello {who}'.format(**kwargs))


@Command('new')
def new_project(**kwargs):
    print('create a new project at {path}'.format(**kwargs))


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='commands', dest='command')

    hello_parser = subparsers.add_parser(
        'hello',
        help='Proof of concept to further the command initiative')
    hello_parser.add_argument('who', type=str)

    new_parser = subparsers.add_parser(
        'new',
        help='Create a new tornadobase project')
    new_parser.add_argument('path', type=str)

    args = parser.parse_args()

    Command.call(**vars(args))
