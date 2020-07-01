# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, ApiManagementPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# pylint: disable=line-too-long
class ApimSubscriptionScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name')
    # sid, display_name, scope, owner_id, primary_key, secondary_key, state, allow_tracing
    def test_apim_Subscription(self, resource_group_name, apim_name):
        # Set variable for subscription operations
        subscription_id = self.create_random_name('apim_subscription-', 50)
        display_name = 'foo-bar'
        state = 'published'
        primary_key = 'd370c19509d24781a5a6d6cf15604e52'
        secondary_key = 'd370c19509d24781a5a6d6cf15604e52'
        allow_tracing = True

        self.kwargs.update({
            'apim_name': apim_name,
            'subscription_id': subscription_id,
            'display_name': display_name,
            'state': state,
            'primary_key': primary_key,
            'secondary_key': secondary_key,
            'allow_tracing': allow_tracing
        })

        # Get a count of the currently existing APIM subscriptions
        start_count = len(self.cmd('apim subscription list -n {apim_name} -g {rg}').get_output_in_json())

        # Create a subscription within the APIM instance
        self.cmd('apim subscription create -n {apim_name} -g {rg} -sid {subscription_id}', checks=[
            self.check('name', '{subscription_id}')
        ])

        self.cmd('apim subscription update -n {apim_name} -g {rg} -sid {subscription_id} --display_name {display_name} --state {state}',
                 checks=[
                     self.check('display_name', '{display_name}'),
                     self.check('state', '{state}')])

        self.cmd('apim subscription show -n {apim_name} -g {rg} -sid {subscription_id}', checks=[
            self.check('display_name', '{display_name}'),
            self.check('state', '{state}')
        ])

        self.cmd('apim subscription regenerate-primary-key -n {apim_name} -g {rg} -sid {subscription_id}', checks=[
            self.check('display_name', '{display_name}'),
            self.check('state', '{state}')
        ])

        self.cmd('apim subscription regenerate-secondary-key -n {apim_name} -g {rg} -sid {subscription_id}', checks=[
            self.check('display_name', '{display_name}'),
            self.check('state', '{state}')
        ])

        self.cmd('apim subscription delete -n {apim_name} -g {rg} -sid {subscription_id}')

        final_count = len(self.cmd('apim subscription list -n {apim_name} -g {rg}').get_output_in_json())
        self.assertLessEqual(final_count, start_count)
