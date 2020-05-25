#!/bin/bash -x

UI_BASE="./enodo-ui"
API_BASE="./enodo-api"

# Dependencies
# node 8.12.0
# yarn 1.7.0
# Python 3.6.6

node -v
yarn -v
python3 --version

pushd "$UI_BASE"
yarn install
popd

pushd "$API_BASE"
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
popd

