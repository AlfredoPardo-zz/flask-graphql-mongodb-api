from app.models.cloud.cloud_account import CloudAccount as CloudAccountModel
from app.schemas.cloud.cloud_account import CloudAccount as CloudAccountSchema

# Referenced Models
# ToDo: Refactor this
from app.models.cloud.cloud_provider import CloudProvider as CloudProviderModel
from app.schemas import CloudProvider as CloudProviderSchema
from app.models.general.customer import Customer as CustomerModel
from app.schemas import Customer as CustomerSchema

import graphene

# TODO: Revisar Todo
class CloudAccountMutation(graphene.Mutation):
    
    class Arguments:
        # The input arguments for this mutation
        uid = graphene.String(required=True)
        name = graphene.String()
        customer_uid = graphene.String()
        cloud_provider_uid = graphene.String()

    # The class attributes define the response of the mutation
    cloud_account = graphene.Field(CloudAccountSchema)

    def mutate(self, info, uid, name=None, customer_uid=None, cloud_provider_uid=None):
        
        if info.field_name == "addCloudAccount":

            customer = CustomerModel.objects(uid=customer_uid).first()
            cloud_provider = CloudProviderModel.objects(uid=cloud_provider_uid).first()

            cloud_account = CloudAccountModel(uid=uid,
                name=name, customer=customer, cloud_provider=cloud_provider)
            cloud_account.save()
        
        if info.field_name == "deleteCloudAccount":
            cloud_account = CloudAccountModel.objects(uid=uid).first()
            cloud_account.delete()

        if info.field_name == "updateCloudAccount":

            customer = CustomerModel.objects(uid=customer_uid).first()
            cloud_provider = CloudProviderModel.objects(uid=cloud_provider_uid).first()

            cloud_account = CloudAccountModel.objects(uid=uid).first()
            cloud_account.name = name
            cloud_account.customer = customer
            cloud_account.cloud_provider = cloud_provider
            cloud_account.save()
              
        # We return an instance of this mutation
        return CloudAccountMutation(cloud_account=cloud_account)