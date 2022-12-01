.SILENT:
.PHONY: all format check
all:
	for file in *.py ; do \
		python $$file ; \
	done

format:
	black *.py

check:
	flake8 *.py
