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


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ApimPolicyScenarioTest(ScenarioTest):
    xml_content = """<policies>
        <inbound></inbound>
        <backend>
                <!-- test -->
        </backend>
        <outbound />
        <on-error />
</policies>"""

    policy_file = os.path.join(TEST_DIR, 'policy.xml').replace('\\', '\\\\')

    def setUp(self):
        self._create_xml_file()
        super(ApimPolicyScenarioTest, self).setUp()

    def tearDown(self):
        self._delete_xml_file()
        super(ApimPolicyScenarioTest, self).tearDown()

    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name')
    def test_apim_policy(self, resource_group, apim_name):
        self.kwargs.update({
            'apim_name': apim_name,
            'name': 'policy',
            'xml_value': self.xml_content,
            'xml_file': self.policy_file
        })

        self._create_policy_using_inline_xml()
        self._create_policy_using_xml_from_file()
        self._delete_policy_resets_xml_value()

    def _create_policy_using_inline_xml(self):
        cmd_statement = 'apim policy create -n {apim_name} -g {rg} -v "{xml_value}" --output tsv --query value'

        result = xmltodict.parse(self.cmd(cmd_statement).output)
        expected = xmltodict.parse(self.xml_content)

        self.assertDictEqual(expected, result)

    def _create_policy_using_xml_from_file(self):
        cmd_statement = 'apim policy create -n {apim_name} -g {rg} -f {xml_file} --output tsv --query value'

        result = xmltodict.parse(self.cmd(cmd_statement).output)
        expected = xmltodict.parse(self.xml_content)

        self.assertDictEqual(expected, result)

    def _delete_policy_resets_xml_value(self):
        """When deleting, it should reset the global policy, not get rid of it where the count would equal 0"""
        self.cmd('apim policy delete -n {apim_name} -g {rg}')
        result = len(self.cmd('az apim policy show -n {apim_name} -g {rg}').get_output_in_json())
        expected = 1

        self.assertEqual(expected, result)

    def _delete_xml_file(self):
        os.remove(self.policy_file)

    def _create_xml_file(self):
        file = open(self.policy_file, "w")
        file.write(self.xml_content)
        file.close()
