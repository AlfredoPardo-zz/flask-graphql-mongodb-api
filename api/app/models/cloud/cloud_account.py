from mongoengine import Document
from mongoengine.fields import (StringField, ReferenceField)

from app.models.cloud.cloud_provider import CloudProvider
from app.models.general.customer import Customer

class CloudAccount(Document):

    meta = {'collection': 'cloud_account'}
    uid = StringField() # 3xm-security
    name = StringField() # 3XM Organizations Security
    customer = ReferenceField(Customer)
    cloud_provider = ReferenceField(CloudProvider)
