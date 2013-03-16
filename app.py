import os
import re
import logging
import random
from logging.handlers import RotatingFileHandler
from flask import Flask
from flaskext.markdown import Markdown

# Setup Flask App
app = Flask(__name__)

# Initialize Markdown Processing
md = Markdown(app,
              safe_mode=False,
              output_format='html5',
             )

# Logging configuration
file_handler = RotatingFileHandler('/var/log/nateferrero.gallery.log')
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)


# Home Routing
@app.route("/")
def home():
    return "Locker is here"

if __name__ == "__main__":
    app.run(port=2005)
