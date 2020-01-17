from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_graphql import GraphQLView
from schema import schema

db = MongoEngine()

def create_app(env=None):
    from app.config import config_by_name
    
    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "Testing"])

    db.connect(db=app.config["MONGODB_SETTINGS"]["db"],
    username=app.config["MONGODB_SETTINGS"]["username"],
    password=app.config["MONGODB_SETTINGS"]["password"],
    host=app.config["MONGODB_SETTINGS"]["host"],
    authentication_source=app.config["MONGODB_SETTINGS"]["authentication_source"],
    port=app.config["MONGODB_SETTINGS"]["port"])

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    
    @app.route("/health")
    def health():
        return jsonify({"Message": "Healthy Status from {}".format(app.config["CONFIG_NAME"])})

    return app

"""
{
  allCloudAccounts {
    edges {
      node {
        id
        uid
        customer {
          id
          name
        }
        cloudProvider {
          id
          name
          abbreviation
        }
      }
    }
  }
}
"""

"""
{
  allCloudProviders {
    edges {
      node {
        id
        uid
        name
        abbreviation
      }
    }
  }
}
"""