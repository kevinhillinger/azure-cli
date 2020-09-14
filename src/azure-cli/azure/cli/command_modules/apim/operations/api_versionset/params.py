# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('apim api versionset') as c:
        c.argument('version_set_id', help="A resource identifier for the related ApiVersionSet.")
        c.argument('versioning_scheme', help="Required. An value that determines where the API Version identifer will be located in a HTTP request. Possible values include: 'Segment', 'Query', 'Header'")
        c.argument('display_name', help="Required. Name of API Version Set")
        c.argument('service_name', options_list=['--service-name', '-n'], help="The name of the API Management service instance.")
        c.argument('description', help="Description of API Version Set.")
        c.argument('version_query_name', help="Name of query parameter that indicates the API Version if versioningScheme is set to `query`.")
        c.argument('version_header_name', help="Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.")
        c.argument('if_match', help='ETag of the Entity.')
