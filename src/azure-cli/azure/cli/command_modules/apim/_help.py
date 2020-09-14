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


helps['apim product api'] = """
type: group
short-summary: Manage Azure API Management Product's APIs.
"""

helps['apim product'] = """
type: group
short-summary: Manage Azure API Management Product's.
"""

helps['apim nv'] = """
type: group
short-summary: Manage Azure API Management Named Values.
"""

helps['apim api operation'] = """
type: group
short-summary: Manage Azure API Management API Operations.
"""

helps['apim api release'] = """
type: group
short-summary: Manage Azure API Management API Release.
"""

helps['apim api revision'] = """
type: group
short-summary: Manage Azure API Management API Revision.
"""

helps['apim api versionset'] = """
type: group
short-summary: Manage Azure API Management API Version Set.
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

# api
helps['apim api'] = """
type: group
short-summary: Manage Azure API Management API services.
"""

helps['apim api create'] = """
type: command
short-summary: Creates new API of the API Management service instance.
parameters:
  - name: --display-name
    type: string
    short-summary: Display name of the api to be created. Must be 1 to 300 characters long. If no supplied, defaults to the value of the path parameter.
  - name: --oauth2-server-id
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
  - name: --header-name
    type: string
    short-summary: Subscription key HTTP header name.
  - name: --querystring-name
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
    short-summary: Resource identifier for existing API Version Set.
  - name: --api-revision
    type: string
    short-summary: Describes the Revision of the Api. If no value is provided, default revision 1 is created.
  - name: --revision-description
    type: string
    short-summary: Description of the API Revision.
examples:
  - name: Create an API, using the Echo service backend, enabling both protocols.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyApi --path MyApiPath --display-name "MyApi Display nName" --description "MyApi Description" --service-url "http://echoapi.cloudapp.net/api" --protocols "http https"
  - name: Clone an existing API, changing the service URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyClonedApi --path MyClonedApiPath --service-url "http://httpbin.org" --display-name "MyClonedApi Display Name" --description "MyClonedApi Description" --source-api-id my-api-id
  - name: Create a new API from an existing API version set. To create a new api version set, use the 'az apim api version-set create' command.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyApiFromVersionSet --path MyApiFromVersionSetPath --display-name "MyApiFromVersionSet Display Name" --service-url "http://echoapi.cloudapp.net/api" --protocols "http https" --source-api-id my-api-id --api-version v2 --api-version-set-id "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/SourceResourceGroupName/providers/Microsoft.ApiManagement/service/SourceApimInstanceName/apiVersionSets/d072a59c-09e9-477d-9a3e-c675b254603e" --is-current
  - name: Create an API revision from an existing API, changing the service URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a "MyApi;rev=2" --path MyApiPath --service-url "http://echoapi.cloudapp.net/apirev2" --revision-description "A Revision of an existing API" --source-api-id my-api-id
  - name: Create an API with OpenID Connect to the backend, sending the bearer token via the Authorization HTTP header.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyOpenIdConnectApi --display-name "Swagger Petstore" --description "This is a sample server Petstore server" --path petstore --openid-provider-id IdPid --openid-token-methods authorizationHeader
  - name: Import an API from a Swagger JSON link.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MySwaggerApi --import-format "swagger-link-json" --value "http://petstore.swagger.io/v2/swagger.json" --path petstore
  - name: Import an API from a Swagger JSON link, overwriting the service URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MySwaggerApi --import-format "swagger-link-json" --value "http://apimpimportviaurl.azurewebsites.net/api/apidocs/" --path petstoreapi123 --service-url "http://petstore.swagger.wordnik.com/api"
  - name: Import an API from an OpenAPI 3 URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyOai3Api --import-format "openapi-link" --value "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml" --path petstore
  - name: Import an API with SOAP pass-through using a WSDL URL.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyCalculatorApi --import-format "wsdl-link" --value "http://www.dneonline.com/calculator.asmx?wsdl" --path "calulator-soap" --wsdl-service-name Calculator --wsdl-endpoint-name CalculatorSoap --api-type soap
  - name: Import an API converting a WSDL SOAP endpoint to a REST endpoint.
    text: >
        az apim api create -n MyApim -g MyResourceGroup -a MyCalculatorApi --import-format "wsdl-link" --value "http://www.dneonline.com/calculator.asmx?wsdl" --path "calulator-http" --wsdl-service-name Calculator --wsdl-endpoint-name CalculatorSoap --api-type http
