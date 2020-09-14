# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.apim._client_factory import cf_api_version_set


def load_command_table(commands_loader, _):
    sdk = CliCommandType(
        operations_tmpl='azure.mgmt.apimanagement.operations#ApiVersionSetOperations.{}',
        client_factory=cf_api_version_set
    )

    custom_type = CliCommandType(
        operations_tmpl='azure.cli.command_modules.apim.operations.api_versionset.custom#{}',
        client_factory=cf_api_version_set
    )

    with commands_loader.command_group('apim api versionset', sdk, custom_command_type=custom_type, is_preview=True) as g:
        g.custom_command('list', 'list_api_vs')
        g.custom_show_command('show', 'show_api_vs')
        g.custom_command('create', 'create_api_vs')
        g.generic_update_command('update', custom_func_name='update_api_apivs')
        g.custom_command('delete', 'delete_api_vs')
