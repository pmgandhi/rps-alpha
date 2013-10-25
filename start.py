from argh import arg
from argh.dispatching import dispatch_command

from claim import claim


@arg('port', type=int, help='The port number to bind to')
def start_app(port):
    claim.start(port)

if __name__ == '__main__':
    dispatch_command(start_app)
