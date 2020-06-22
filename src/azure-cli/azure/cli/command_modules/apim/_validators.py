# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def validate_policy_xml_content(xml_content):
    """Validates that the xml content has been set"""
    if len(xml_content) == 0:
        raise CLIError('The XML is required for creating or updating an API Management service policy')