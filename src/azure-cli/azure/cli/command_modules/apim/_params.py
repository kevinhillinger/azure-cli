# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from enum import Enum
from azure.mgmt.apimanagement.models import (SkuType, VirtualNetworkType, Protocol, ApiType, ProductState)
from azure.cli.command_modules.apim.actions import (TemplateParameter)
from azure.cli.core.commands.parameters import (get_enum_type, get_location_type, resource_group_name_type, get_three_state_flag)

SKU_TYPES = SkuType
VNET_TYPES = VirtualNetworkType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    # service
    with self.argument_context('apim') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('tags', tags_type)
        c.argument('service_name', options_list=['--name', '-n'], help="The name of the api management service instance", id_part=None)
        c.argument('name', options_list=['--name', '-n'], help="The name of the api management service instance", id_part=None)
        c.argument('location', validator=get_default_location_from_resource_group)

    with self.argument_context('apim create') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), validator=get_default_location_from_resource_group)
        c.argument('publisher_name', help='The name of your organization for use in the developer portal and e-mail notifications.', required=True)
        c.argument('publisher_email', help='The e-mail address to receive all system notifications.')
        c.argument('enable_client_certificate', arg_type=get_three_state_flag(), help='Enforces a client certificate to be presented on each request to the gateway and also enables the ability to authenticate the certificate in the policy on the gateway.')
        c.argument('virtual_network_type', get_enum_type(VNET_TYPES), options_list=['--virtual-network', '-v'], help='The virtual network type.')
        c.argument('sku_name', arg_type=get_enum_type(SKU_TYPES), help='The sku of the api management instance')
        c.argument('sku_capacity', type=int, help='The number of deployed units of the SKU.')
        c.argument('enable_managed_identity', arg_type=get_three_state_flag(), help='Create a managed identity for the API Management service to access other Azure resources.')

    with self.argument_context('apim update') as c:
        c.argument('publisher_name', help='The name of your organization for use in the developer portal and e-mail notifications.')
        c.argument('publisher_email', help='The e-mail address to receive all system notifications.')
        c.argument('enable_client_certificate', arg_type=get_three_state_flag(), help='Enforces a client certificate to be presented on each request to the gateway and also enables the ability to authenticate the certificate in the policy on the gateway.')
        c.argument('virtual_network_type', get_enum_type(VNET_TYPES), options_list=['--virtual-network', '-v'], help='The virtual network type.')
        c.argument('sku_name', arg_type=get_enum_type(SKU_TYPES), help='The sku of the api management instance')
        c.argument('sku_capacity', type=int, help='The number of deployed units of the SKU.')
        c.argument('enable_managed_identity', arg_type=get_three_state_flag(), help='Create a managed identity for the API Management service to access other Azure resources.')

    with self.argument_context('apim backup') as c:
        c.argument('backup_name', help='The name of the backup file to create.')
        c.argument('storage_account_name', arg_group='Storage', help='The name of the storage account used to place the backup.')
        c.argument('storage_account_key', arg_group='Storage', help='The access key of the storage account used to place the backup.')
        c.argument('storage_account_container', arg_group='Storage', help='The name of the storage account container used to place the backup.')

    with self.argument_context('apim product api list') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the api management service instance", id_part=None)
        c.argument('product_id', help="Product identifier. Must be unique in the current API Management service instance.")

    with self.argument_context('apim product api check') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the api management service instance", id_part=None)
        c.argument('product_id', help="Product identifier. Must be unique in the current API Management service instance.")
        c.argument('api_id', arg_group='API', help='API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.')

    with self.argument_context('apim product api add') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the api management service instance", id_part=None)
        c.argument('product_id', help="Product identifier. Must be unique in the current API Management service instance.")
        c.argument('api_id', arg_group='API', help='API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.')

    with self.argument_context('apim product api delete') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the api management service instance", id_part=None)
        c.argument('product_id', help="Product identifier. Must be unique in the current API Management service instance.")
        c.argument('api_id', arg_group='API', help='API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.')

    with self.argument_context('apim product') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the api management service instance", id_part=None)
        c.argument('product_id', help="Product identifier. Must be unique in the current API Management service instance.")
        c.argument('product_name', help="Product name.")
        c.argument('description', help="Product description. May include HTML formatting tags.")
        c.argument('legal_terms', help="Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.")
        c.argument('subscription_required', options_list=['--subscription-required', '-s'], help="Whether a product subscription is required for accessing APIs included in this product.")
        c.argument('approval_required', help="whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.")
        c.argument('subscriptions_limit', help="Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.")
        c.argument('state', arg_type=get_enum_type(ProductState), help="whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished. Possible values include: 'notPublished', 'published'")
        c.argument('delete_subscriptions', help="Delete existing subscriptions associated with the product or not.")
        c.argument('if_match', help='ETag of the Entity.')

    with self.argument_context('apim nv') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help='The name of the API Management service instance.')
        c.argument('named_value_id', help='Identifier of the NamedValue.')
        c.argument('display_name', help='Required. Unique name of NamedValue. It may contain only letters, digits, period, dash, and underscore characters.')
        c.argument('value', help='Required. Value of the NamedValue. Can contain policy expressions. It may not be empty or consist only of whitespace. This property will not be filled on GET operations! Use /listSecrets POST request to get the value.')
        c.argument('secret', arg_type=get_three_state_flag(), help='Determines whether the value is a secret and should be encrypted or not. Default value is false.')
        c.argument('tags', tags_type)

    with self.argument_context('apim api operation') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the API Management service instance.")
        c.argument('api_id', help='API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.')
        c.argument('operation_id', help='Operation identifier within an API. Must be unique in the current API Management service instance.')
        c.argument('description', help="Description of the operation. May include HTML formatting tags.")
        c.argument('template_parameters', options_list=['--template-parameters', '--params', '-p'], action=TemplateParameter, nargs='+', help="Collection of URL template parameters.")
        c.argument('method', help="Required. A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.")
        c.argument('display_name', help="Required. Operation Name.")
        c.argument('if_match', help='ETag of the Entity.')
        c.argument('url_template', help='Relative URL template identifying the target resource for this operation. May include parameters.')

    with self.argument_context('apim api release') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the API Management service instance.")
        c.argument('api_id', help='API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.')
        c.argument('release_id', help="Release identifier within an API. Must be unique in the current API Management service instance.")
        c.argument('api_revision', help="API revision number.")
        c.argument('notes', help="Release Notes.")
        c.argument('if_match', help='ETag of the Entity.')

    with self.argument_context('apim api revision') as c:
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the API Management service instance.")
        c.argument('api_id', help='API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.')
        c.argument('api_revision', help='Describes the Revision of the Api.')
        c.argument('api_revision_description', options_list=['--api-revision-description', '--rev-description'], help='Description of the Api Revision.')

    with self.argument_context('apim api versionset') as c:
        c.argument('version_set_id', help="A resource identifier for the related ApiVersionSet.")
        c.argument('versioning_scheme', help="Required. An value that determines where the API Version identifer will be located in a HTTP request. Possible values include: 'Segment', 'Query', 'Header'")
        c.argument('display_name', help="Required. Name of API Version Set")
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the API Management service instance.")
        c.argument('description', help="Description of API Version Set.")
        c.argument('version_query_name', help="Name of query parameter that indicates the API Version if versioningScheme is set to `query`.")
        c.argument('version_header_name', help="Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.")
        c.argument('if_match', help='ETag of the Entity.')
