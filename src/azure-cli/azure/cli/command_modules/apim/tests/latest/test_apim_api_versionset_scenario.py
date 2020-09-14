# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
import unittest
import xmltodict
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, ApiManagementPreparer)


class ApimApiVersionSetScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name')
    def test_apim_api_policy(self, resource_group, apim_name):
        # setup

        # list API version set
        initial_vs_count = len(self.cmd('apim api versionset list -g "{rg}" -n "{service_name}"').get_output_in_json())

        # create API version set
        self.cmd('apim api versionset create -g "{rg}" -n "{service_name}" --display-name "{versionset_name}" --version-set-id "{vs_id}" --versioning-scheme "{version_schema}" --description "{vs_description}" --version-query-name "{version_query_name}"', checks=[
            self.check('displayName', '{versionset_name}'),
            self.check('description', '{vs_description}'),
            self.check('versioningScheme', '{version_schema}'),
            self.check('name', '{vs_id}')
        ])

        # show API version set
        self.cmd('apim api versionset show -g "{rg}" -n "{service_name}" --version-set-id "{vs_id}"')

        # update API version set
        self.cmd('apim api versionset update -g "{rg}" -n "{service_name}" --version-set-id "{vs_id}" --display-name "{new_vs_name}"', checks=[
            self.check('displayName', '{new_vs_name}')
        ])

        # delete API version set
        self.cmd('apim api versionset delete -g "{rg}" -n "{service_name}" --version-set-id "{vs_id}"')
        final_vs_count = len(self.cmd('apim api versionset list -g "{rg}" -n "{service_name}"').get_output_in_json())
        self.assertEqual(final_vs_count, initial_vs_count)
