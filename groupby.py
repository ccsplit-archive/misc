#!/usr/bin/env python
"""
Usage:
    script [options]

Options:
    -n = n --nums = n       The numbers to group. [Default: [10,20,30,40]]
    -h --help               Show this help.
    -v --version            Show the version
"""
from docopt import docopt

def main(args):
    if type(args['--nums']) == str:
        import json
        args['--nums'] = json.loads(args['--nums'])
    print group_nums(args['--nums'])


def group_nums(num_array):
    from collections import Counter
    return Counter(map(lambda x: x/10*10, num_array)).most_common()

if __name__ == '__main__':
    main(docopt(__doc__, version='Script 1.0'))

