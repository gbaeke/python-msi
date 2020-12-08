# sample from https://github.com/Azure-Samples/resource-manager-python-manage-resources-with-msi

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from fastapi import FastAPI

app = FastAPI()

try:
    credentials = DefaultAzureCredential()
    subscription_client = SubscriptionClient(credentials)
    subscription = next(subscription_client.subscriptions.list())
    subscription_id = subscription.subscription_id
    resource_client = ResourceManagementClient(credentials, subscription_id)
except:
    print("error obtaining credentials")

@app.get("/")
def read_root():
    groups=[]
    try:
        for resource_group in resource_client.resource_groups.list():
            groups.append(resource_group.name)
    except:
        print("error obtaining groups")
    
    return groups
        
