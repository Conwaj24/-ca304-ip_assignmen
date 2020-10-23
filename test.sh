#!/bin/sh
python ip_calculator.py < 1in | diff 1out /dev/stdin

