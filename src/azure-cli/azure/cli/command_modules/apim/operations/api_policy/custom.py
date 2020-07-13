# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.util import sdk_no_wait
from azure.mgmt.apimanagement.models import PolicyContentFormat
from azure.cli.command_modules.apim._util import (get_xml_content)


def create_api_policy(client, resource_group_name, service_name, api_id, xml=None, xml_path=None, xml_uri=None, no_wait=False):
    return _create_update_api(client, no_wait, resource_group_name, service_name, api_id, xml, xml_path, xml_uri, is_update=False)


def update_api_policy(client, resource_group_name, service_name, api_id, xml=None, xml_path=None, xml_uri=None, no_wait=False):
    return _create_update_api(client, no_wait, resource_group_name, service_name, api_id, xml, xml_path, xml_uri, is_update=True)


def _create_update_api(client, no_wait, resource_group_name, service_name, api_id, xml=None, xml_path=None, xml_uri=None, is_update=False):
    if_match = None if not is_update else client.get_entity_tag(resource_group_name, service_name, api_id)

    xml_format = _get_xml_format(xml, xml_path, xml_uri)
    xml_content = get_xml_content(xml, xml_path, xml_uri)

    return sdk_no_wait(no_wait, client.create_or_update,
                       resource_group_name=resource_group_name,
                       service_name=service_name,
                       api_id=api_id,
                       value=xml_content, if_match=if_match,
                       format=xml_format)


def list_api_policy(client, resource_group_name, service_name, api_id):
    return client.list_by_api(resource_group_name, service_name, api_id)


def show_api_policy(client, resource_group_name, service_name, api_id):
    return client.get(resource_group_name, service_name, api_id)


def delete_api_policy(client, resource_group_name, service_name, api_id):
    return client.delete(resource_group_name, service_name, api_id, if_match='*')


def _get_xml_format(xml, xml_path, xml_uri):
    if xml or xml_path:
        return PolicyContentFormat.xml
    if xml_uri:
        return PolicyContentFormat.xml_link
    return PolicyContentFormat.xml