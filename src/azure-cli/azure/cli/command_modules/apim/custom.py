# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.util import sdk_no_wait
from azure.mgmt.apimanagement.models import (ApiManagementServiceResource, ApiManagementServiceIdentity,
                                             ApiManagementServiceSkuProperties, ApiManagementServiceBackupRestoreParameters,
                                             VirtualNetworkType, SkuType, ProductContract)


def create_apim(client, resource_group_name, name, publisher_email, sku_name=SkuType.developer.value,
                sku_capacity=1, virtual_network_type=VirtualNetworkType.none.value, enable_managed_identity=False,
                enable_client_certificate=None, publisher_name=None, location=None, tags=None, no_wait=False):

    resource = ApiManagementServiceResource(
        location=location,
        notification_sender_email=publisher_email,
        publisher_email=publisher_email,
        publisher_name=publisher_name,
        sku=ApiManagementServiceSkuProperties(name=sku_name, capacity=sku_capacity),
        enable_client_certificate=enable_client_certificate,
        virtual_network_type=VirtualNetworkType(virtual_network_type),
        tags=tags
    )

    if enable_managed_identity:
        resource['identity'] = ApiManagementServiceIdentity(type="SystemAssigned")

    if resource.sku.name == SkuType.consumption.value:
        resource.sku.capacity = None

    cms = client.api_management_service

    return sdk_no_wait(no_wait, cms.create_or_update,
                       resource_group_name=resource_group_name,
                       service_name=name, parameters=resource)


def update_apim(instance, publisher_email=None, sku_name=None, sku_capacity=None,
                virtual_network_type=None, publisher_name=None, enable_managed_identity=None,
                enable_client_certificate=None, tags=None):

    if publisher_email is not None:
        instance.publisher_email = publisher_email

    if sku_name is not None:
        instance.sku.name = sku_name

    if sku_capacity is not None:
        instance.sku.capacity = sku_capacity

    if virtual_network_type is not None:
        instance.virtual_network_type = virtual_network_type

    if publisher_email is not None:
        instance.publisher_email = publisher_email

    if publisher_name is not None:
        instance.publisher_name = publisher_name

    if not enable_managed_identity:
        instance.identity = None
    else:
        if instance.identity is None:
            instance.identity = ApiManagementServiceIdentity(type="SystemAssigned")

    if enable_client_certificate is not None:
        instance.enable_client_certificate = enable_client_certificate

    if tags is not None:
        instance.tags = tags

    return instance


def list_apim(client, resource_group_name=None):
    """List all APIM instances.  Resource group is optional """
    if resource_group_name:
        return client.api_management_service.list_by_resource_group(resource_group_name)
    return client.api_management_service.list()


def get_apim(client, resource_group_name, name):
    """Show details of an APIM instance """
    return client.api_management_service.get(resource_group_name, name)


def check_name_availability(client, name):
    """checks to see if a service name is available to use """
    return client.api_management_service.check_name_availability(name)


def apim_backup(client, resource_group_name, name, backup_name, storage_account_name,
                storage_account_container, storage_account_key):
    """back up an API Management service to the configured storage account """
    parameters = ApiManagementServiceBackupRestoreParameters(
        storage_account=storage_account_name,
        access_key=storage_account_key,
        container_name=storage_account_container,
        backup_name=backup_name)

    return client.api_management_service.backup(resource_group_name, name, parameters)


def apim_apply_network_configuration_updates(client, resource_group_name, name, location=None):
    """back up an API Management service to the configured storage account """
    properties = {}
    if location is not None:
        properties['location'] = location

    return client.api_management_service.apply_network_configuration_updates(resource_group_name, name, properties)


# Product Commands
def product_list_by_service(client, resource_group_name, service_name):
    """Lists a collection of products in the specified service instance. """

    return client.list_by_service(resource_group_name, service_name)


def product_show(client, resource_group_name, service_name, product_id):
    """Gets the details of the product specified by its identifier. """

    return client.get(resource_group_name, service_name, product_id)


def product_delete(client, resource_group_name, service_name, product_id):
    """Delete product. """
    delete_subscriptions = 'True'
    # Request Header If-Match
    if_match = '*'
    return client.delete(resource_group_name, service_name, product_id, delete_subscriptions, if_match)


def product_create(client, resource_group_name, service_name, product_id, description=None, terms=None,
                   subscription_required=None, approval_required=None, subscriptions_limit=None, state=None):
    """Creates a product. """
    # Request Header If-Match
    if_match = '*'

    resource = ProductContract(
        display_name=product_id
    )
    if description is not None:
        resource.description = description

    if terms is not None:
        resource.terms = terms

    if subscription_required is not None:
        resource.subscription_required = subscription_required

    if approval_required is not None:
        resource.approval_required = approval_required

    if subscriptions_limit is not None:
        resource.subscriptions_limit = subscriptions_limit

    if state is not None:
        resource.state = state

    return client.create_or_update(resource_group_name, service_name, product_id, resource, if_match)


def product_update(instance, description=None, terms=None, subscription_required=None, approval_required=None,
                   subscriptions_limit=None, state=None):
    """Update existing product details. """
    # Request Header If-Match
#    if_match = '*'

    if description is not None:
        instance.description = description

    if terms is not None:
        instance.terms = terms

    if subscription_required is not None:
        instance.subscription_required = subscription_required

    if approval_required is not None:
        instance.approval_required = approval_required

    if subscriptions_limit is not None:
        instance.subscriptions_limit = subscriptions_limit

    if state is not None:
        instance.state = state

    return instance
