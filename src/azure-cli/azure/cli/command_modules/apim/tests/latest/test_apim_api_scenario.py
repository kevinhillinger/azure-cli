# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, ApiManagementPreparer, live_only)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# pylint: disable=line-too-long
class ApimApiScenarioTest(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_apim-', parameter_name_for_location='resource_group_location')
    @ApiManagementPreparer(parameter_name='apim_name', sku_name='Consumption')
    def test_apim_api(self, resource_group, apim_name):

        # Counter of APIs created - used in delete and list commands
        created_apis = 0

        # Create an API
        api_id = 'api-id'
        path = 'api-path'
        display_name = 'api display name'
        description = 'api description'
        service_url = 'http://echoapi.cloudapp.net/api'

        self.kwargs.update({
            'apim_name': apim_name,
            'api_id': api_id,
            'path': path,
            'display_name': display_name,
            'description': description,
            'service_url': service_url,
            'protocols': 'http',
            'subscription_key_header_name': 'header1234',
            'subscription_key_query_string_name': 'query1234'
        })

        source_api_id = self.cmd(
            """apim api create -n {apim_name} -g {rg} -a {api_id} \
                    --path {path} \
                    --display-name "{display_name}" \
                    --description "{description}" \
                    --service-url {service_url} \
                    --protocols {protocols} \
                    --subscription-key-header-name {subscription_key_header_name} \
                    --subscription-key-query-string-name {subscription_key_query_string_name}""", checks=[
                self.check('name', '{api_id}'),
                self.check('path', '{path}'),
                self.check('displayName', '{display_name}'),
                self.check('description', '{description}'),
                self.check('serviceUrl', '{service_url}'),
                self.check('subscriptionKeyParameterNames.header', '{subscription_key_header_name}'),
                self.check('subscriptionKeyParameterNames.query', '{subscription_key_query_string_name}')
            ]).get_output_in_json()['id']

        assert source_api_id is not None
        created_apis += 1

        # Clone an API from the previously created API, using the --source-api-id parameter with value {source_api_id}
        self.kwargs.update({
            'api_id': api_id + '-clone',
            'path': path + '-clone',
            'display_name': display_name + ' clone',
            'description': description + ' clone',
            'source_api_id': source_api_id
        })

        self.cmd('apim api create -n {apim_name} -g {rg} -a {api_id} --path {path} --display-name "{display_name}" --description "{description}" --source-api-id "{source_api_id}"', checks=[
            self.check('name', '{api_id}'),
            self.check('path', '{path}'),
            self.check('displayName', '{display_name}'),
            self.check('description', '{description}'),
            self.check('serviceUrl', '{service_url}'),
            self.check('subscriptionKeyParameterNames.header', '{subscription_key_header_name}'),
            self.check('subscriptionKeyParameterNames.query', '{subscription_key_query_string_name}')
            ])

        # Create a new revision from an existing API, using the --source-api-id parameter with value {source_api_id}
        api_id_revision2 = api_id + ';rev=2'
        api_revision_description = description + ' revision 2'
        service_url_revision = service_url + '2'

        self.kwargs.update({
            'api_id': api_id_revision2,
            'path': path,
            'api_revision_description': api_revision_description,
            'service_url': service_url_revision
        })

        self.cmd('apim api create -n {apim_name} -g {rg} -a "{api_id}" --path {path} --api-revision-description "{api_revision_description}" --service-url {service_url} --source-api-id "{source_api_id}"', checks=[
            self.check('name', '{api_id}'),
            self.check('apiRevisionDescription', '{api_revision_description}'),
            self.check('apiRevision', '2'),
            self.check('serviceUrl', '{service_url}')
        ])
        created_apis += 1

        # Import an API from Swagger, overwriting the service URL
        self.kwargs.update({
            'api_id': api_id + '-swagger',
            'path': path + '-swagger',
            'display_name': 'Swagger Sample App',
            'service_url': 'http://petstore.swagger.wordnik.com/api',
            'import_format': 'swagger-link-json',
            'value': 'http://apimpimportviaurl.azurewebsites.net/api/apidocs/'
        })

        self.cmd('apim api create -n {apim_name} -g {rg} -a {api_id} --path {path} --import-format {import_format} --value {value} --service-url {service_url}', checks=[
            self.check('name', '{api_id}'),
            self.check('path', '{path}'),
            self.check('displayName', '{display_name}'),
            self.check('serviceUrl', '{service_url}')
        ])
        created_apis += 1

        # Import an API from Open API
        self.kwargs.update({
            'api_id': api_id + '-oai3-import',
            'path': path + '-oai3-import',
            'display_name': 'Swagger Petstore',
            'import_format': 'openapi-link',
            'value': 'https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml'
        })

        self.cmd('apim api create -n {apim_name} -g {rg} -a {api_id} --path {path} --import-format {import_format} --value {value}', checks=[
            self.check('name', '{api_id}'),
            self.check('path', '{path}'),
            self.check('displayName', '{display_name}')
        ])
        created_apis += 1

        # Import an API from WSDL
        self.kwargs.update({
            'api_id': api_id + '-wsdl',
            'path': path + '-wsdl',
            'display_name': 'Calculator',
            'import_format': 'wsdl-link',
            'value': 'http://www.dneonline.com/calculator.asmx?wsdl',
            'wsdl_service_name': 'Calculator',
            'wsdl_endpoint_name': 'CalculatorSoap',
            'api_type': 'http'
        })

        self.cmd('apim api create -n {apim_name} -g {rg} -a {api_id} --path {path} --import-format {import_format} --value {value} --wsdl-service-name {wsdl_service_name} --wsdl-endpoint-name {wsdl_endpoint_name} --api-type {api_type}', checks=[
            self.check('name', '{api_id}'),
            self.check('path', '{path}'),
            self.check('displayName', '{display_name}')
        ])
        created_apis += 1

        # Update an API
        description_updated = description + ' updated'
        display_name_updated = display_name + ' updated'

        self.kwargs.update({
            'api_id': api_id,
            'path': path + '-updated',
            'display_name': display_name + ' updated',
            'description': description + ' updated',
            'subscription_key_header_name': 'updatedheader1234',
            'subscription_key_query_string_name': 'updatedquery1234'
        })

        self.cmd('apim api update -n {apim_name} -g {rg} -a {api_id} --path {path} --display-name "{display_name}" --description "{description}" --subscription-key-header-name {subscription_key_header_name} --subscription-key-query-string-name {subscription_key_query_string_name}', checks=[
            self.check('name', '{api_id}'),
            self.check('path', '{path}'),
            self.check('displayName', '{display_name}'),
            self.check('description', '{description}'),
            self.check('subscriptionKeyParameterNames.header', '{subscription_key_header_name}'),
            self.check('subscriptionKeyParameterNames.query', '{subscription_key_query_string_name}')
        ])

        # Show an API
        self.cmd('apim api show -n {apim_name} -g {rg} -a {api_id}', checks=[
            self.check('path', '{path}'),
            self.check('description', description_updated),
            self.check('displayName', display_name_updated)
        ])

        # Show API revision 2
        self.kwargs.update({
            'api_id': api_id_revision2
        })

        self.cmd('apim api show -n {apim_name} -g {rg} -a {api_id}', checks=[
            self.check('path', '{path}'),
            self.check('apiRevisionDescription', api_revision_description),
            self.check('serviceUrl', service_url_revision)
        ])

        # # List APIs
        api_count = len(self.cmd('apim api list -n {apim_name} -g {rg}').get_output_in_json())
        self.assertEqual(api_count, created_apis)

        # Delete an API, including all revisions
        self.kwargs.update({
            'api_id': api_id
        })
        
        self.cmd('apim api delete -n {apim_name} -g {rg} -a {api_id} --delete-revisions --yes')
        self.assertEqual(len(self.cmd('apim api list -n {apim_name} -g {rg}').get_output_in_json()), created_apis - 1)
