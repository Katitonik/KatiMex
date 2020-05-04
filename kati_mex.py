import sys
from argparse import ArgumentParser
from kati_mex import controller


def main(args):
    parser = ArgumentParser(description="KatiMex")
    parser.add_argument(
        '-m', '--mode',
        choices=['order', 'deliver'],
        default='order')
    try:
        function = parser.parse_args(args)
        code = controller.run(function.mode)
        print(code)
    except Exception:
        parser.print_help()


if __name__ == "__main__":
    main(sys.argv[1:])
