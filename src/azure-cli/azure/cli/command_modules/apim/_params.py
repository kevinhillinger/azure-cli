# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_location_type,
                                                resource_group_name_type,
                                                get_three_state_flag)
from azure.mgmt.apimanagement.models import (SkuType, VirtualNetworkType, ProductState, SoapApiType, ContentFormat, SubscriptionState)
from azure.cli.command_modules.apim.operations.subscription import SubscriptionKeyKind

SKU_TYPES = SkuType
VNET_TYPES = VirtualNetworkType
STATE_TYPES = ProductState
SUBSCRIPTION_TYPES = SubscriptionState
SUBSCRIPTION_KEY_KIND = SubscriptionKeyKind

def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    # api service
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

    # policy
    with self.argument_context('apim policy') as c:
        c.argument('xml', options_list=['--xml-value', '-v'], help='The XML document value inline as a non-XML encoded string.')
        c.argument('xml_path', options_list=['--xml-file', '-f'], help='The path to the policy XML document.')
        c.argument('xml_uri', options_list=['--xml-uri', '-u'], help='The URI of the policy XML document from an HTTP endpoint accessible from the API Management service.')

    # product
    with self.argument_context('apim api') as c:
        c.argument('api_id', options_list=['--api-id', '-a'], help='API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.')
        c.argument('path', options_list=['--path', '-p'], help='Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API.')
        c.argument('description', options_list=['--description', '-d'], help='Description of the API. May include HTML formatting tags.')
        c.argument('subscription_required', arg_type=get_three_state_flag(), help='Indicate whether an API or Product subscription is required for accessing the API. If parameter is omitted when creating a new API its value is assumed to be true.')
        c.argument('is_current', arg_type=get_three_state_flag(), help='Indicate if an API revision is the current api revision. New revisions cannot be set as current.')
        c.argument('is_online', arg_type=get_three_state_flag(), help='Indicate if an API revision is accessible via the gateway.')
        c.argument('protocols', nargs='+', help='Describe on which protocols the operations in this API can be invoked. Default: "https"')
        c.argument('openid_bearer_token_sending_methods', nargs='+', help='Indicate how to send the bearer token to the backend server.')
        c.argument('api_type', arg_type=get_enum_type(SoapApiType), help='Type of API to create.')
        c.argument('import_format', arg_type=get_enum_type(ContentFormat), help='Format of the Content in which the API is getting imported.')
        c.argument('delete_revisions', arg_type=get_three_state_flag(), help='Delete all revisions of the API.')
        c.argument('expand_api_version_set', arg_type=get_three_state_flag(), help='Include full ApiVersionSet resource in response.')

    with self.argument_context('apim product') as c:
        c.argument('product_id', options_list=['--product_id', '-p'], help='Product identifier. Must be unique in the current API Management service instance.')
        c.argument('description', options_list=['--description', '-d'], help='Product description. May include HTML formatting tags.')
        c.argument('terms', help='Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.')
        c.argument('subscription_required', arg_type=get_three_state_flag(), help='Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product its value is assumed to be true.')
        c.argument('approval_required', help='Whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.')
        c.argument('subscriptions_limit', type=int, help='Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.')
        c.argument('state', get_enum_type(STATE_TYPES), help='Whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.')

    with self.argument_context('apim subscription') as c:
        c.argument('sid', arg_group="Subscription", help='Subscription entity Identifier. The entity represents the association between a user and a product in API Management.')
        c.argument('display_name', options_list=['--display_name', '-d'], arg_group='Subscription', help='Subscription name')
        c.argument('owner_id', arg_group='Subscription', help='User (user id path) for whom subscription is being created in form /users/{userId}')
        c.argument('state', get_enum_type(SUBSCRIPTION_TYPES), arg_group='Subscription', help='Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated. Possible values include: \'suspended\', \'active\', \'expired\', \'submitted\', \'rejected\', \'cancelled\'')
        c.argument('allow_tracing', options_list=['--allow_tracing', '-a'], arg_type=get_three_state_flag(), arg_group='Subscription', help='Determines whether tracing can be enabled')
        c.argument('scope', arg_group='Subscription', help='Scope like /products/{productId} or /apis or /apis/{apiId}.')
        c.argument('primary_key', arg_group="Subscription", help='The primary access key for the APIM subscription')
        c.argument('secondary_key', arg_group="Subscription", help='The secondary access key for the APIM subscription')
    
    for scope in ['apim subscription keys regenerate', 'apim subscription regenerate-key']:
        with self.argument_context(scope) as c:
            c.argument('key_kind', arg_type=get_enum_type(SubscriptionKeyKind), help='The type of key to regenerate: primary or secondary')
