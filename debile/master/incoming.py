# Copyright (c) 2012-2013 Paul Tagliamonte <paultag@debian.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import os
import fnmatch

from debile.master.utils import session
from debile.utils.changes import parse_changes_file


def process_directory(path):
    abspath = os.path.abspath(path)
    for fp in os.listdir(abspath):
        path = os.path.join(abspath, fp)
        for glob, handler in DELEGATE.items():
            if fnmatch.fnmatch(path, glob):
                handler(path)
                break


def process_changes(path):
    changes = parse_changes_file(path)
    changes.validate()


def process_dud(path):
    pass


def reject_dud():
    pass


def accept_dud():
    pass


def reject_upload():
    pass


def accept_upload():
    pass


DELEGATE = {
    "*.changes": process_changes,
    "*.dud": process_dud,
}