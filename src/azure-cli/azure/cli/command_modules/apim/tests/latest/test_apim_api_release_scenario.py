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


class ApimApiReleaseScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name')
    def test_apim_api_policy(self, resource_group, apim_name):
        # setup

        # list API release
        initial_release_count = len(self.cmd('apim api release list -g "{rg}" -n "{service_name}" --api-id "{api_id}"').get_output_in_json())

        # create API release
        self.cmd('apim api release create -g "{rg}" -n "{service_name}" --api-id "{api_id}" --release-id "{release_id}" --api-revision "{api_revision}" --notes "{release_notes}"', checks=[
            self.check('name', '{release_id}'),
            self.check('notes', '{release_notes}')
        ])

        # show API release
        self.cmd('apim api release show -g "{rg}" -n "{service_name}" --api-id "{api_id}" --release-id "{release_id}"')

        # update API release
        self.cmd('apim api release update -g "{rg}" -n "{service_name}" --api-id "{api_id}" --release-id "{release_id}" --notes "{new_release_notes}"', checks=[
            self.check('name', '{release_id}'),
            self.check('notes', '{new_release_notes}')
        ])

        # delete API release
        self.cmd('apim api release delete -g "{rg}" -n "{service_name}" --api-id "{api_id}" --release-id "{release_id}"')

        final_release_count = len(self.cmd('apim api release list -g "{rg}" -n "{service_name}" --api-id "{api_id}"').get_output_in_json())
        self.assertEqual(final_release_count, initial_release_count)
