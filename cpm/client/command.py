# Copyright 2021 curoky(cccuroky@gmail.com).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import codecs
import inspect
import logging
import signal
import sys
from difflib import get_close_matches

import jinja2
from conans.client.command import OnceArgument, SmartFormatter
from conans.errors import ConanException, ConanInvalidConfiguration
from conans.util.files import exception_message_safe
from conans.util.log import logger

from cpm import __version__ as client_version
from cpm.client.cpm_api import Cpm

# Exit codes for conan command:
SUCCESS = 0  # 0: Success (done)
ERROR_GENERAL = 1  # 1: General ConanException error (done)
ERROR_MIGRATION = 2  # 2: Migration error
USER_CTRL_C = 3  # 3: Ctrl+C
USER_CTRL_BREAK = 4  # 4: Ctrl+Break
ERROR_SIGTERM = 5  # 5: SIGTERM
ERROR_INVALID_CONFIGURATION = 6  # 6: Invalid configuration (done)


class Command(object):
    """A single command of the conan application, with all the first level commands. Manages the
    parsing of parameters and delegates functionality in collaborators. It can also show the
    help of the tool.
    """

    def __init__(self, cpm_api):
        assert isinstance(cpm_api, Cpm)
        self._cpm = cpm_api
        self._out = cpm_api.out

    def freeze(self, *args):
        """
        Output installed packages in requirements format.
        """
        parser = argparse.ArgumentParser(description=self.create.__doc__,
                                         prog='cpm freeze',
                                         formatter_class=SmartFormatter)
        parser.add_argument('path', type=str, help='dump path')
        args = parser.parse_args(*args)
        self._cpm.freeze(path=args.path)

    def install(self, *args):
        """
        Installs the requirements specified in a recipe (cpmfile.py).
        """

        parser = argparse.ArgumentParser(description=self.install.__doc__,
                                         prog='cpm install',
                                         formatter_class=SmartFormatter)
        parser.add_argument('name', help='name of package')
        parser.add_argument(
            '-r',
            '--requirement',
            help='Install from the given requirements file. This option can be used multiple times.'
        )
        args = parser.parse_args(*args)

        self._cpm.install(name=args.name, requirement=args.requirement)

    def list(self, *args):
        """
        List installed packags.
        """
        self._cpm.list()

    def create(self, *args):
        """
        Creates a new package recipe template with a 'cpmfile.py'.
        """

        parser = argparse.ArgumentParser(description=self.create.__doc__,
                                         prog='cpm create',
                                         formatter_class=SmartFormatter)
        parser.add_argument('name', type=str, help='name of package')
        parser.add_argument('-gp',
                            '--github_path',
                            default=None,
                            action=OnceArgument,
                            help='github path')

        args = parser.parse_args(*args)

        self._cpm.create(name=args.name, github_path=args.github_path)

    def _commands(self):
        """ Returns a list of available commands.
        """
        result = {}
        for m in inspect.getmembers(self, predicate=inspect.ismethod):
            method_name = m[0]
            if not method_name.startswith('_'):
                method = m[1]
                if method.__doc__ and not method.__doc__.startswith('HIDDEN'):
                    result[method_name] = method
        return result

    def _print_similar(self, command):
        """ Looks for similar commands and prints them if found.
        """
        matches = get_close_matches(word=command,
                                    possibilities=self._commands().keys(),
                                    n=5,
                                    cutoff=0.75)

        if len(matches) == 0:
            return

        if len(matches) > 1:
            self._out.writeln('The most similar commands are')
        else:
            self._out.writeln('The most similar command is')

        for match in matches:
            self._out.writeln('    %s' % match)

        self._out.writeln('')

    def run(self, *args):
        """HIDDEN: entry point for executing commands, dispatcher to class
        methods
        """
        ret_code = SUCCESS
        try:
            try:
                command = args[0][0]
            except IndexError:  # No parameters
                self._show_help()
                return False
            try:
                commands = self._commands()
                method = commands[command]
            except KeyError as exc:
                if command in ['-v', '--version']:
                    self._out.success('Conan version %s' % client_version)
                    return False

                self._warn_python_version()

                if command in ['-h', '--help']:
                    self._show_help()
                    return False

                self._out.writeln("'%s' is not a Conan command. See 'conan --help'." % command)
                self._out.writeln('')
                self._print_similar(command)
                raise ConanException('Unknown command %s' % str(exc))

            # if is_config_install_scheduled(self._conan) and \
            #    (command != "config" or (command == "config" and args[0] != "install")):
            #     self._conan.config_install(None, None)

            method(args[0][1:])
        except KeyboardInterrupt as exc:
            logger.error(exc)
            ret_code = SUCCESS
        except SystemExit as exc:
            if exc.code != 0:
                logger.error(exc)
                self._out.error('Exiting with code: %d' % exc.code)
            ret_code = exc.code
        except ConanInvalidConfiguration as exc:
            ret_code = ERROR_INVALID_CONFIGURATION
            self._out.error(exc)
        except ConanException as exc:
            ret_code = ERROR_GENERAL
            self._out.error(exc)
        except Exception as exc:
            import traceback
            print(traceback.format_exc())
            ret_code = ERROR_GENERAL
            msg = exception_message_safe(exc)
            self._out.error(msg)

        return ret_code


def main(args):
    logging.basicConfig(level=logging.DEBUG)
    # logging.basicConfig(level=logging.INFO)
    """ main entry point of the conan application, using a Command to
    parse parameters

    Exit codes for conan command:

        0: Success (done)
        1: General ConanException error (done)
        2: Migration error
        3: Ctrl+C
        4: Ctrl+Break
        5: SIGTERM
        6: Invalid configuration (done)
    """
    try:
        cpm_api, _, _ = Cpm.factory()
    except Exception as e:
        sys.stderr.write('Error in Conan initialization: {}'.format(e))
        sys.exit(ERROR_GENERAL)

    def ctrl_c_handler(_, __):
        print('You pressed Ctrl+C!')
        sys.exit(USER_CTRL_C)

    def sigterm_handler(_, __):
        print('Received SIGTERM!')
        sys.exit(ERROR_SIGTERM)

    def ctrl_break_handler(_, __):
        print('You pressed Ctrl+Break!')
        sys.exit(USER_CTRL_BREAK)

    signal.signal(signal.SIGINT, ctrl_c_handler)
    signal.signal(signal.SIGTERM, sigterm_handler)

    command = Command(cpm_api)
    error = command.run(args)
    sys.exit(error)
