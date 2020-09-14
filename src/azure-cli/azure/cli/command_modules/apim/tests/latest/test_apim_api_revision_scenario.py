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


class ApimApiRevisionScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name')
    def test_apim_api_policy(self, resource_group, apim_name):
        # setup

        # list API revision
        self.cmd('apim api revision list -g "{rg}" -n "{service_name}" --api-id "{api_id}"')

        # create API revision
        self.cmd('apim api revision create -g "{rg}" -n "{service_name}" --api-id "{api_id}"  --api-revision "{api_revision}" --api-revision-description "{api_revision_description}"')
