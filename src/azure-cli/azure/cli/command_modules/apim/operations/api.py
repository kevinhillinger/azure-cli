# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long


from azure.mgmt.apimanagement.models import (ApiCreateOrUpdateParameter, Protocol,
                                             AuthenticationSettingsContract, OAuth2AuthenticationSettingsContract, OpenIdAuthenticationSettingsContract, BearerTokenSendingMethod,
                                             SubscriptionKeyParameterNamesContract,
                                             ApiCreateOrUpdatePropertiesWsdlSelector)


# API Operations
# pylint: disable=too-many-locals
def create_api(client, resource_group_name, service_name, api_id,
               path, display_name=None, description=None, service_url=None, protocols=None,
               api_revision=None, api_revision_description=None,
               api_version=None, api_version_set_id=None,
               source_api_id=None,
               oauth2_authorization_server_id=None, oauth2_scope=None,
               openid_provider_id=None, openid_bearer_token_sending_methods=None,
               subscription_required=None, subscription_key_header_name=None, subscription_key_query_string_name=None,
               is_current=None, is_online=None,
               import_format=None, value=None,
               wsdl_service_name=None, wsdl_endpoint_name=None, api_type=None,
               ):

    # Revsion indicator
    REVISION_INDICATOR = ";rev="

    if_match = None

    # Default the display name to the path - DO NOT DEFAULT when creating a new revision
    if display_name is None and REVISION_INDICATOR not in api_id:
        display_name = path

    # Set the authentication settings
    authentication_settings = AuthenticationSettingsContract()

    if oauth2_authorization_server_id is not None:
        o_auth2 = OAuth2AuthenticationSettingsContract(
            authorization_server_id=oauth2_authorization_server_id,
            scope=oauth2_scope
        )
        authentication_settings.o_auth2 = o_auth2

    if openid_provider_id is not None:
        openid = OpenIdAuthenticationSettingsContract(
            openid_provider_id=openid_provider_id,
            bearer_token_sending_methods=list(map(lambda x: BearerTokenSendingMethod(x), openid_bearer_token_sending_methods[0].split()))  # pylint: disable=unnecessary-lambda
        )
        authentication_settings.openid = openid

    # Set the remaining parameters
    parameters = ApiCreateOrUpdateParameter(
        path=path,
        display_name=display_name,
        description=description,
        api_revision=api_revision,
        api_revision_description=api_revision_description,
        api_version=api_version,
        api_version_set_id=api_version_set_id,
        subscription_required=subscription_required,
        source_api_id=source_api_id,
        service_url=service_url,
        authentication_settings=authentication_settings,
        api_type=api_type,
        is_current=is_current,
        is_online=is_online,
        format=import_format,
        value=value
    )

    # Default and set the protocol(s) - DO NOT DEFAULT when creating a new revision
    if protocols is None and REVISION_INDICATOR not in api_id:
        parameters.protocols = ["https"]
    if protocols is not None and len(protocols) > 0:  # pylint: disable=len-as-condition
        parameters.protocols = list(map(lambda x: Protocol(x), protocols[0].split()))  # pylint: disable=unnecessary-lambda

    # Set the subscription_key_parameter_names
    if subscription_key_header_name is not None or subscription_key_query_string_name is not None:
        parameters.subscription_key_parameter_names = SubscriptionKeyParameterNamesContract(
            header=subscription_key_header_name,
            query=subscription_key_query_string_name
        )

    # Set the wsdl_selector
    if wsdl_service_name is not None and wsdl_endpoint_name is not None:
        parameters.wsdl_selector = ApiCreateOrUpdatePropertiesWsdlSelector(
            wsdl_service_name=wsdl_service_name,
            wsdl_endpoint_name=wsdl_endpoint_name
        )

    return client.create_or_update(resource_group_name, service_name, api_id, parameters, if_match)

# pylint: disable=too-many-branches
def update_api(instance,
               path=None, display_name=None, description=None, service_url=None, protocols=None,
               api_revision=None, api_revision_description=None,
               api_version=None, api_version_set_id=None,
               source_api_id=None,
               oauth2_authorization_server_id=None, oauth2_scope=None,
               openid_provider_id=None, openid_bearer_token_sending_methods=None,
               subscription_required=None, subscription_key_header_name=None, subscription_key_query_string_name=None,
               is_current=None, is_online=None,
               import_format=None, value=None,
               wsdl_service_name=None, wsdl_endpoint_name=None, api_type=None,
               ):

    if path is not None:
        instance.path = path

    if display_name is not None:
        instance.display_name = display_name
    if description is not None:
        instance.description = description

    if service_url is not None:
        instance.service_url = service_url

    if protocols is not None and len(protocols) > 0:  # pylint: disable=len-as-condition
        instance.protocols = list(map(lambda x: Protocol(x), protocols[0].split()))  # pylint: disable=unnecessary-lambda

    if api_revision is not None:
        instance.api_revision = api_revision

    if api_revision_description is not None:
        instance.api_revision_description = api_revision_description

    if api_version is not None:
        instance.api_version = api_version

    if api_version_set_id is not None:
        instance.api_version_set_id = api_version_set_id

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
        instance.authentication_settings.openid_bearer_token_sending_methods = list(map(lambda x: BearerTokenSendingMethod(x), openid_bearer_token_sending_methods[0].split()))  # pylint: disable=unnecessary-lambda

    if subscription_required is not None:
        instance.subscription_required = subscription_required

    # Set the subscription_key_parameter_names
    if subscription_key_header_name is not None:
        instance.subscription_key_parameter_names.header = subscription_key_header_name
    if subscription_key_query_string_name is not None:
        instance.subscription_key_parameter_names.query = subscription_key_query_string_name

    if is_current is not None:
        instance.is_current = is_current

    if is_online is not None:
        instance.is_online = is_online

    if import_format is not None:
        instance.format = import_format

    if value is not None:
        instance.value = value

    # TODO:
    # Set the WSDL selector
    if wsdl_service_name is not None and wsdl_endpoint_name is not None:
        instance.wsdl_selector = ApiCreateOrUpdatePropertiesWsdlSelector(
            wsdl_service_name=wsdl_service_name,
            wsdl_endpoint_name=wsdl_endpoint_name
        )

    if api_type is not None:
        instance.api_type = api_type

    return instance


def delete_api(client, resource_group_name, service_name, api_id, delete_revisions=None):
    if_match = '*'
    return client.delete(resource_group_name, service_name, api_id, if_match, delete_revisions)


def get_api(client, resource_group_name, service_name, api_id):
    return client.get(resource_group_name, service_name, api_id)


# def get_api_etag(client, resource_group_name, service_name, api_id):
#     return client.get_entity_tag(resource_group_name, service_name, api_id)

def list_api(client, resource_group_name, service_name, tags=None, expand_api_version_set=None):
    return client.list_by_service(resource_group_name, service_name, None, None, None, tags, expand_api_version_set)