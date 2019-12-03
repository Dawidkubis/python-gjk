# code_gen.py
```python
#!/usr/bin/python3

from site_gen import get_ext
import os

def mkformat(name, lines):
	result = []
	result.append(f'# {name}\n')
	result.append('```python\n')
	result += lines
	result.append('```')
	return result

if __name__=='__main__':
	files = [(i + '.py', i + '.md') for i in get_ext('.', '.py')]
	
	for py, md in files:
		with open(py) as p:
			with open(md, 'w') as m:
				m.writelines(mkformat(os.path.split(p.name)[1], p.readlines()))
```