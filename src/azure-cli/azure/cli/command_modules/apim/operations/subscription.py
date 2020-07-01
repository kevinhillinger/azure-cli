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


def create_subscription(cmd, resource_group_name, service_name, sid, display_name, scope, owner_id=None, primary_key=None, secondary_key=None, state=None, allow_tracing=None):

    from azure.cli.command_modules.apim._client_factory import (cf_service, cf_subscription)
    client = cf_subscription(cmd.cli_ctx)
    service_client = cf_service(cmd.cli_ctx)
    apim_instance = service_client.get(resource_group_name, service_name)
    scope = apim_instance.id + scope

    parameters = SubscriptionCreateParameters(
        display_name=display_name,
        scope=scope
    )
    if owner_id is not None:
        owner_id = apim_instance.id + "/users/" + owner_id
        parameters.owner_id = owner_id

    if primary_key is not None:
        parameters.primary_key = primary_key

    if secondary_key is not None:
        parameters.secondary_key = secondary_key

    if state is not None:
        parameters.state = state

    if allow_tracing is not None:
        parameters.allow_tracing = allow_tracing

    return client.create_or_update(resource_group_name, service_name, sid, parameters)


def update_subscription(cmd, resource_group_name, service_name, sid, display_name, scope, owner_id=None, primary_key=None, secondary_key=None, state=None, allow_tracing=None):
    return create_subscription(cmd, resource_group_name, service_name, sid, display_name, scope, owner_id, primary_key, secondary_key, state, allow_tracing)


def delete_subscription(client, resource_group_name, service_name, sid):
    return client.delete(resource_group_name, service_name, sid, if_match='*')


def regenerate_primary_key(client, resource_group_name, service_name, sid):
    return client.regenerate_primary_key(resource_group_name, service_name, sid, if_match='*')


def regenerate_secondary_key(client, resource_group_name, service_name, sid):
    return client.regenerate_secondary_key(resource_group_name, service_name, sid, if_match='*')
