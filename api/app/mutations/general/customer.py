from app.models.general.customer import Customer as CustomerModel
from app.schemas.general.customer import Customer as CustomerSchema
import graphene

class CustomerMutation(graphene.Mutation):
    
    class Arguments:
        # The input arguments for this mutation
        uid = graphene.String(required=True)
        name = graphene.String()

    # The class attributes define the response of the mutation
    customer = graphene.Field(CustomerSchema)

    def mutate(self, info, uid, name=None):
        
        if info.field_name == "addCustomer":
            customer = CustomerModel(uid=uid,
            name=name)
            customer.save()
        
        if info.field_name == "deleteCustomer":
            customer = CustomerModel.objects(uid=uid).first()
            customer.delete()

        if info.field_name == "updateCustomer":
            customer = CustomerModel.objects(uid=uid).first()
            customer.name = name
            customer.save()
              
        # We return an instance of this mutation
        return CustomerMutation(customer=customer)