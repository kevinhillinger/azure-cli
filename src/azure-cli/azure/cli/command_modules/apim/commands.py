# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.apim._format import (service_output_format, product_output_format, policy_output_format, subscription_output_format)
from azure.cli.command_modules.apim._client_factory import (cf_service, cf_api, cf_policy, cf_product, cf_subscription)
from ._validators import validate_policy_xml_content



def load_command_table(self, _):

    service_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimanagement.operations#ApiManagementServiceOperations.{}',
        client_factory=cf_service
    )

    policy_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimanagement.operations#PolicyOperations.{}',
        client_factory=cf_policy
    )

    policy_custom_type = CliCommandType(
        operations_tmpl='azure.cli.command_modules.apim.operations.policy#{}',
        client_factory=cf_policy
    )

    api_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimanagement.operations#ApiOperations.{}',
        client_factory=cf_api
    )

    api_custom_type = CliCommandType(
        operations_tmpl='azure.cli.command_modules.apim.operations.api#{}',
        client_factory=cf_api
    )

    product_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimanagement.operations#ProductOperations.{}',
        client_factory=cf_product
    )

    product_custom_type = CliCommandType(
        operations_tmpl='azure.cli.command_modules.apim.operations.product#{}',
        client_factory=cf_product
    )
    
    subscription_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimanagement.operations#SubscriptionOperations.{}',
        client_factory=cf_subscription
    )

    subscription_custom_type = CliCommandType(
        operations_tmpl='azure.cli.command_modules.apim.operations.subscription#{}',
        client_factory=cf_subscription
    )

    # pylint: disable=line-too-long
    with self.command_group('apim', service_sdk, is_preview=True) as g:
        g.custom_command('create', 'create_apim', supports_no_wait=True, table_transformer=service_output_format)
        g.custom_show_command('show', 'get_apim', table_transformer=service_output_format)
        g.custom_command('list', 'list_apim', table_transformer=service_output_format)
        g.command('delete', 'delete', confirmation=True, supports_no_wait=True)
        g.generic_update_command('update', custom_func_name='update_apim', getter_name='get', setter_name='create_or_update', supports_no_wait=True)
        g.custom_command('check-name', 'check_name_availability')
        g.custom_command('backup', 'apim_backup', supports_no_wait=True)
        g.custom_command('apply-network-updates', 'apim_apply_network_configuration_updates', supports_no_wait=True)

    # api apis
    with self.command_group('apim api', api_sdk, custom_command_type=api_custom_type, client_factory=cf_api, is_preview=True) as g:
        g.custom_command('create', 'create_api', supports_no_wait=True, table_transformer=None)
        g.custom_command('delete', 'delete_api', confirmation=True, supports_no_wait=True)
        g.custom_command('show-etag', 'get_api_etag')
        g.custom_show_command('show', 'get_api', table_transformer=None)
        g.custom_command('list', 'list_api', table_transformer=None)
        g.generic_update_command('update', custom_func_name='update_api', supports_no_wait=True)

    # product apis
    with self.command_group('apim product', product_sdk, is_preview=True, client_factory=cf_product) as g:
        g.custom_command('create', 'product_create', table_transformer=product_output_format)
        g.custom_command('list', 'product_list_by_service', table_transformer=product_output_format)
        g.custom_command('show', 'product_show', table_transformer=product_output_format)
        g.custom_command('delete', 'product_delete', table_transformer=product_output_format)
        g.generic_update_command('update', custom_func_name='product_update', getter_name='get', setter_name='create_or_update', supports_no_wait=True)
    
    # policy
    with self.command_group('apim policy', policy_sdk, custom_command_type=policy_custom_type, client_factory=cf_policy, is_preview=True) as g:
        g.custom_command('create', 'create_policy', supports_no_wait=True, table_transformer=policy_output_format, validator=validate_policy_xml_content)
        g.custom_show_command('show', 'get_policy', table_transformer=policy_output_format)
        g.custom_command('delete', 'delete_policy', confirmation=True, supports_no_wait=True)
        g.custom_command('update', 'update_policy', table_transformer=policy_output_format, validator=validate_policy_xml_content)

    # subscription apis
    with self.command_group('apim subscription', subscription_sdk, custom_command_type=subscription_custom_type, is_preview=True, client_factory=cf_subscription) as g:
        g.custom_command('create', 'create_subscription', table_transformer=subscription_output_format)
        g.custom_command('list', 'list_subscription', table_transformer=subscription_output_format)
        g.custom_command('show', 'get_subscription', table_transformer=subscription_output_format)
        g.custom_command('delete', 'delete_subscription', confirmation=True, table_transformer=subscription_output_format)
        g.generic_update_command('update', custom_func_name='update_subscription', supports_no_wait=subscription_output_format )