"""

helps['apim api update'] = """
type: command
short-summary: Updates API attributes specified by the parameters.
parameters:
  - name: --display-name
    type: string
    short-summary: Display name of the api to be created. Must be 1 to 300 characters long. If no supplied, defaults to the value of the path parameter.
  - name: --oauth2-server-id
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
  - name: --header-name
    type: string
    short-summary: Subscription key HTTP header name.
  - name: --querystring-name
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
  - name: --revision-description
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
        az apim api list -n MyApim -g MyResourceGroup --expand-version-set
"""

# policy
helps['apim policy'] = """
type: group
short-summary: Manage the global policy.
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
short-summary: Manage products.
"""

helps['apim product list'] = """
type: command
short-summary: Lists a collection of products in the specified service instance.
"""

helps['apim product show'] = """
type: command
short-summary: Gets the details of the product specified by its name.
examples:
  - name: Common usage.
    text: >
        az apim product show -n MyApim -g MyResourceGroup -p starter
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

helps['apim product delete'] = """
type: command
short-summary: Deletes the product specified by its name.
examples:
  - name: Common usage.
    text: >
        az apim product delete -g MyResourceGroup -n MyApim -p starter
"""

helps['apim subscription create'] = """
type: command
short-summary: Creates the subscription specified by its subscription ID, display name and scope. Other parameters are optional
examples:
  - name: Common usage.
    text: >
        az apim subscription create -g MyResourceGroup -n MyApim --sid mySubscriptionId -d myDisplayName --scope apis
"""

helps['apim subscription update'] = """
type: command
short-summary: Updates the subscription specified by its identifier
examples:
  - name: Common usage.
    text: >
        az apim subscription update -g MyResourceGroup -n MyApim --sid mySubscriptionId -d myDisplayName --scope apis
"""

helps['apim subscription delete'] = """
type: command
short-summary: Deletes the subscription specified by its identifier
examples:
  - name: Common usage.
    text: >
        az apim subscription delete -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription list'] = """
type: command
short-summary: Lists all subscriptions of the API Management service instance
examples:
  - name: Common usage.
    text: >
        az apim subscription list -g MyResourceGroup -n MyApim
"""

helps['apim subscription show'] = """
type: command
short-summary: Shows the specified subscription by its identifier
examples:
  - name: Common usage.
    text: >
        az apim subscription show -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription keys'] = """
type: group
short-summary: Manage API management keys.
"""

helps['apim subscription keys regenerate'] = """
type: command
short-summary: Regenerates a key of an existing subscription of the API Management service. If primary is specified for key-kind or key-kind is omitted, it will regenerate the primary key. Otherwise, specify secondary for key-kind to regenerate the secondary key.
examples:
  - name: Common usage.
    text: >
        az apim subscription keys regenerate --key-kind secondary -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription keys list'] = """
type: command
short-summary: Lists the keys of an existing subscription of the API Management service.
examples:
  - name: Common usage.
    text: >
        az apim subscription keys list -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription regenerate-key'] = """
type: command
short-summary: Regenerates a key of an existing subscription of the API Management service. If primary is specified for key-kind or key-kind is omitted, it will regenerate the primary key. Otherwise, specify secondary for key-kind to regenerate the secondary key.
examples:
  - name: Common usage.
    text: >
        az apim subscription regenerate-key --key-kind secondary -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription'] = """
type: group
short-summary: Manage subscriptions.
"""

helps['apim subscription create'] = """
type: command
short-summary: Creates the subscription specified by its subscription ID, display name and scope. Other parameters are optional
examples:
  - name: Common usage.
    text: >
        az apim subscription create -g MyResourceGroup -n MyApim --sid mySubscriptionId -d myDisplayName --scope apis
