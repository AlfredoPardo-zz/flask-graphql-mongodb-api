from flask import Flask, url_for
import urllib
import os
import yaml

def strftime(date, fmt):
    return date.strftime(fmt.encode('utf-8')).decode('utf-8')

config = None

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

app = Flask(__name__)

@app.context_processor
def override_url_for():

    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

app.jinja_env.filters['strftime'] = strftime
app.jinja_env.filters['quote_plus'] = lambda u: urllib.parse.quote_plus(u)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

app.secret_key = config["SECRET_KEY"]

from blueprints.main import main_bp

app.register_blueprint(main_bp)