# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest
import xmltodict
from azure_devtools.scenario_tests import AllowLargeResponse
from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, ApiManagementPreparer)

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# pylint: disable=line-too-long
class ApimApiPolicyScenarioTest(ScenarioTest):
    xml_content = """<policies>
        <inbound></inbound>
        <backend>
                <!-- test -->
        </backend>
        <outbound />
        <on-error />
</policies>"""

    xml_update_content = """<policies>
        <inbound>
        <base />
        <rate-limit-by-key calls="1000" renewal-period="60" counter-key="@(context.Request.IpAddress)" />
        <quota-by-key calls="1000" renewal-period="600" counter-key="@(context.Request.IpAddress)" />
    </inbound>
        <backend>
                <forward-request />
        </backend>
        <outbound />
        <on-error />
</policies>"""

    policy_file = os.path.join(TEST_DIR, 'policy.xml').replace('\\', '\\\\')

    def setUp(self):
        self._create_xml_file()
        super(ApimApiPolicyScenarioTest, self).setUp()

    def tearDown(self):
        self._delete_xml_file()
        super(ApimApiPolicyScenarioTest, self).tearDown()

    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name')
    def test_apim_api_policy(self, resource_group, apim_name):
        # Set variable for api policy operations

        self.kwargs.update({
            'apim_name': apim_name,
            'api_id': 'echo-api',
            'xml_value': self.xml_content,
            'xml_file': self.policy_file
        })

        self._create_policy_using_inline_xml()
#        self._create_policy_using_xml_from_file()
#        self._delete_policy_resets_xml_value()

    def _create_policy_using_xml_from_file(self):
        cmd_statement = 'apim api policy create -n {apim_name} -g {rg} -a {api_id} -f {xml_file} --output tsv --query value'

        print(self.policy_file)

        result = xmltodict.parse(self.cmd(cmd_statement).output)
        expected = xmltodict.parse(self.xml_content)

        self.assertDictEqual(expected, result)

        # List the policy
        self.cmd('apim api policy list -n {apim_name} -g {rg} -a {api_id}', checks=[
            self.assertEqual(xml_result, self.xml_content)
        ])


    def _create_policy_using_inline_xml(self):
        cmd_statement = 'apim api policy create -n {apim_name} -g {rg} -a {api_id} -v "{xml_value}"'
#        cmd_statement = 'apim api policy create -n {apim_name} -g {rg} -a {api_id} -v "{xml_value}" --output tsv --query value'

        result = xmltodict.parse(self.cmd(cmd_statement).output)
        expected = xmltodict.parse(self.xml_content)

        self.assertDictEqual(expected, result)

        # Show the policy
        self.cmd('apim api policy list -n {apim_name} -g {rg} -a {api_id}', checks=[
            self.assertEqual(xml_result, self.xml_content)
        ])


    def _delete_policy_resets_xml_value(self):
        # Delete the policy
        self.cmd('apim api policy delete -n {apim_name} -g {rg} -a {api_id}')

        final_count = len(self.cmd('apim api policy list -n {apim_name} -g {rg} -a {api_id}').get_output_in_json())
        self.assertLessEqual(final_count, 0)  # 0 used here since the default APIM products were deleted


    def _delete_xml_file(self):
        os.remove(self.policy_file)

    def _create_xml_file(self):
        file = open(self.policy_file, "w")
        file.write(self.xml_content)
        file.close()
