#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'Markus Beuckelmann'
__author_email__ = 'email@markus-beuckelmann.de'
__version__ = '0.1.0'

from flask import Flask, jsonify, abort, redirect, url_for
from flask import render_template

import json
import os
from random import randint


app = Flask(__name__)

data = {}

@app.before_first_request
def load():

	global data

	path = 'data'
	for f in os.listdir(path):
		if f.endswith('.json'):
			language = f.replace('.json', '')
			data[language] = json.load(open('/'.join([path, f]), 'r'))

@app.route('/')
def index():
	return redirect(url_for('languages', language = 'en'))

@app.route('/<language>', methods = ['GET'])
def languages(language):
	return render_template('batyr.html', language = language)

@app.route('/items/random/<language>', methods = ['GET'])
def items(language):

	if data.has_key(language):
		return jsonify(data[language][randint(0, len(data[language]))])
	else:
		abort(404)

if __name__ == '__main__':

	app.debug = True
	app.run()
