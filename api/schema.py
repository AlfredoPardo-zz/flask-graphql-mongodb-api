import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from app.models import CloudAccount as CloudAccountModel, \
  CloudProvider as CloudProviderModel, \
    Customer as CustomerModel

from app.schemas import CloudAccount as CloudAccountSchema, \
  CloudProvider as CloudProviderSchema, \
  Customer as CustomerSchema

from app.mutations import CloudAccountMutation, CloudProviderMutation, CustomerMutation

class Query(graphene.ObjectType):
    node = Node.Field()
    all_cloud_accounts = MongoengineConnectionField(CloudAccountSchema)
    all_cloud_providers = MongoengineConnectionField(CloudProviderSchema)
    all_customers = MongoengineConnectionField(CustomerSchema)

class Mutation(graphene.ObjectType):
    
    add_cloud_account = CloudAccountMutation.Field() 
    delete_cloud_account = CloudAccountMutation.Field()
    update_cloud_account = CloudAccountMutation.Field()
    
    add_cloud_provider = CloudProviderMutation.Field() 
    delete_cloud_provider = CloudProviderMutation.Field() 
    update_cloud_provider = CloudProviderMutation.Field()

    add_customer = CustomerMutation.Field() 
    delete_customer = CustomerMutation.Field() 
    update_customer = CustomerMutation.Field()

schema = graphene.Schema(query=Query, types=[CloudAccountSchema, \
  CloudProviderSchema, CustomerSchema], mutation=Mutation)