"""

helps['apim subscription update'] = """
type: command
short-summary: Updates the subscription specified by its identifier
examples:
  - name: Common usage.
    text: >
        az apim subscription update -g MyResourceGroup -n MyApim --sid mySubscriptionId -d myDisplayName --scope apis
"""

helps['apim subscription delete'] = """
type: command
short-summary: Deletes the subscription specified by its identifier
examples:
  - name: Common usage.
    text: >
        az apim subscription delete -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription list'] = """
type: command
short-summary: Lists all subscriptions of the API Management service instance
examples:
  - name: Common usage.
    text: >
        az apim subscription list -g MyResourceGroup -n MyApim
"""

helps['apim subscription show'] = """
type: command
short-summary: Shows the specified subscription by its identifier
examples:
  - name: Common usage.
    text: >
        az apim subscription show -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription keys'] = """
type: group
short-summary: Manage API management keys.
"""

helps['apim subscription keys regenerate'] = """
type: command
short-summary: Regenerates a key of existing subscription of the API Management. If primary is specified for key-kind or key-kind is omitted, it will regenerate the primary key. Otherwise, specify secondary for key-kind to regenerate the secondary key.
examples:
  - name: Common usage.
    text: >
        az apim subscription keys regenerate --key-kind secondary -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription keys list'] = """
type: command
short-summary: Lists the keys of an existing subscription of the API Management service.
examples:
  - name: Common usage.
    text: >
        az apim subscription keys list -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim subscription regenerate-key'] = """
type: command
short-summary: Regenerates a key of an existing subscription of the API Management service. If primary is specified for key-kind or key-kind is omitted, it will regenerate the primary key. Otherwise, specify secondary for key-kind to regenerate the secondary key.
examples:
  - name: Common usage.
    text: >
        az apim subscription regenerate-key --key-kind secondary -g MyResourceGroup -n MyApim --sid mySubscriptionId
"""

helps['apim api policy'] = """
type: group
short-summary: Manage policies for an API.
"""

helps['apim api policy list'] = """
type: command
short-summary: Lists a collection of policies in the specified API.
examples:
  - name: Common usage.
    text: >
        az apim api policy list -g MyResourceGroup -n MyApim -a echo-api
"""

helps['apim api policy show'] = """
type: command
short-summary: Gets the policy for an API.
examples:
  - name: Common usage.
    text: >
        az apim api policy show -g MyResourceGroup -n MyApim -a echo-api
"""

helps['apim api policy delete'] = """
type: command
short-summary: Delete the policy for an API.
examples:
  - name: Common usage.
    text: >
        az apim api policy delete -g MyResourceGroup -n MyApim -a echo-api
"""

helps['apim api policy create'] = """
type: command
short-summary: Creates a policyfor an API.
"""

helps['apim api policy update'] = """
type: command
short-summary: Updates the policy for an API.
"""

helps['apim product api list'] = """
type: command
short-summary: Lists a collection of the APIs associated with a product.
examples:
  - name: List all APIs associated with a product.
    text: |-
        az apim product api list --resource-group MyResourceGroup  --service-name MyServiceName  --product-id MyProductID
"""

helps['apim product api check'] = """
type: command
short-summary: Checks that API entity specified by identifier is associated with the Product entity.
examples:
  - name: Check if the API is associated with the Product.
    text: |-
        az apim product api check --resource-group MyResourceGroup  --service-name MyServiceName  --product-id MyProductID --api-id MyAPIID
"""

helps['apim product api add'] = """
type: command
short-summary: Add an API to the specified product.
examples:
  - name: Add an API to the specified product.
    text: |-
        az apim product api add --resource-group MyResourceGroup --service-name MyServiceName  --product-id MyProductID --api-id MyAPIID
"""

helps['apim product api delete'] = """
type: command
short-summary: Deletes the specified API from the specified product.
examples:
  - name: Deletes the specified API from the specified product.
    text: |-
        az apim product api delete --resource-group MyResourceGroup --service-name MyServiceName  --product-id MyProductID --api-id MyAPIID
