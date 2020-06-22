# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.util import sdk_no_wait
from azure.mgmt.apimanagement.models import (PolicyContract)


# Service Operations

def list_policy(client, resource_group_name, service_name):
    return client.list_by_service(resource_group_name, service_name)


def get_policy(client, resource_group_name, service_name):
    """Show details of an APIM policy """
    return client.get(resource_group_name, service_name)


def create_policy():
    return None


def update_policy():
    return None


def delete_policy():
    return None


def get_policy_etag():
    """Show etag of an APIM policy """
    return client.get_entity_tag(resource_group_name, service_name)

