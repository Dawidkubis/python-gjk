#!/usr/bin/python3

import os
from functools import reduce

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
	files = [list(os.path.split(i)) for i in files]
	files = path_dict(files)

	for key in files:
		if 'README' in files[key]:
			result.append(f'## [{key}]({key})')
		else:
			result.append(f'## {key}')
		for name in [i for i in sorted(files[key]) if i != 'README']:
			result.append(f'+ [{name}]({os.path.join(key, name)})')
		result.append('')
	
	return result

	
def path_dict(files):
	di = dict()
	for x, y in files:
		if not di.get(x):
			di[x] = []
		di[x].append(y)
	return di

if __name__=='__main__':
	prefix = []
	if os.path.exists('PREFIX.md'):
		with open('PREFIX.md') as p:
			prefix = p.readlines()

	files = sorted([i[2:] for i in get_mds('.') if i != './README' and i != './PREFIX'])

	with open('README.md', 'w') as f:
		to_write = mkformat(files)
		to_write = [i + '\n' for i in to_write]
		to_write = prefix + to_write
		f.writelines(to_write)
