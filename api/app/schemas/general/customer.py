from app.models import Customer as CustomerModel
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType

class Customer(MongoengineObjectType):

    class Meta:
        model = CustomerModel
        interfaces = (Node,)