# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.mgmt.apimanagement.models import NamedValueCreateContract


def create_apim_nv(client, resource_group_name, service_name, named_value_id, display_name, value=None, tags=None, secret=False):
    """Creates a new Named Value. """
    resource = NamedValueCreateContract(
        tags=tags,
        secret=secret,
        display_name=display_name,
        value=value
    )
    return client.create_or_update(resource_group_name, service_name, named_value_id, resource)


def get_apim_nv(client, resource_group_name, service_name, named_value_id, secret=False):
    """Shows details of a Named Value. """
    if secret:
        return client.named_value.list_value(resource_group_name, service_name, named_value_id)
    return client.get(resource_group_name, service_name, named_value_id)


def list_apim_nv(client, resource_group_name, service_name):
    """List all Named Values of an API Management instance. """
    return client.list_by_service(resource_group_name, service_name)


def delete_apim_nv(client, resource_group_name, service_name, named_value_id):
    """Deletes an existing Named Value. """
    return client.delete(resource_group_name, service_name, named_value_id, if_match='*')


def update_apim_nv(instance, value=None, tags=None, secret=None):
    """Updates an existing Named Value."""
    if tags is not None:
        instance.tags = tags

    if value is not None:
        instance.value = value

    if secret is not None:
        instance.secret = secret

    return instance