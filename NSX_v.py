"""
Module:     NSX_v.py
Author:     Luis Chanu
Date:       8/13/2017
Target:     NSX for vSphere v6.x

Description:
    As an attempt to better learn Python, I'm creating this NSX Class file.  The primary goal of this
    file is to create a set of basic NSX Classes which I can use to create simple NSX automation scripts
    from.  The secondary goal is to aid in the creation of automating various NSX actions.

"""

import requests
import NSX_GoGet

from requests.auth import HTTPDigestAuth


class NSXManager:
    address = ""
    user = ""
    password = ""

    def __init__(self, nsx_manager_address, admin_user, admin_password):
        self.address = nsx_manager_address
        self.user = admin_user
        self.password = admin_password


class LogicalSwitch:
    name = ""
    description = ""
    tenantId = ""
    controlPlaneMode = ""


    def __init__(self, LS_name, LS_description, LS_tenantId, LS_controlPlaneMode):
        name = LS_name
        description = LS_description
        tenantId = LS_tenantId
        controlPlaneMode = LS_controlPlaneMode



'''
def convert_keys_to_nsx_fields(nsx):
"""
This function replaces the "User Friendly" header fields, used as Keys within the Dict, to the expected NSX fields in
the ReST API calls.  By doing the conversion here, we don't have to worry about mapping them later during the API,
and we can just iterate through the objects and create them.
"""

mapping = {
    "LS": [
        ""
    ]
}
'''
