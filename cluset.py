#! /usr/bin/env python

from flask import Flask, render_template
from ClusterShell.NodeSet import NodeSet

app = Flask(__name__)

@app.route("/")
def get_home():
    return render_template('index.html')

@app.route("/fold/<nodeset>")
def get_fold(nodeset):
    return str(NodeSet(nodeset))

@app.route("/expand/<nodeset>")
def get_expand(nodeset):
    return ' '.join(NodeSet(nodeset))

@app.route("/count/<nodeset>")
def get_count(nodeset):
    return "%d" % len(NodeSet(nodeset))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
