#!/bin/sh
adb devices

python xclear_es.py

adb kill-server
pid=$(pgrep com.termux)
kill -9 $pid
