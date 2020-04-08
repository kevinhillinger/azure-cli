# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, ApiManagementPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ApimProductScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name')
    def test_apim_product(self, resource_group, apim_name):
        product_id = self.create_random_name('apim_product-', 50)
        print('About to set the kwargs')
        self.kwargs.update({
            'apim_name': apim_name,
            'product_id': product_id,
            'tags': ["foo=boo"]
        })
        print('Set the kwargs')
        self.cmd('apim product create -n {apim_name} -g {rg} -p {product_id}', checks=[
            self.check('name', '{product_id}')
        ])
