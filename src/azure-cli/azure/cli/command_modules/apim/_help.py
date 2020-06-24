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

# policy
helps['apim policy'] = """
type: group
short-summary: Manage Azure API Management policies.
"""

helps['apim policy show'] = """
type: command
short-summary: Show details of a policy for an API Management instance.
"""

helps['apim policy create'] = """
type: command
short-summary: Create a policy for an API Management instance.
"""

helps['apim policy update'] = """
type: command
short-summary: Update a policy for an API Management instance.
"""

helps['apim policy delete'] = """
type: command
short-summary: Delete a policy for an API Management instance.
"""

# product
helps['apim product'] = """
type: group
short-summary: Manage Azure API Management products.
"""

helps['apim product list'] = """
type: command
short-summary: Lists a collection of products in the specified service instance.
"""

helps['apim product create'] = """
type: command
short-summary: Create a product specified by the name.
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
examples:
  - name: Updates the state of a product to a published state and updates the description.
    text: >
        az apim product update -g MyResourceGroup -n MyApim -p NewName --state published --description "My Description"
"""

helps['apim product show'] = """
type: command
short-summary: Gets the details of the product specified by its name.
examples:
  - name: Common usage.
    text: >
        az apim product show -n MyApim -g MyResourceGroup -p starter
"""

helps['apim product delete'] = """
type: command
short-summary: Deletes the product specified by its name.
examples:
  - name: Common usage.
    text: >
        az apim product delete -g MyResourceGroup -n MyApim -p starter
"""

helps['apim api create'] = """
type: command
short-summary: Creates new API of the API Management service instance.
parameters:
  - name: --display-name
    type: string
    short-summary: Display name of the api to be created. Must be 1 to 300 characters long. If no supplied, defaults to the value of the path parameter. 
  - name: --oauth2-authorization-server-id
    type: string
    short-summary: OAuth 2.0 authorization server identifier. Authorization server definition must already exist in the API Management service instance. 
  - name: --oauth2-scope
    type: string
    short-summary: OAuth 2.0 operations scope. 
  - name: --openid-provider-id
    type: string
    short-summary: OpenID authorization server identifier. Authorization server definition must already exist in the API Management service instance. 
  - name: --service-url
    type: string
    short-summary: Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.
  - name: --source-api-id
    type: string
    short-summary: API identifier of the source API, to clone an existing API.
  - name: --subscription-key-header-name
    type: string
    short-summary: Subscription key HTTP header name.
  - name: --subscription-key-query-string-name
    type: string
    short-summary: Subscription key query string parameter name.
  - name: --value
    type: string
    short-summary: Content value when Importing an API.
  - name: --wsdl-endpoint-name
    type: string
    short-summary: Name of endpoint(port) to import from WSDL.
  - name: --wsdl-service-name
    type: string
    short-summary: CName of service to import from WSDL.
  - name: --api-version
    type: string
    short-summary: Indicate the Version identifier of the API if the API is versioned.
  - name: --api-version-set-id
    type: string
    short-summary: Identifier for existing API Version Set.
  - name: --api-revision
    type: string
    short-summary: Describes the Revision of the Api. If no value is provided, default revision 1 is created.
  - name: --api-revision-description
    type: string
    short-summary: Description of the API Revision.
examples:
  - name: Create an API, using the Echo service backend, enabling both protocols.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyApi --path MyApiPath --display-name "MyApi Display nName" --description "MyApi Description" --service-url "http://echoapi.cloudapp.net/api" --protocols "http https"
  - name: Clone an existing API, changing the service URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyClonedApi --path MyClonedApiPath --service-url "http://httpbin.org" --display-name "MyClonedApi Display Name" --description "MyClonedApi Description" --source-api-id "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/SourceResourceGroupName/providers/Microsoft.ApiManagement/service/SourceApimInstanceName/apis/MySourceApiId"
  - name: Create a new API from an existing API version set. To create a new api version set, use the 'az apim api version-set create' command.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyApiFromVersionSet --path MyApiFromVersionSetPath --display-name "MyApiFromVersionSet Display Name" --service-url "http://echoapi.cloudapp.net/api" --protocols "http https" --source-api-id "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/SourceResourceGroupName/providers/Microsoft.ApiManagement/service/SourceApimInstanceName/apis/MySourceApiId" --api-version v2 --api-version-set-id "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/SourceResourceGroupName/providers/Microsoft.ApiManagement/service/SourceApimInstanceName/apiVersionSets/d072a59c-09e9-477d-9a3e-c675b254603e" --is-current
  - name: Create an API revision from an existing API, changing the service URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a "MyApi;rev=2" --path MyApiPath --service-url "http://echoapi.cloudapp.net/apirev2" --api-revision-description "A Revision of an existing API" --source-api-id "subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/SourceResourceGroupName/providers/Microsoft.ApiManagement/service/SourceApimInstanceName/apis/api-id"
  - name: Create an API with OpenID Connect to the backend, sending the bearer token via the Authorization HTTP header.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyOpenIdConnectApi --display-name "Swagger Petstore" --description "This is a sample server Petstore server" --path petstore --openid-provider-id IdPid --openid-bearer-token-sending-methods authorizationHeader
  - name: Import an API from a Swagger JSON link.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MySwaggerApi --format "swagger-link-json" --value "http://petstore.swagger.io/v2/swagger.json" --path petstore 
  - name: Import an API from a Swagger JSON link, overwriting the service URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MySwaggerApi --format "swagger-link-json" --value "http://apimpimportviaurl.azurewebsites.net/api/apidocs/" --path petstoreapi123 --service-url "http://petstore.swagger.wordnik.com/api"
  - name: Import an API from an OpenAPI 3 URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyOai3Api --format "openapi-link" --value "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml" --path petstore
  - name: Import an API with SOAP pass-through using a WSDL URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyCalculatorApi --format "wsdl-link" --value "http://www.dneonline.com/calculator.asmx?wsdl" --path "calulator-soap" --wsdl-service-name Calculator --wsdl-endpoint-name CalculatorSoap --api-type soap
  - name: Import an API converting a WSDL SOAP endpoint to a REST endpoint.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyCalculatorApi --format "wsdl-link" --value "http://www.dneonline.com/calculator.asmx?wsdl" --path "calulator-http" --wsdl-service-name Calculator --wsdl-endpoint-name CalculatorSoap --api-type http
"""

