#!/usr/bin/env python
"""Generate diagrams from imposm mapping schema and tm2source project.
Usage:
  enqueue-jobs.py <queue> [--host=<host>] [--port=<port>]
  enqueue-jobs.py (-h | --help)
  enqueue-jobs.py --version
Options:
  -h --help         Show this screen.
  --version         Show version.
  --host=<host>     Host of Beanstalkd server [default: localhost]
  --port=<port>     Port of Beanstalkd server [default: 11300]
"""
import sys
import beanstalkc
from docopt import docopt


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')
    queue = args.get('<queue>')
    print(args.get('--host'))
    beanstalk = beanstalkc.Connection(host=args.get('--host'),
                                      port=int(args.get('--port')))
    beanstalk.use(queue)
    for line in sys.stdin:
        beanstalk.put(line, ttr=3600)
