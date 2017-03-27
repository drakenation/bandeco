#!/usr/bin/env bash

@Phony: help
@Phony: install

help:
	@echo "install: installs the package in your machine"

install:
	python setup.py install
