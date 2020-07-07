# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, ApiManagementPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# pylint: disable=line-too-long
class ApimSubscriptionScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name')
    
    def test_apim_Subscription(self, resource_group, apim_name):
        # Set variable for subscription operations 
      
        subscription_id = self.create_random_name('apim_subscription-', 50)
        display_name = 'foo-bar'
        updated_display_name = 'bar-foo'
        state = 'Submitted'
        primary_key = 'd370c19509d24781a5a6d6cf15604e52'
        secondary_key = 'd370c19509d24781a5a6d6cf15604e52'
        allow_tracing = True
        scope = "/apis"

        self.kwargs.update({
            'apim_name': apim_name,
            'subscription_id': subscription_id,
            'display_name': display_name,
            'state': state,
            'primary_key': primary_key,
            'secondary_key': secondary_key,
            'allow_tracing': allow_tracing,
            'scope': scope,
            'updated_display_name': updated_display_name
        })

        # Get a count of the currently existing APIM subscriptions
        start_count = len(self.cmd('apim subscription list -n {apim_name} -g {rg}').get_output_in_json())

        # Create a subscription within the APIM instance
        self.cmd('apim subscription create -n {apim_name} -g {rg} --sid {subscription_id} --scope {scope} -d {display_name}', checks=[
            self.check('name', '{subscription_id}')
        ])

        original_sub = self.cmd('apim subscription show -n {apim_name} -g {rg} --sid {subscription_id}').get_output_in_json()
        self.cmd('apim subscription update -n {apim_name} -g {rg} --sid {subscription_id} -d {updated_display_name}')
        
        modified_sub = self.cmd('apim subscription show -n {apim_name} -g {rg} --sid {subscription_id}').get_output_in_json()
        assert original_sub['displayName'] != modified_sub['displayName']
        
        original_keys = self.cmd('apim subscription keys list -n {apim_name} -g {rg} --sid {subscription_id}').get_output_in_json()
        self.cmd('apim subscription keys regenerate --key-kind primary -n {apim_name} -g {rg} --sid {subscription_id}')
        self.cmd('apim subscription keys regenerate --key-kind secondary -n {apim_name} -g {rg} --sid {subscription_id}')

        modified_keys = self.cmd('apim subscription key list -n {apim_name} -g {rg} --sid {subscription_id}').get_output_in_json()
      
        assert original_keys['primaryKey'] != modified_keys['primaryKey']
        assert original_keys['secondaryKey'] != modified_keys['secondaryKey']

        self.cmd('apim subscription delete -n {apim_name} -g {rg} --sid {subscription_id} --yes')
      
        final_count = len(self.cmd('apim subscription list -n {apim_name} -g {rg}').get_output_in_json())
        self.assertLessEqual(final_count, start_count)
