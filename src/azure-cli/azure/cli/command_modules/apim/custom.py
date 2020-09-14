# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.util import sdk_no_wait
from azure.mgmt.apimanagement.models import (ApiManagementServiceResource, ApiManagementServiceIdentity,
                                             ApiManagementServiceSkuProperties, ApiManagementServiceBackupRestoreParameters,
                                             ApiContract, ApiType, ApiCreateOrUpdateParameter, Protocol,
                                             VirtualNetworkType, SkuType, ApiCreateOrUpdatePropertiesWsdlSelector,
                                             SoapApiType, ContentFormat, SubscriptionKeyParameterNamesContract,
                                             OAuth2AuthenticationSettingsContract, AuthenticationSettingsContract,
                                             OpenIdAuthenticationSettingsContract, ProductContract, ProductState,
                                             NamedValueCreateContract, VersioningScheme, ApiVersionSetContract,
                                             OperationContract)

# Service Operations


def create_apim(client, resource_group_name, name, publisher_email, sku_name=SkuType.developer.value,
                sku_capacity=1, virtual_network_type=VirtualNetworkType.none.value, enable_managed_identity=False,
                enable_client_certificate=None, publisher_name=None, location=None, tags=None, no_wait=False):

    resource = ApiManagementServiceResource(
        location=location,
        notification_sender_email=publisher_email,
        publisher_email=publisher_email,
        publisher_name=publisher_name,
        sku=ApiManagementServiceSkuProperties(name=sku_name, capacity=sku_capacity),
        enable_client_certificate=enable_client_certificate,
        virtual_network_type=VirtualNetworkType(virtual_network_type),
        tags=tags
    )

    if enable_managed_identity:
        resource['identity'] = ApiManagementServiceIdentity(type="SystemAssigned")

    if resource.sku.name == SkuType.consumption.value:
        resource.sku.capacity = 0

    cms = client.api_management_service

    return sdk_no_wait(no_wait, cms.create_or_update,
                       resource_group_name=resource_group_name,
                       service_name=name, parameters=resource)


def update_apim(instance, publisher_email=None, sku_name=None, sku_capacity=None,
                virtual_network_type=None, publisher_name=None, enable_managed_identity=None,
                enable_client_certificate=None, tags=None):

    if publisher_email is not None:
        instance.publisher_email = publisher_email

    if sku_name is not None:
        instance.sku.name = sku_name

    if sku_capacity is not None:
        instance.sku.capacity = sku_capacity

    if virtual_network_type is not None:
        instance.virtual_network_type = virtual_network_type

    if publisher_email is not None:
        instance.publisher_email = publisher_email

    if publisher_name is not None:
        instance.publisher_name = publisher_name

    if not enable_managed_identity:
        instance.identity = None
    else:
        if instance.identity is None:
            instance.identity = ApiManagementServiceIdentity(type="SystemAssigned")

    if enable_client_certificate is not None:
        instance.enable_client_certificate = enable_client_certificate

    if tags is not None:
        instance.tags = tags

    return instance


def list_apim(client, resource_group_name=None):
    """List all APIM instances.  Resource group is optional """
    if resource_group_name:
        return client.api_management_service.list_by_resource_group(resource_group_name)
    return client.api_management_service.list()


def get_apim(client, resource_group_name, name):
    """Show details of an APIM instance """
    return client.api_management_service.get(resource_group_name, name)


def check_name_availability(client, name):
    """checks to see if a service name is available to use """
    return client.api_management_service.check_name_availability(name)


def apim_backup(client, resource_group_name, name, backup_name, storage_account_name,
                storage_account_container, storage_account_key):
    """back up an API Management service to the configured storage account """
    parameters = ApiManagementServiceBackupRestoreParameters(
        storage_account=storage_account_name,
        access_key=storage_account_key,
        container_name=storage_account_container,
        backup_name=backup_name)

    return client.api_management_service.backup(resource_group_name, name, parameters)


