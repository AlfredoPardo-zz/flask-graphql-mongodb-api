from flask import Flask, jsonify
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(env=None):
    from app.config import config_by_name
    
    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "Testing"])
    
    @app.route("/health")
    def health():
        return jsonify({"Message": "Healthy Status from {}".format(app.config["CONFIG_NAME"])})

    return app
