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
    @ApiManagementPreparer(parameter_name='apim_name')
    def test_apim_api(self, resource_group, apim_name):

        # Create a  API
        api_id = self.create_random_name('apim-api-', 50)
        path = 'api-path'
        display_name = 'api display name'
        description = 'api description'
        service_url  = 'http://echoapi.cloudapp.net/api'
        protocols = 'http https'
        subscription_key_header_name = 'header1234'
        subscription_key_query_string_name = 'query1234'

        self.kwargs.update({
            'apim_name': apim_name,
            'api_id': api_id,
            'path': path,
            'display_name': display_name,
            'description': description,
            'service_url': service_url,
            'protocols': protocols,
            'subscription_key_header_name': subscription_key_header_name,
            'subscription_key_query_string_name': subscription_key_query_string_name
        })

        source_api_id = self.cmd('apim api create -n {apim_name} -g {rg} -a {api_id} --path {path} --display-name {display_name} --description {description} --service-url {service_url} --protocols {protocols} --subscription-key-header-name {subscription_key_header_name} --subscription-key-query-string-name {subscription_key_query_string_name}', checks=[
            self.check('name', '{api_id}'),
            self.check('path', '{path}'),
            self.check('displayName', '{display_name}'),
            self.check('description', '{description}'),
            self.check('serviceUrl', '{service_url}'),
            self.check('subscriptionKeyParameterNames.header', '{subscription_key_header_name}'),
            self.check('subscriptionKeyParameterNames.query', '{subscription_key_query_string_name}')
        ]).get_output_in_json().id

        # Clone an API from the previously created API, using the --source-api-id parameter with value {source_api_id}
        self.kwargs.update({
            'api_id': api_id + '_clone',
            'path': path + '-clone',
            'display_name': display_name + ' clone',
            'description': description + ' clone'
        })

        self.cmd('apim api create -n {apim_name} -g {rg} -a {api_id} --path {path} --display-name {display_name} --description {description} --service-url {service_url} --protocols {protocols} --source-api-id {source_api_id}', checks=[
            self.check('name', '{api_id}'),
            self.check('path', '{path}'),
            self.check('displayName', '{display_name}'),
            self.check('description', '{description}'),
            self.check('serviceUrl', '{service_url}'),
            self.check('subscriptionKeyParameterNames.header', '{subscription_key_header_name}'),
            self.check('subscriptionKeyParameterNames.query', '{subscription_key_query_string_name}')
        ])

        # Create a new revision from an existing API, using the --source-api-id parameter with value {source_api_id}
        # api_id_revision = api_id + ';rev=2'
        # api_revision_description = description + ' revision'
        # service_url_revision = service_url + '2'

        # self.kwargs.update({
        #     'api_id': api_id_revision,
        #     'path': path,
        #     'api_revision_description': api_revision_description,
        #     'service_url': service_url_revision
        # })

        # self.cmd('apim api create -n {apim_name} -g {rg} -a {api_id} --path {path} --api-revision-description {description} --service-url {service_url} --source-api-id {source_api_id}', checks=[
        #     self.check('name', '{api_id}'),
        #     self.check('path', '{path}'),
        #     self.check('apiRevisionDescription', '{description}'),
        #     self.check('serviceUrl', '{service_url}'),
        #     self.check('subscriptionKeyParameterNames.header', '{subscription_key_header_name}'),
        #     self.check('subscriptionKeyParameterNames.query', '{subscription_key_query_string_name}')
        # ])

        # Import an API from Swagger, overwriting the service URL
        # api_id_swagger = api_id + '_swagger'
        # path_swagger = path + '_swagger'
        # display_name_swagger = 'Swagger Sample App'
        # format_swagger = 'swagger-link-json'
        # value_swagger = 'http://apimpimportviaurl.azurewebsites.net/api/apidocs/'
        # service_url_swagger = 'http://petstore.swagger.wordnik.com/api'
        # self.cmd('apim api create -n {apim_name} -g {rg} -a {api_id_swagger} --path {path_swagger} --format {format_swagger} --value {value_swagger} --service-url {service_url_swagger}', checks=[
        #     self.check('name', '{api_id_swagger}'),
        #     self.check('path', '{path_swagger}'),
        #     self.check('displayName', '{display_name_swagger}'),
        #     self.check('serviceUrl', '{service_url_swagger}')
        # ])

        # # Update an API
        # self.cmd('apim api update -n {apim_name} -g {rg} -p {api_id} --description {description} --state {state}',
        #          checks=[
        #              self.check('description', '{description}'),
        #              self.check('state', '{state}')])

        # # Show an API
        # self.cmd('apim api show -n {apim_name} -g {rg} -p {api_id}', checks=[
        #     self.check('description', '{description}'),
        #     self.check('state', '{state}')
        # ])

        # # List APIs
        # final_count = len(self.cmd('apim api list -n {apim_name} -g {rg}').get_output_in_json())
        # self.assertLessEqual(final_count, 1)  # 0 used here since the default APIM apis were deleted

        # # Delete an API
        # self.cmd('apim api delete -n {apim_name} -g {rg} -p {api_id}')

        # # List APIs
        # final_count = len(self.cmd('apim api list -n {apim_name} -g {rg}').get_output_in_json())
        # self.assertLessEqual(final_count, 0)  # 0 used here since the default APIM apis were deleted
