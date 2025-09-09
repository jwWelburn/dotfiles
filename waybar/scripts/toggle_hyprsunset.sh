#!/bin/bash

PIDFILE="/tmp/hyprsunset.pid"

if [[ -f "$PIDFILE" ]]; then
    kill "$(cat "$PIDFILE")"
    rm "$PIDFILE"
    notify-send "Hyprsunset Disabled"
else
    hyprsunset --temperature "5000" & echo $! > "$PIDFILE"
    notify-send "Hyprsunset Enabled"
fi

