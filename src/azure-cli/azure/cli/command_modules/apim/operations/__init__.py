# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.command_modules.apim.operations.api import ApiOperations
from azure.cli.command_modules.apim.operations.api_policy import ApiPolicyOperations
from azure.cli.command_modules.apim.operations.named_value import NamedValueOperations
from azure.cli.command_modules.apim.operations.policy import PolicyOperations
from azure.cli.command_modules.apim.operations.product import ProductOperations
from azure.cli.command_modules.apim.operations.subscription import SubscriptionOperations


class ApimSubgroupsLoader():
    operations = ['api', 'api_policy', 'named_value', 'policy', 'product', 'subscription']

    def __init__(self, commands_loader):
        self.commands_loader = commands_loader

        self.api = ApiOperations(self)
        self.api_policy = ApiPolicyOperations(self)
        self.named_value = NamedValueOperations(self)
        self.policy = PolicyOperations(self)
        self.product = ProductOperations(self)
        self.subscription = SubscriptionOperations(self)

    def load_arguments(self, _):
        for operation in self.operations:
            getattr(self, operation).load_arguments(_)

    def load_command_table(self, _):
        for operation in self.operations:
            getattr(self, operation).load_command_table(_)
