PWD:=$(shell pwd)

build: 
	docker build -t foreman-python-client .

run:   
	docker run -it --rm -v ${PWD}:/app foreman-python-client python script.py $(ARG)
