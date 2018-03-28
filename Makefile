#-----------------------------------
# Makefile - s3-mfa-delete
#-----------------------------------

.PHONY:  help


help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


#--------------------------------------------
# Virtualenvwrapper setup
#--------------------------------------------

SHELL:=/bin/bash
VIRTUAL_ENV_NAME:=s3-mfa-delete
VIRTUAL_ENV_INSTALL:=~/.virtualenvs/$(VIRTUAL_ENV_NAME)/bin/activate
PIP_INSTALL:=~/.virtualenvs/$(VIRTUAL_ENV_NAME)/bin/pip

$(VIRTUAL_ENV_INSTALL):
	( \
	source $(VIRTUALENVWRAPPER_SCRIPT) ; \
	mkvirtualenv $(VIRTUAL_ENV_NAME) --python=/usr/local/bin/python3.6 ; \
	touch ~/.virtualenvs/$(VIRTUAL_ENV_NAME)/bin/activate ; \
	)


$(PIP_INSTALL): $(VIRTUAL_ENV_INSTALL) requirements.txt
	( \
	source $(VIRTUALENVWRAPPER_SCRIPT) ; \
	workon $(VIRTUAL_ENV_NAME) ; \
	pip install -r requirements.txt ;\
	touch ~/.virtualenvs/$(VIRTUAL_ENV_NAME)/bin/pip ;\
	)

setup: $(PIP_INSTALL) ## Setup Python virtualenv


executable: ## Build executable
	pyinstaller --onefile s3-mfa-delete.py


clean: ## Clean up build artifacts
	rm -rf build dist __pycache__ *.spec
