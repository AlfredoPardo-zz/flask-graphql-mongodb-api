from mongoengine import connect
from app.models import CloudAccount, CloudProvider, Customer

connect(db='fgm_db_dev',
    username='fgm',
    password='fl4sKGr4phQLM0ngO#',
    host='fgm_db',
    authentication_source='admin',
    port=27017)

def init_db():

    # Adding Cloud Providers
    cloud_provider_1 = CloudProvider(uid="aws", abbreviation="AWS", name="Amazon Web Services")
    cloud_provider_1.save()

    cloud_provider_2 = CloudProvider(uid="azure", abbreviation="Azure", name="Azure")
    cloud_provider_2.save()

    cloud_provider_3 = CloudProvider(uid="gcp", abbreviation="GCP", name="Google Cloud")
    cloud_provider_3.save()

    # Adding Customers
    customer_1 = Customer(uid="netflix", name="Netflix")
    customer_1.save()

    customer_2 = Customer(uid="apv", name="Amazon Prime Video")
    customer_2.save()

    # Adding Cloud Accounts
    cloud_account = CloudAccount(uid="netflix-dev",
    name="Netflix Dev",
    customer=customer_1,
    cloud_provider=cloud_provider_1)
    cloud_account.save()

if __name__ == "__main__":
    init_db()