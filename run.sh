#!/bin/bash

UI_BASE="./enodo-ui"
API_BASE="./enodo-api"

pushd "$API_BASE"
. .venv/bin/activate
python3 runflask.py &
FLASK_PID="$!"
popd

echo "$FLASK_PID" > flask.pid

pushd "$UI_BASE"
yarn serve &
VUE_PID="$!"
popd

echo "$VUE_PID" > vue.pid

