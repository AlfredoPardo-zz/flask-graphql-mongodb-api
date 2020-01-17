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

"""
class Department(MongoengineObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (Node,)


class Role(MongoengineObjectType):

    class Meta:
        model = RoleModel
        interfaces = (Node,)


class Task(MongoengineObjectType):

    class Meta:
        model = TaskModel
        interfaces = (Node,)
"""

# class Employee(MongoengineObjectType):

#     class Meta:
#         model = EmployeeModel
#         interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()
    #all_employees = MongoengineConnectionField(Employee)
    #all_roles = MongoengineConnectionField(Role)
    """ Added by me """
    #all_tasks = MongoengineConnectionField(Task)
    #all_departments = MongoengineConnectionField(Department)
    all_cloud_accounts = MongoengineConnectionField(CloudAccountSchema)
    all_cloud_providers = MongoengineConnectionField(CloudProviderSchema)
    all_customers = MongoengineConnectionField(CustomerSchema)
    """ End of Added by me """
    #role = graphene.Field(Role)

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
    


# schema = graphene.Schema(query=Query, types=[Department, Employee, Role], mutation=Mutation)
schema = graphene.Schema(query=Query, types=[CloudAccountSchema, \
  CloudProviderSchema, CustomerSchema], mutation=Mutation)

"""
{
  allRoles {
    edges {
      node {
        id
        name
      }
    }
  }
}
"""

"""

**************************

mutation updateRole {
 updateRole( uid:"manager", name: "Managerrrr") {
    role {
      name
    }
    }
}

******************************

mutation addRole {
 addRole( uid:"manager3", name: "Manager 3") {
    role {
      name
    }
}
}


mutation deleteRole {
 deleteRole( uid:"manager") {
    role {
      name
    }
    }
}
"""