from app.models import CloudAccount as CloudAccountModel
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType

class CloudAccount(MongoengineObjectType):

    class Meta:
        model = CloudAccountModel
        interfaces = (Node,)