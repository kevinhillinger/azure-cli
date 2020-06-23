# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def get_xml_content(xml, xml_path, xml_uri):
    """Gets the XML content for policies based on the 3 options that a user can provide, with inline taking precedentsm, then file, then uri"""
    xml_content = xml
    if xml_content is None:
        if xml_path is not None:
            xml_content = read_file(xml_path)
        else:
            xml_content = xml_uri
    return xml_content


def read_file(file_path):
    import os
    with open(os.path.realpath(os.path.expanduser(file_path)), 'r') as fs:
        content = fs.read()
        return content