"""

helps['apim product list'] = """
type: command
short-summary: Lists a collection of products in the specified service instance.
examples:
  - name: List all products for this APIM instance.
    text: |-
        az apim product list --resource-group MyResourceGroup --service-name MyServiceName
"""

helps['apim product show'] = """
type: command
short-summary: Gets the details of the product specified by its identifier.
examples:
  - name: Gets the details of the product specified by its identifier.
    text: |-
        az apim product show --resource-group MyResourceGroup --service-name MyServiceName  --product-id MyProductID
"""

helps['apim product create'] = """
type: command
short-summary: Creates a product.
examples:
  - name: Creates a product.
    text: |-
        az apim product create --resource-group MyResourceGroup  --service-name MyServiceName --product-id MyProductID --product-name MyProductName --description MyDescription --legal-terms MyTerms --subscription-required true --approval-required true --subscriptions-limit 8 --state "published"
"""

helps['apim product update'] = """
type: command
short-summary: Update existing product details.
examples:
  - name: Update existing product details.
    text: |-
        az apim product update --resource-group MyResourceGroup  --service-name MyServiceName --product-id MyProductID --product-name MyNewProductName --description MyNewDescription --legal-terms MyNewTerms --subscription-required false --state "notPublished"
"""

helps['apim product delete'] = """
type: command
short-summary: Delete product.
examples:
  - name: Delete product with all subscriptions to this product.
    text: |-
        az apim product delete --resource-group MyResourceGroup  --service-name MyServiceName --product-id MyProductID --delete-subscriptions true
"""

helps['apim nv list'] = """
type: command
short-summary: List API Management Named Values.
"""

helps['apim nv show'] = """
type: command
short-summary: Show details of an API Management Named Value.
"""

helps['apim nv show-secret'] = """
type: command
short-summary: Gets the secret of an API Management Named Value.
"""

helps['apim nv delete'] = """
type: command
short-summary: Delete an API Management Named Value.
"""

helps['apim nv create'] = """
type: command
short-summary: Create an API Management Named Value.
parameters:
  - name: --named-value-id
    type: string
    short-summary: unique name for the Named Value to be created
    long-summary: |
        Must be unique in the current API Management service instance.
  - name: --display-name
    type: string
    short-summary: The Display name of the Named Value.
  - name: --value
    type: string
    short-summary: The value of the Named Value.
examples:
  - name: Create a Named Value.
    text: |-
        az apim nv create --service-name MyApim -g MyResourceGroup --named-value-id MyNamedValue --display-name 'My Named Value' --value 'foo'
"""

helps['apim nv update'] = """
type: command
short-summary: Update an API Management Named Value.
parameters:
  - name: --named-value-id
    type: string
    short-summary: unique name of the api to be created
    long-summary: |
        Must be unique in the current API Management service instance.
  - name: --value
    type: string
    short-summary: The value of the Named Value.
examples:
  - name: Create a basic API.
    text: |-
        az apim nv update --service-name MyApim -g MyResourceGroup --named-value-id MyNamedValue --value foo
"""

helps['apim api operation list'] = """
type: command
short-summary: List a collection of the operations for the specified API.
examples:
  - name: List a collection of the operations for the specified API.
    text: |-
        az apim api operation list --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId
"""

helps['apim api operation show'] = """
type: command
short-summary: Gets the details of the API Operation specified by its identifier.
examples:
  - name: Gets the details of the API Operation specified by its identifier.
    text: |-
        az apim api operation show --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --operation-id MyOperationId
"""

helps['apim api operation create'] = """
type: command
short-summary: Creates a new operation in the API
examples:
  - name: Creates a new operation in the API with several parameters
    text: |-
        az apim api operation create --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --url-template "/session/{param1}/{param2}" --method "GET" --display-name MyOperationName --description MyDescription --template-parameters name=param1 description=descriptionContent type=paramType required="true" --template-parameters name=param2 required="false" type="string"
