from app.models.cloud.cloud_provider import CloudProvider as CloudProviderModel
from app.schemas.cloud.cloud_provider import CloudProvider as CloudProviderSchema
import graphene

class CloudProviderMutation(graphene.Mutation):
    
    class Arguments:
        # The input arguments for this mutation
        uid = graphene.String(required=True)
        name = graphene.String()
        abbreviation = graphene.String()

    # The class attributes define the response of the mutation
    cloud_provider = graphene.Field(CloudProviderSchema)

    def mutate(self, info, uid, name=None, abbreviation=None):
        
        if info.field_name == "addCloudProvider":
            cloud_provider = CloudProviderModel(uid=uid,
            name=name, abbreviation=abbreviation)
            cloud_provider.save()
        
        if info.field_name == "deleteCloudProvider":
            cloud_provider = CloudProviderModel.objects(uid=uid).first()
            cloud_provider.delete()

        if info.field_name == "updateCloudProvider":
            cloud_provider = CloudProviderModel.objects(uid=uid).first()
            cloud_provider.name = name
            cloud_provider.abbreviation = abbreviation
            cloud_provider.save()
              
        # We return an instance of this mutation
        return CloudProviderMutation(cloud_provider=cloud_provider)