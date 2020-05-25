#!/bin/bash

kill -TERM $(cat vue.pid) && rm "vue.pid"
kill -TERM $(cat flask.pid) && rm "flask.pid"

