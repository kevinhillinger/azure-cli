# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

# from azure.mgmt.apimanagement.models import SubscriptionContentFormat

def list_subscription(client, resource_group_name, service_name):
    return client.list(resource_group_name, service_name)


def get_subscription(client, resource_group_name, service_name, sid):
    return client.get(resource_group_name, service_name, sid)


def create_subscription(client, resource_group_name, service_name, sid):
    return client.create(resource_group_name, service_name, sid)


def update_subscription(client, resource_group_name, service_name):
    return None


def delete_subscription(client, resource_group_name, service_name, sid):
    return client.delete(resource_group_name, service_name, sid, if_match='*')

