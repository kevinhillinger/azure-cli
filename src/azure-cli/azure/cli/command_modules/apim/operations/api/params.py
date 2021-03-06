# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type, get_three_state_flag)
from azure.mgmt.apimanagement.models import (Protocol, ApiType, ContentFormat)

PROTOCOL_TYPES = Protocol
API_TYPES = ApiType
CONTENT_FORMATS = ContentFormat


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('apim api') as c:
        c.argument('api_id', options_list=['--api-id', '-a'], help='API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.')
        c.argument('path', options_list=['--path', '-p'], help='Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.')
        c.argument('description', options_list=['--description', '-d'], help='Description of the API. May include HTML formatting tags.')
        c.argument('subscription_required', options_list=['--subscription-required'], arg_type=get_three_state_flag(), help='Indicate whether an API or Product subscription is required for accessing the API. If parameter is omitted when creating a new API its value is assumed to be true.')
        c.argument('is_current', arg_type=get_three_state_flag(), help='Indicate if an API revision is the current api revision. New revisions cannot be set as current.')
        c.argument('is_online', arg_type=get_three_state_flag(), help='Indicate if an API revision is accessible via the gateway.')
        c.argument('protocols', nargs='+', arg_type=get_enum_type(PROTOCOL_TYPES), help='Describe on which protocols the operations in this API can be invoked. Default: "https"')
        c.argument('openid_bearer_token_sending_methods', options_list=['--openid-token-methods'], nargs='+', help='Indicate how to send the bearer token to the backend server.')
        c.argument('api_type', arg_type=get_enum_type(ApiType), help='Type of API to create.')
        c.argument('import_format', arg_type=get_enum_type(CONTENT_FORMATS), help='Format of the Content in which the API is getting imported.')
        c.argument('delete_revisions', arg_type=get_three_state_flag(), help='Delete all revisions of the API.')
        c.argument('expand_api_version_set', options_list=['--expand-version-set'], arg_type=get_three_state_flag(), help='Include full ApiVersionSet resource in response.')
        c.argument('api_revision_description', options_list=['--revision-description'], help='Description of the Api Revision.')
        c.argument('querystring_name', help='Subscription key query string parameter name.')
        c.argument('header_name', help='Subscription key header name.')
        c.argument('oauth2_server_id', help='OAuth authorization server identifier.')
        c.argument('oauth2_scope', help='OAuth operations scope.')
