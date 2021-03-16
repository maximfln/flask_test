from flask import Flask, render_template, request, make_response, jsonify
from markupsafe import Markup
from components.index_page import Index_Page

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Markup.escape('<h1>hello world!</h1>')