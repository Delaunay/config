import argparse
import json
import os
import socket
from shutil import copyfile


def undefined_command(args):
    print(f'Command {args.cmd} is indefined')


def restore_machine_config(args):
    pass


def save_machine_config(args):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    files = json.load(open(f'{current_dir}/files.json'))
    hostname = socket.gethostname()

    destination = f'{current_dir}/{hostname}/'

    for file_property in files:
        name = file_property['name']

        if os.path.islink(name):
            pass

        elif os.path.isfile(name):
            file_path = f'{destination}/{name}'
            path, file = file_path.rsplit('/', maxsplit=1)
            os.makedirs(path)

            copyfile(name, file_path)

        elif os.path.exists(name):
            raise RuntimeError('Unsupported file type')

        else:
            pass


commands = {
    'save': save_machine_config,
    'restore': restore_machine_config
}

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='cmd')
save_parser = subparsers.add_parser('save')

restore_parser = subparsers.add_parser('restore')

args = parser.parse_args()

commands.get(args.cmd, undefined_command)(args)
