# @author Vsevolod Ivanov <seva@binarytrails.net>

from pomoshchnik import cli

if __name__ == '__main__':
    args = cli.get_parser().parse_args()
    if (args.run_loop):
        runner.loop()
