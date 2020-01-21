from . import main_bp as main
from flask import render_template, request, redirect, session
from graphqlclient import GraphQLClient
from app import config
import json

graphql_url = 'http://{}:{}/graphql'.format(config["BACKEND_URL"], config["BACKEND_PORT"])

@main.route('/', methods=["GET"])
def customers():

    client = GraphQLClient(graphql_url)

    result = client.execute('''
    query   {
        allCustomers {
            edges {
            node {
                id
                uid
                name
            }
            }
        }
    }
    ''')
    
    return render_template("customers.jade", customers=json.loads(result)["data"]["allCustomers"]["edges"])

@main.route('/cloud_providers', methods=["GET"])
def cloud_providers():

    client = GraphQLClient(graphql_url)

    result = client.execute('''
    query   {
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
    ''')
    
    return render_template("cloud_providers.jade", cloud_providers=json.loads(result)["data"]["allCloudProviders"]["edges"])


@main.route('/cloud_accounts', methods=["GET"])
def cloud_accounts():

    client = GraphQLClient(graphql_url)

    # This can be minimized
    result = client.execute('''
    query   {
        allCloudAccounts {
            edges {
            node {
                id
                uid
                name
                customer {
                id
                uid
                name
                }
                cloudProvider {
                id
                uid
                name
                abbreviation
                }
            }
            }
        }
    }
    ''')

    return render_template("cloud_accounts.jade", cloud_accounts=json.loads(result)["data"]["allCloudAccounts"]["edges"])