# possibilities:
# run mongodb command
# create db and collection
# import the json file to the collection

# set environment variables for development
SHELL := /bin/zsh

VENV := ${PWD}/hymnal_venv/bin/activate

install:
	source ${VENV}; \
	pip install -r requirements.txt; \

# the virtualenv context as to be there to do python commands
server: install
	source ${VENV}; \
	gunicorn -w 2 --bind 0.0.0.0:5000 wsgi; \