"""

helps['apim api operation update'] = """
type: command
short-summary: Updates the details of the operation in the API specified by its identifier.
examples:
  - name: Updates method, displayname, description of the operation in the API specified by its identifier.
    text: |-
        az apim api operation update --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --operation-id MyOperationId --method "PUT" --display-name NewDisplayName --description NewDescription
"""

helps['apim api operation delete'] = """
type: command
short-summary: Deletes the specified operation in the API.
examples:
  - name: Deletes the specified operation in the API.
    text: |-
        az apim api operation delete --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --operation-id MyOperationId
"""

helps['apim api release list'] = """
type: command
short-summary: Lists all releases of an API.
examples:
  - name: Lists all releases of an API.
    text: |-
        az apim api release list --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId
"""

helps['apim api release show'] = """
type: command
short-summary: Returns the details of an API release.
examples:
  - name: Returns the details of an API release.
    text: |-
        az apim api release show --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --release-id MyReleaseId
"""

helps['apim api release create'] = """
type: command
short-summary: Creates a new Release for the API.
examples:
  - name: Creates a new Release for the API.
    text: |-
        az apim api release create --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --release-id MyReleaseId --api-revision 2 --notes MyNotes
"""

helps['apim api release update'] = """
type: command
short-summary: Updates the details of the release of the API specified by its identifier.
examples:
  - name: Updates the notes of the release of the API specified by its identifier.
    text: |-
        az apim api release update --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --release-id MyReleaseId --notes MyNewNotes
"""

helps['apim api release delete'] = """
type: command
short-summary: Deletes the specified release in the API.
examples:
  - name: Deletes the specified release in the API.
    text: |-
        az apim api release delete --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --release-id MyReleaseId
"""

helps['apim api revision list'] = """
type: command
short-summary: Lists all revisions of an API.
examples:
  - name: Lists all revisions of an API.
    text: |-
        az apim api revision list --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId
"""

helps['apim api revision create'] = """
type: command
short-summary: Create API revision.
examples:
  - name: Create a revision for the specfic API.
    text: |-
        az apim api revision create --resource-group MyResourceGroup --service-name MyServiceName --api-id MyApiId --api-revision RevisionNumber --api-revision-description RevisionDescription
"""

helps['apim api versionset list'] = """
type: command
short-summary: Lists a collection of API Version Sets in the specified service instance.
examples:
  - name: Lists a collection of API Version Sets in the specified service instance.
    text: |-
        az apim api versionset list --resource-group MyResourceGroup --service-name MyServiceName
"""

helps['apim api versionset show'] = """
type: command
short-summary: Gets the details of the Api Version Set specified by its identifier.
examples:
  - name: Gets the details of the Api Version Set specified by its identifier.
    text: |-
        az apim api versionset show --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId
"""

helps['apim api versionset create'] = """
type: command
short-summary: Creates a Api Version Set.
examples:
  - name: Creates a Api Version Set with version schema as header.
    text: |-
        az apim api versionset create --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId --display-name MyDisplayName --versioning-scheme "Header" --description MyDescription --version-header-name MyHeaderName
  - name: Creates a Api Version Set with version schema as query.
    text: |-
        az apim api versionset create --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId --display-name MyDisplayName --versioning-scheme "Query" --description MyDescription --version-query-name MyQueryName
"""

helps['apim api versionset update'] = """
type: command
short-summary: Updates the details of the Api VersionSet specified by its identifier.
examples:
  - name: Updates the description, display-name of the Api VersionSet specified by its identifier.
    text: |-
        az apim api versionset update --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId --display-name MyNewDisplayName --description MyNewDescription
  - name: Updates the version schema of the Api VersionSet specified by its identifier.
    text: |-
        az apim api versionset update --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId --versioning-scheme "Query" --version-query-name MyNewQueryName
"""

helps['apim api versionset delete'] = """
type: command
short-summary: Deletes specific Api Version Set.
examples:
  - name: Deletes specific Api Version Set.
    text: |-
        az apim api versionset delete --resource-group MyResourceGroup --service-name MyServiceName --version-set-id MyVersionSetId
"""
