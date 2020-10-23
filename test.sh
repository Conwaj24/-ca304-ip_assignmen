#!/bin/sh
python ip_calculator.py < 1in | diff /dev/stdin 1out

