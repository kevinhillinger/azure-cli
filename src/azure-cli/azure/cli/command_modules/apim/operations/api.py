# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.util import sdk_no_wait
from azure.mgmt.apimanagement.models import (ApiContract, ApiCreateOrUpdateParameter, Protocol,
                                                AuthenticationSettingsContract, OAuth2AuthenticationSettingsContract, OpenIdAuthenticationSettingsContract, BearerTokenSendingMethod,
                                                SubscriptionKeyParameterNamesContract,
                                                ApiVersionSetContractDetails, 
                                                ApiCreateOrUpdatePropertiesWsdlSelector)

# API Operations
def create_api(client, resource_group_name, service_name, api_id, 
                path, display_name=None, description=None, service_url=None, protocols=None, 
                api_revision=None, api_revision_description=None, api_version=None, api_version_set_id=None, api_version_set=None, api_version_description=None, 
                source_api_id=None,
                oauth2_authorization_server_id=None, oauth2_scope=None,
                openid_provider_id=None, openid_bearer_token_sending_methods=None,
                subscription_required=None, subscription_key_header_name=None, subscription_key_query_string_name=None,
                wsdl_selector=None, soap_api_type=None,
            ):
    
    if_match = None

    # Set the authentication settings
    authentication_settings = AuthenticationSettingsContract()
    if oauth2_authorization_server_id is not None:
        o_auth2 = OAuth2AuthenticationSettingsContract(
            authorization_server_id = oauth2_authorization_server_id,
            scope = oauth2_scope
        )
        authentication_settings.o_auth2 = o_auth2
    if openid_provider_id is not None:
        openid = OpenIdAuthenticationSettingsContract(
            openid_provider_id = openid_provider_id,
            bearer_token_sending_methods = list(map(lambda x: BearerTokenSendingMethod(x), openid_bearer_token_sending_methods[0].split()))
        )
        authentication_settings.openid = openid
    
    # Set the remaining parameters
    parameters = ApiCreateOrUpdateParameter(
        path = path,
        display_name=display_name,
        description = description,
        api_revision = api_revision, 
        api_revision_description = api_revision_description, 
        api_version = api_version, 
        api_version_description = api_version_description, 
        api_version_set_id = api_version_set_id, 
        subscription_required = subscription_required,
        source_api_id = source_api_id,
        service_url = service_url,
        # subscription_key_parameter_names = subscription_key_parameter_names,
        authentication_settings = authentication_settings,
        api_version_set = api_version_set,
        wsdl_selector = wsdl_selector,
        api_type = soap_api_type
    )

    # Set the protocol(s)
    if protocols is not None and len(protocols) > 0:
        parameters.protocols = list(map(lambda x: Protocol(x), protocols[0].split()))

    # Set the subscription_key_parameter_names
    if subscription_key_header_name is not None or subscription_key_query_string_name is not None:
        parameters.subscription_key_parameter_names = SubscriptionKeyParameterNamesContract(
            header = subscription_key_header_name,
            query = subscription_key_query_string_name
        )

    # TODO: api_version_set
    # parameters['api_version_set'] = ApiVersionSetContractDetails()

    # TODO: wsdl_selector = wsdl_selector
    # parameters['wsdl_selector'] = ApiCreateOrUpdatePropertiesWsdlSelector()

    return client.create_or_update(resource_group_name, service_name, api_id, parameters, if_match)


def update_api(instance,  
                path=None, display_name=None, description=None, service_url=None, protocols=None,
                api_revision=None, api_revision_description=None, api_version=None, api_version_set_id=None, api_version_set=None, api_version_description=None, 
                source_api_id=None,
                oauth2_authorization_server_id=None, oauth2_scope=None,
                openid_provider_id=None, openid_bearer_token_sending_methods=None,
                subscription_required=None, subscription_key_header_name=None, subscription_key_query_string_name=None,
                wsdl_selector=None, soap_api_type=None,
                is_current=None, is_online=None
            ):

    if path is not None:
        instance.path = path

    if display_name is not None:
        instance.display_name = display_name
        
    if description is not None:
        instance.description = description

    if service_url is not None:
        instance.service_url = service_url

    if protocols is not None and len(protocols) > 0:
        instance.protocols = list(map(lambda x: Protocol(x), protocols[0].split()))

    if api_revision is not None:
        instance.api_revision = api_revision
        
    if api_revision_description is not None:
        instance.api_revision_description = api_revision_description

    if api_version is not None: 
        instance.api_version = api_version

    if api_version_set_id is not None: 
        instance.api_version_set_id

    if api_version_set is not None:
        instance.api_version_set = api_version_set

    if api_version_description is not None:
        instance.api_version_description = api_version_description

    if source_api_id is not None:
        instance.source_api_id = source_api_id

    # Set the authentication settings
    if oauth2_authorization_server_id is not None:
        instance.authentication_settings.oauth2_authorization_server_id = oauth2_authorization_server_id
    if oauth2_scope is not None:
        instance.authentication_settings.oauth2_scope = oauth2_scope
    if openid_provider_id is not None:
        instance.authentication_settings.openid_provider_id = openid_provider_id
    if openid_bearer_token_sending_methods is not None:
        instance.authentication_settings.openid_bearer_token_sending_methods = list(map(lambda x: BearerTokenSendingMethod(x), openid_bearer_token_sending_methods[0].split()))

    if subscription_required is not None:
        instance.subscription_required = subscription_required

    # Set the subscription_key_parameter_names
    if subscription_key_header_name is not None:
        instance.subscription_key_parameter_names.header = subscription_key_header_name
    if subscription_key_query_string_name is not None:
        instance.subscription_key_parameter_names.query = subscription_key_query_string_name

    if wsdl_selector is not None:
        instance.wsdl_selector = wsdl_selector

    if soap_api_type is not None:
        instance.soap_api_type = soap_api_type

    if is_current is not None: 
        instance.is_current = is_current

    if is_online is not None:
        instance.is_online = is_online

    return instance


def delete_api(client, resource_group_name, service_name, api_id, delete_revisions=None):
    if_match = '*'
    return client.delete(resource_group_name, service_name, api_id, if_match, delete_revisions)


def get_api(client, resource_group_name, service_name, api_id):
    return client.get(resource_group_name, service_name, api_id)


def get_api_etag(client, resource_group_name, service_name, api_id):
    return client.get_entity_tag(resource_group_name, service_name, api_id)


def list_api(client, resource_group_name, service_name, filter=None, top=None, skip=None, tags=None, expand_api_version_set=None):
    return client.list_by_service(resource_group_name, service_name, filter, top, skip, tags, expand_api_version_set)

