#!/bin/bash
mpfshell -o ttyUSB0 --reset -n -c 'put main.py'
mpfshell -o ttyUSB0 --reset -c repl

