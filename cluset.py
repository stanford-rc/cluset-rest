#! /usr/bin/env python
# REST API to ClusterShell NodeSet class
# Copyright (C) 2016 Stephane Thiell <sthiell@stanford.edu>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


from flask import Flask, render_template
from ClusterShell.NodeSet import NodeSet

app = Flask(__name__)

import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

list_files('/app')

@app.route("/")
def get_home():
    return render_template('index.html')

def compute_nodeset(data):
    """compute the NodeSet object from textbox data"""
    xset = NodeSet()
    for nodeset in data.split():
        xset.update(nodeset)
    return xset

@app.route("/fold/<data>")
def get_fold(data):
    return str(compute_nodeset(data))

@app.route("/expand/<data>")
def get_expand(data):
    return ' '.join(compute_nodeset(data))

@app.route("/count/<data>")
def get_count(data):
    return "%d" % len(compute_nodeset(data))

if __name__ == '__main__':
    app.run(debug=True)