def apim_apply_network_configuration_updates(client, resource_group_name, name, location=None):
    """back up an API Management service to the configured storage account """
    properties = {}
    if location is not None:
        properties['location'] = location

    return client.api_management_service.apply_network_configuration_updates(resource_group_name, name, properties)


def get_subscription_key_parameter_names(subscription_key_header_name=None, subscription_key_query_param_name=None):
    if subscription_key_query_param_name is not None and subscription_key_header_name is not None:
        return SubscriptionKeyParameterNamesContract(
            header=subscription_key_header_name,
            query=subscription_key_query_param_name
        )
    elif subscription_key_query_param_name is not None or subscription_key_header_name is not None:
        raise CLIError("Please specify 'subscription_key_query_param_name' and 'subscription_key_header_name' at the same time.")

    return None


# Product API Operations

def list_product_api(client, resource_group_name, service_name, product_id):

    return client.product_api.list_by_product(resource_group_name, service_name, product_id)


def check_product_exists(client, resource_group_name, service_name, product_id, api_id):

    return client.product_api.check_entity_exists(resource_group_name, service_name, product_id, api_id)


def add_product_api(client, resource_group_name, service_name, product_id, api_id, no_wait=False):

    return sdk_no_wait(
        no_wait,
        client.product_api.create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        product_id=product_id,
        api_id=api_id)


def delete_product_api(client, resource_group_name, service_name, product_id, api_id, no_wait=False):

    return sdk_no_wait(
        no_wait,
        client.product_api.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        product_id=product_id,
        api_id=api_id)


# Product Operations

def list_products(client, resource_group_name, service_name):

    return client.product.list_by_service(resource_group_name, service_name)


def show_product(client, resource_group_name, service_name, product_id):

    return client.product.get(resource_group_name, service_name, product_id)


def create_product(client, resource_group_name, service_name, product_name, product_id=None, description=None, legal_terms=None, subscription_required=None, approval_required=None, subscriptions_limit=None, state=None, no_wait=False):

    parameters = ProductContract(
        description=description,
        terms=legal_terms,
        subscription_required=subscription_required,
        display_name=product_name,
        approval_required=approval_required,
        subscriptions_limit=subscriptions_limit
    )

    # Possible values include: 'notPublished', 'published'
    if state is not None:
        if state == ProductState.not_published:
            parameters.state = ProductState.not_published
        elif state == ProductState.published:
            parameters.state = ProductState.published
        else:
            raise CLIError("State " + state + " is not supported.")

    if product_id is None:
        product_id = uuid.uuid4().hex

    return sdk_no_wait(
        no_wait,
        client.product.create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        product_id=product_id,
        parameters=parameters)


def update_product(instance, product_name=None, description=None, legal_terms=None, subscription_required=None, approval_required=None, subscriptions_limit=None, state=None):

    if product_name is not None:
        instance.display_name = product_name

    if description is not None:
        instance.description = description

    if legal_terms is not None:
        instance.terms = legal_terms

    if subscription_required is not None:
        instance.subscription_required = subscription_required

    if approval_required is not None:
        instance.approval_required = approval_required

    if subscriptions_limit is not None:
        instance.subscriptions_limit = subscriptions_limit

    if state is not None:
        if state == ProductState.not_published:
            instance.state = ProductState.not_published
        elif state == ProductState.published:
            instance.state = ProductState.published
        else:
            raise CLIError("State " + state + " is not supported.")

    return instance


def delete_product(client, resource_group_name, service_name, product_id, delete_subscriptions=None, if_match=None, no_wait=False):

    return sdk_no_wait(
        no_wait,
        client.product.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        product_id=product_id,
        delete_subscriptions=delete_subscriptions,
        if_match="*" if if_match is None else if_match)


# Named Value Operations

