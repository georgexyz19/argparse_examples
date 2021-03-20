#!/usr/bin/env python3
# argparse_example.py
# This is a version using argparse
# revised by GHZ on 2/2019

import argparse

def main():

    parser = argparse.ArgumentParser(
        usage = 'usage: %(prog)s [options] filename'
    )

    parser.add_argument('-x', '--xhtml',
        action = 'store_true', dest = 'xhtml_flag',
        default = False,
        help = 'create a XHTML template instead of HTML'
        )

    parser.add_argument('-c', '--cssfile',
        action = 'store',
        dest = 'cssfile',
        default = 'style.css',
        help = 'CSS file to link',
    )

    parser.add_argument('filename', nargs='?',  # '*' for multiple files
        action = 'store',
        help = 'the name of file to be processed'
    )

    parser.add_argument('-V', '--version',
        action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    print(args)
    print(args.filename)

if __name__ == '__main__':
    main()

