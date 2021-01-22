# @author Vsevolod Ivanov <seva@binarytrails.net>

import argparse
import traceback

__version__ = '0.1'
__author__ = 'Vsevolod (Seva) Ivanov'
__description__ = 'Pomoshchnik - Web Automation Assistant'
__banner__ = u"""
    ___  ____ _  _ ____ ____ _  _ ____ _  _ _  _ _ _  _ 
    |__] |  | |\/| |  | [__  |__| |    |__| |\ | | |_/  
    |    |__| |  | |__| ___] |  | |___ |  | | \| | | \_ 
"""

def get_parser():
    parser = argparse.ArgumentParser(__description__ + __banner__)
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    parser.add_argument('--run-loop', '-r', action='store_true', default=False)
    return parser