def create_apim_nv(client, resource_group_name, service_name, named_value_id, display_name, value=None, tags=None, secret=False):
    """Creates a new Named Value. """

    resource = NamedValueCreateContract(
        tags=tags,
        secret=secret,
        display_name=display_name,
        value=value
    )

    return client.named_value.create_or_update(resource_group_name, service_name, named_value_id, resource)


def get_apim_nv(client, resource_group_name, service_name, named_value_id):
    """Shows details of a Named Value. """

    return client.named_value.get(resource_group_name, service_name, named_value_id)


def get_apim_nv_secret(client, resource_group_name, service_name, named_value_id):
    """Gets the secret of the NamedValue."""

    return client.named_value.list_value(resource_group_name, service_name, named_value_id)


def list_apim_nv(client, resource_group_name, service_name):
    """List all Named Values of an API Management instance. """

    return client.named_value.list_by_service(resource_group_name, service_name)


def delete_apim_nv(client, resource_group_name, service_name, named_value_id):
    """Deletes an existing Named Value. """

    return client.named_value.delete(resource_group_name, service_name, named_value_id, if_match='*')


def update_apim_nv(instance, value=None, tags=None, secret=None):
    """Updates an existing Named Value."""
    if tags is not None:
        instance.tags = tags

    if value is not None:
        instance.value = value

    if secret is not None:
        instance.secret = secret

    return instance


def list_api_operation(client, resource_group_name, service_name, api_id):
    """List a collection of the operations for the specified API."""

    return client.api_operation.list_by_api(resource_group_name, service_name, api_id)


def get_api_operation(client, resource_group_name, service_name, api_id, operation_id):
    """Gets the details of the API Operation specified by its identifier."""

    return client.api_operation.get(resource_group_name, service_name, api_id, operation_id)


def create_api_operation(client, resource_group_name, service_name, api_id, url_template, method, display_name, template_parameters=None, operation_id=None, description=None, if_match=None, no_wait=False):
    """Creates a new operation in the API or updates an existing one."""

    if operation_id is None:
        operation_id = uuid.uuid4().hex

    resource = OperationContract(
        description=description,
        display_name=display_name,
        method=method,
        url_template=url_template,
        template_parameters=template_parameters)

    return sdk_no_wait(
        no_wait,
        client.api_operation.create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        api_id=api_id,
        operation_id=operation_id,
        parameters=resource,
        if_match="*" if if_match is None else if_match)


def update_api_operation(instance, display_name=None, description=None, method=None, url_template=None):
    """Updates the details of the operation in the API specified by its identifier."""

    if display_name is not None:
        instance.display_name = display_name

    if description is not None:
        instance.description = description

    if method is not None:
        instance.method = method

    if url_template is not None:
        instance.url_template = url_template

    return instance


def delete_api_operation(client, resource_group_name, service_name, api_id, operation_id, if_match=None, no_wait=False):
    """Deletes the specified operation in the API."""

    return sdk_no_wait(
        no_wait,
        client.api_operation.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        api_id=api_id,
        operation_id=operation_id,
        if_match="*" if if_match is None else if_match)


def list_api_release(client, resource_group_name, service_name, api_id):
    """Lists all releases of an API."""

    return client.api_release.list_by_service(resource_group_name, service_name, api_id)


def show_api_release(client, resource_group_name, service_name, api_id, release_id):
    """Returns the details of an API release."""

    return client.api_release.get(resource_group_name, service_name, api_id, release_id)


def create_api_release(client, resource_group_name, service_name, api_id, api_revision, release_id=None, if_match=None, notes=None):
    """Creates a new Release for the API."""

    if release_id is None:
        release_id = uuid.uuid4().hex

    api_id1 = "/apis/" + api_id + ";rev=" + api_revision

    return client.api_release.create_or_update(resource_group_name, service_name, api_id, release_id, "*" if if_match is None else if_match, api_id1, notes)


def update_api_release(instance, notes=None):
    """Updates the details of the release of the API specified by its identifier."""

    instance.notes = notes

    return instance


