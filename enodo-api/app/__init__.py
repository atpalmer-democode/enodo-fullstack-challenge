from flask import Flask
from .routes import load_routes
from .hooks import apply_hooks


flask = Flask(__name__)


load_routes(flask)
apply_hooks(flask)

