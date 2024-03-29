#!/bin/sh
adb devices

python xclear.py

adb kill-server
pid=$(pgrep com.termux)
kill -9 $pid
