# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.apim._client_factory import cf_named_value


def load_command_table(commands_loader, _):
    sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimanagement.operations#NamedValueOperations.{}',
        client_factory=cf_named_value
    )

    custom_type = CliCommandType(
        operations_tmpl='azure.cli.command_modules.apim.operations.named_value.custom#{}',
        client_factory=cf_named_value
    )

    # convention is to name out sub group command with dash '-' separating nouns, e.g. named-value
    with commands_loader.command_group('apim named-value', sdk, custom_command_type=custom_type, client_factory=cf_named_value, is_preview=True) as g:
        g.custom_command('create', 'create_apim_nv')
        g.custom_show_command('show', 'get_apim_nv')
        g.custom_command('list', 'list_apim_nv')
        g.custom_command('delete', 'delete_apim_nv', confirmation=True)
        g.generic_update_command('update', custom_func_name='update_apim_nv')