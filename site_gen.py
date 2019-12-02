#!/usr/bin/python

import os

PREFIX = '''# python-gjk

Učí profesor Kubis a docent Veškrna.

'''.splitlines()

def get_mds(path):
	results = []
	for i in os.listdir(path):
		if i[0] == '.':
			continue
		if os.path.isdir(i):
			results = results + get_mds(os.path.join(path, i))
		else:
			name, extension = os.path.splitext(i)
			if extension == ".md":
				results.append(os.path.join(path, name))
	return results

def mkformat(files):
	result = []
	

files = [i for i in get_mds('.') if i != './README']
with open('README.md', 'w') as f:
	f.writelines(PREFIX + mkformat(files))
