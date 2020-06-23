# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.util import sdk_no_wait
from azure.mgmt.apimanagement.models import (PolicyContract, PolicyContentFormat)
from azure.cli.command_modules.apim._validators import validate_policy_xml_content
from azure.cli.command_modules.apim._util import (get_xml_content)

# Service Operations

def list_policy(client, resource_group_name, service_name):
    return client.list_by_service(resource_group_name, service_name)


def get_policy(client, resource_group_name, service_name):
    return client.get(resource_group_name, service_name)


def create_policy(client, resource_group_name, service_name, xml=None, xml_path=None, xml_uri=None):
    _create_update(client, resource_group_name, service_name, xml, xml_path, xml_uri, is_update = False)


def update_policy(client, resource_group_name, service_name, xml=None, xml_path=None, xml_uri=None):
    _create_update(client, resource_group_name, service_name, xml, xml_path, xml_uri, is_update = True)


def delete_policy(client, resource_group_name, service_name):
    return client.delete(resource_group_name, service_name, if_match = '*')


def get_policy_etag(client, resource_group_name, service_name):
    return client.get_entity_tag(resource_group_name, service_name)

def _create_update(client, resource_group_name, service_name, xml=None, xml_path=None, xml_uri=None, is_update = False):
    if_match = None if not is_update else client.get_entity_tag(resource_group_name, service_name)
    xml_format = _get_xml_format(xml, xml_path, xml_uri)
    xml_content = get_xml_content(xml, xml_path, xml_uri)

    validate_policy_xml_content(xml_content)
    client.create_or_update(resource_group_name, service_name, xml_content, if_match, xml_format)

def _get_xml_format(xml, xml_path, xml_uri):
    if xml is not None or xml_path is not None:
        return PolicyContentFormat.xml
    elif xml_uri is not None:
        return PolicyContentFormat.xml_link
    return PolicyContentFormat.xml