def delete_api_release(client, resource_group_name, service_name, api_id, release_id, if_match=None):
    """Deletes the specified release in the API."""

    return client.api_release.delete(resource_group_name, service_name, api_id, release_id, "*" if if_match is None else if_match)


def list_api_revision(client, resource_group_name, service_name, api_id):
    """Lists all revisions of an API."""

    return client.api_revision.list_by_service(resource_group_name, service_name, api_id)


def create_apim_api_revision(client, resource_group_name, service_name, api_id, api_revision, api_revision_description=None,
                             no_wait=False):
    """Creates a new API Revision. """

    cur_api = client.api.get(resource_group_name, service_name, api_id)

    resource = ApiCreateOrUpdateParameter(
        path=cur_api.path,
        display_name=cur_api.display_name,
        service_url=cur_api.service_url,
        authentication_settings=cur_api.authentication_settings,
        protocols=cur_api.protocols,
        subscription_key_parameter_names=cur_api.subscription_key_parameter_names,
        api_revision_description=api_revision_description,
        source_api_id="/apis/" + api_id
    )

    return sdk_no_wait(no_wait, client.api.create_or_update,
                       resource_group_name=resource_group_name, service_name=service_name,
                       api_id=api_id + ";rev=" + api_revision, parameters=resource)


def list_api_vs(client, resource_group_name, service_name):
    """Lists a collection of API Version Sets in the specified service instance."""

    return client.api_version_set.list_by_service(resource_group_name, service_name)


def show_api_vs(client, resource_group_name, service_name, version_set_id):
    """Gets the details of the Api Version Set specified by its identifier."""

    return client.api_version_set.get(resource_group_name, service_name, version_set_id)


def create_api_vs(client, resource_group_name, service_name, display_name, versioning_scheme, version_set_id=None, if_match=None, description=None, version_query_name=None, version_header_name=None, no_wait=False):
    """Creates or Updates a Api Version Set."""

    if version_set_id is None:
        version_set_id = uuid.uuid4().hex

    resource = ApiVersionSetContract(
        description=description,
        versioning_scheme=versioning_scheme,
        display_name=display_name)

    if versioning_scheme == VersioningScheme.header:
        if version_header_name is None:
            raise CLIError("Please specify version header name while using 'header' as version scheme.")

        resource.version_header_name = version_header_name

    if versioning_scheme == VersioningScheme.query:
        if version_query_name is None:
            raise CLIError("Please specify version query name while using 'query' as version scheme.")

        resource.version_query_name = version_query_name

    return sdk_no_wait(
        no_wait,
        client.api_version_set.create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        version_set_id=version_set_id,
        parameters=resource,
        if_match="*" if if_match is None else if_match)


def update_api_apivs(instance, versioning_scheme=None, description=None, display_name=None, version_header_name=None, version_query_name=None):
    """Updates the details of the Api VersionSet specified by its identifier."""

    if display_name is not None:
        instance.display_name = display_name

    if versioning_scheme is not None:
        instance.versioning_scheme = versioning_scheme
        if versioning_scheme == VersioningScheme.header:
            if version_header_name is None:
                raise CLIError("Please specify version header name while using 'header' as version scheme.")

            instance.version_header_name = version_header_name
            instance.version_query_name = None
        if versioning_scheme == VersioningScheme.query:
            if version_query_name is None:
                raise CLIError("Please specify version query name while using 'query' as version scheme.")

            instance.version_query_name = version_query_name
            instance.version_header_name = None

    if description is None:
        instance.description = description

    return instance


def delete_api_vs(client, resource_group_name, service_name, version_set_id, if_match=None, no_wait=False):
    """Deletes specific Api Version Set."""

    return sdk_no_wait(
        no_wait,
        client.api_version_set.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        version_set_id=version_set_id,
        if_match="*" if if_match is None else if_match)
