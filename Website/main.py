from flask import Flask, render_template, request, redirect,send_file
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'