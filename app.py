# sample from https://github.com/Azure-Samples/resource-manager-python-manage-resources-with-msi

from msrestazure.azure_active_directory import MSIAuthentication
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient

# Manage resources and resource groups - create, update and delete a resource group,
# deploy a solution into a resource group, export an ARM template. Create, read, update
# and delete a resource


def run_example():
    """MSI Authentication example."""

    #
    # Create System Assigned MSI Authentication
    #
    credentials = MSIAuthentication()

    #
    # Create a Subscription client, and get the subscription ID attached to that credentials.
    # This assumes there is only ONE subscription attached to this MSI token (most likely scenario)
    #
    subscription_client = SubscriptionClient(credentials)
    subscription = next(subscription_client.subscriptions.list())
    subscription_id = subscription.subscription_id

    #
    # Create a Resource Management client
    #

    resource_client = ResourceManagementClient(credentials, subscription_id)

    #
    # List resource groups as an example. The only limit is what role and policy
    # are assigned to this MSI token.
    #

    for resource_group in resource_client.resource_groups.list():
        print(resource_group.name)


if __name__ == "__main__":
    run_example()
le()