
all: code site


site:
	python3 site_gen.py

code:
	python3 code_gen.py

.PHONY: site code
