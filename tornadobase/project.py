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


def hello(args):
    print('Hello {0}'.format(args.who))


def new_project(args):
    print('create a new project at {0}'.format(args.path))


def start():
    pass


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='commands')

hello_parser = subparsers.add_parser(
    'hello',
    help='Proof of concept to further the command initiative')
hello_parser.add_argument('who', type=str)
hello_parser.set_defaults(command=hello)

new_parser = subparsers.add_parser(
    'new',
    help='Create a new tornadobase project')
new_parser.add_argument('path', type=str)
new_parser.set_defaults(command=new_project)

start_parser = subparsers.add_parser(
    'start',
    help='Start the web server')
start_parser.set_defaults(command=start)


def main():
    args = parser.parse_args()
    args.command(args)
