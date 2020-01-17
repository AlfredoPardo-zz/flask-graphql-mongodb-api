from app.models import CloudProvider as CloudProviderModel
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType

class CloudProvider(MongoengineObjectType):

    class Meta:
        model = CloudProviderModel
        interfaces = (Node,)