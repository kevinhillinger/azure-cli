# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['apim'] = """
type: group
short-summary: Manage Azure API Management services.
"""

helps['apim api'] = """
type: group
short-summary: Manage Azure API Management API's.
"""

helps['apim backup'] = """
type: command
short-summary: Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.
examples:
  - name: Create a backup of the API Management service instance
    text: |-
        az apim backup --name MyApim -g MyResourceGroup --backup-name myBackup \
             --storage-account-name mystorageaccount --storage-account-container backups \
             --storage-account-key Ay2ZbdxLnD4OJPT29F6jLPkB6KynOzx85YCObhrw==
"""

helps['apim create'] = """
type: command
short-summary: Create an API Management service instance.
parameters:
  - name: --name -n
    type: string
    short-summary: unique name of the service instance to be created
    long-summary: |
        The name must be globally unique since it will be included as the gateway
        hostname like' https://my-api-servicename.azure-api.net'.  See examples.
examples:
  - name: Create a Developer tier API Management service.
    text: |-
        az apim create --name MyApim -g MyResourceGroup -l eastus --publisher-email email@mydomain.com --publisher-name Microsoft
  - name: Create a Consumption tier API Management service.
    text: |-
        az apim create --name MyApim -g MyResourceGroup -l eastus --sku-name Consumption --enable-client-certificate \\
            --publisher-email email@mydomain.com --publisher-name Microsoft
"""

helps['apim delete'] = """
type: command
short-summary: Deletes an API Management service.
examples:
  - name: Delete an API Management service.
    text: >
        az apim delete -n MyApim -g MyResourceGroup
"""

helps['apim list'] = """
type: command
short-summary: List API Management service instances.
"""

helps['apim show'] = """
type: command
short-summary: Show details of an API Management service instance.
"""

helps['apim update'] = """
type: command
short-summary: Update an API Management service instance.
"""

helps['apim product list'] = """
type: command
short-summary: Lists a collection of products in the specified service instance.
"""

helps['apim product create'] = """
type: command
short-summary: Create a product specified by the name.
parameters:
  - name: --product_name -p
    type: string
    short-summary: unique name of the product
    long-summary: |
        The unique internal name of the product.  See 'name' attribute from
        list-by-service result.
examples:
  - name: Creates a product with no options set.
    text: >
        az apim product create -g MyResourceGroup -n MyApim -p NewName
  - name: Create a product in a published state.
    text: >
        az apim product create -g MyResourceGroup -n MyApim -p NewName --state published
"""

helps['apim product update'] = """
type: command
short-summary: Updates product attributes specified by the options.
parameters:
  - name: --product_name -p
    type: string
    short-summary: unique name of the product
    long-summary: |
        The unique internal name of the product.  See 'name' attribute from
        list-by-service result.
examples:
  - name: Updates the state of a product to a published state and updates the description.
    text: >
        az apim product update -g MyResourceGroup -n MyApim -p NewName --state published --description "My Description"
"""

helps['apim product show'] = """
type: command
short-summary: Gets the details of the product specified by its name.
parameters:
  - name: --product_name -p
    type: string
    short-summary: unique name of the product
    long-summary: |
        The unique internal name of the product.  See 'name' attribute from
        list-by-service result.
examples:
  - name: Common usage.
    text: >
        az apim product show -n MyApim -g MyResourceGroup -p starter
"""

helps['apim product delete'] = """
type: command
short-summary: Deletes the product specified by its name.
parameters:
  - name: --product_name -p
    type: string
    short-summary: unique name of the product
    long-summary: |
        The unique internal name of the product.  See 'name' attribute from
        list-by-service result.
examples:
  - name: Common usage.
    text: >
        az apim product delete -g MyResourceGroup -n MyApim -p starter
"""