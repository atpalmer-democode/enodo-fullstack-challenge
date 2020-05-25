# Enodo Fullstack Challenge

## Requirements

This application was developed with the following developer tools:

* node 8.12.0
* yarn 1.7.0
* python 3.6.6
* bash 4.4.23 (optional dependency used by install scripts)

## Installation

To install application dependencies, navigate to the root directory of this repository and execute the following command:

```
    $ ./install.sh
```

This script runs `yarn install` to install UI dependencies, runs `python3 -m venv` to create a Python virtual environment, and runs `pip install` to install Python dependencies within the newly created virtual environment.

## Serving Locally

To serve the application locally on your machine, using development servers, navigate to the root directory of this repository and run the following command:

```
    $ ./run.sh
```

This command starts separate development servers for the Flask-based API application and the Vue-based UI application using default ports (5000 and 8080 respectively).

The application should be available at `http://localhost:8080/`.

## Shutdown

Starting the application with `run.sh` will save the PIDs for each of the running servers in files named `vue.pid` and `flask.pid`.

Run `shutdown.sh` to read these files and shut down the processes corresponding to each server PID.

```
    $ ./shutdown.sh
```

## Testing

An end-to-end test, written using Selenium, is included in the `tests` directory. See further notes inside `tests`.

