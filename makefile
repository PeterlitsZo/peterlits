
.PHONY: freeze
freeze:
	pip freeze > config/pip.txt

.PHONY: install
install:
	pip install -r config/pip.txt

