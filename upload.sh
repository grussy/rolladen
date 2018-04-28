#!/bin/bash
mpfshell -o ttyUSB0 -n -c 'rm main.py'
mpfshell -o ttyUSB0 -n --reset
mpfshell -o ttyUSB0 -n -c 'put main.py'
mpfshell -o ttyUSB0 -c repl

