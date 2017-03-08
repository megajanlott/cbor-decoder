#!/usr/bin/env python3
"""
Does pylint linting and pycodestyle (PEP8) code style checks on the modules.
"""
import os
import sys
from pycodestyle import Checker, StyleGuide
import pylint.lint

ROOT_PATH = os.path.join(os.path.dirname(__file__), '..')
MODULES_TO_CHECK = ['cbor', 'scripts']
PEP8_OPTIONS = StyleGuide(config_file=os.path.join(ROOT_PATH, 'setup.cfg')).options


def pep8_file(filename):
    """return whether the given file passes PEP8 standards"""
    checker = Checker(filename=filename, options=PEP8_OPTIONS)
    return checker.check_all() == 0


def pep8_module(module_name):
    """return whether the given module passes PEP8 standards"""
    success = True
    for subdir, dirs, files in os.walk(os.path.join(ROOT_PATH, module_name)):
        for file in files:
            if file[-3:] == '.py':
                if not pep8_file(os.path.join(subdir, file)):
                    success = False
    return success


def lint_module(module_name):
    """return whether the given module passes linting"""
    status = pylint.lint.Run(['-r', 'n', module_name], None, False).linter.msg_status
    evaluation = {
        'has_fatal': status & 1 == 1,
        'has_error': status & 2 == 2,
        'has_warning': status & 4 == 4,
        'has_refactor': status & 8 == 8,
        'has_convention': status & 16 == 16,
    }
    return not evaluation['has_fatal'] and not evaluation['has_error']


def main():
    """script entry point"""
    successful = True
    for module in MODULES_TO_CHECK:
        lint_failed = not lint_module(module)
        pep8_failed = not pep8_module(module)
        if lint_failed or pep8_failed:
            successful = False
    print("")
    if not successful:
        print("Linting found issues in the code. Please fix them.")
        sys.exit(1)
    print("No significant issues found in the code. Go on!")
    sys.exit(0)


if __name__ == '__main__':
    main()