helps['apim api update'] = """
type: command
short-summary: Updates API attributes specified by the parameters.
parameters:
  - name: --display-name
    type: string
    short-summary: Display name of the api to be created. Must be 1 to 300 characters long. If no supplied, defaults to the value of the path parameter. 
  - name: --oauth2-authorization-server-id
    type: string
    short-summary: OAuth 2.0 authorization server identifier. Authorization server definition must already exist in the API Management service instance. 
  - name: --oauth2-scope
    type: string
    short-summary: OAuth 2.0 operations scope. 
  - name: --openid-provider-id
    type: string
    short-summary: OpenID authorization server identifier. Authorization server definition must already exist in the API Management service instance. 
  - name: --service-url
    type: string
    short-summary: Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.
  - name: --source-api-id
    type: string
    short-summary: API identifier of the source API, to clone an existing API.
  - name: --subscription-key-header-name
    type: string
    short-summary: Subscription key HTTP header name.
  - name: --subscription-key-query-string-name
    type: string
    short-summary: Subscription key query string parameter name.
  - name: --value
    type: string
    short-summary: Content value when Importing an API.
  - name: --wsdl-endpoint-name
    type: string
    short-summary: Name of endpoint(port) to import from WSDL.
  - name: --wsdl-service-name
    type: string
    short-summary: CName of service to import from WSDL.
  - name: --api-version
    type: string
    short-summary: Indicate the Version identifier of the API if the API is versioned.
  - name: --api-version-set-id
    type: string
    short-summary: Identifier for existing API Version Set.
  - name: --api-revision
    type: string
    short-summary: Describes the Revision of the Api. If no value is provided, default revision 1 is created.
  - name: --api-revision-description
    type: string
    short-summary: Description of the API Revision.
examples:
  - name: Update an API, setting a new path, display name, description, service URL and protocol(s).
    text: >
        az apim api update -n MyApim -g MyResourceGroup -a MyApi --path MyNewApiPath --display-name "MyApi New Display nName" --description "MyApi New Description" --service-url "http://echoapi.cloudapp.net/newapi" --protocols "https"
"""

helps['apim api delete'] = """
type: command
short-summary: Deletes the specified API of the API Management service instance.
parameters:
  - name: --delete-revisions
    type: string
    short-summary: Delete all revisions of the API.
examples:
  - name: Common usage.
    text: >
        az apim api delete -n MyApim -g MyResourceGroup -a MyApi
  - name: Delete revision 3 of an API (use quotes for the --api-id parameter).
    text: >
        az apim api delete -n MyApim -g MyResourceGroup -a "MyApi;rev=3"
  - name: Delete all revisions of an API (for a single revision, the API will be completely deleted).
    text: >
        az apim api delete -n MyApim -g MyResourceGroup -a MyApi --delete-revisions
"""

helps['apim api show'] = """
type: command
short-summary: Gets the details of the API specified by its identifier.
examples:
  - name: Common usage (shows the 'current' revision).
    text: >
        az apim api show -n MyApim -g MyResourceGroup -a MyApi
  - name: Show detail of revision 3 of an API (use quotes for the --api-id parameter).
    text: >
        az apim api show -n MyApim -g MyResourceGroup -a "MyApi;rev=3"
"""

helps['apim api list'] = """
type: command
short-summary: Lists all APIs of the API Management service instance.
examples:
  - name: Common usage (lists only 'current' APIs). To list all revisions of an API, use the 'az apim api revision list' command.
    text: >
        az apim api list -n MyApim -g MyResourceGroup
  - name: Lists all APIs, including the version set information.
    text: >
        az apim api list -n MyApim -g MyResourceGroup --expand-api-version-set
"""