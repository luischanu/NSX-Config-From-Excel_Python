"""
Still ToDo Items:
1) Convert over to logging module instead of print statements
2) Handle exceptions
"""

import NSX_v
import requests
import xml.etree.ElementTree

from requests.auth import HTTPBasicAuth  # Still need to understand why requests.auth.HTTPBasicAuth() is not valid.

from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable Untrusted SSL Certificate Warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def transportzone_oid(NSXManager, tz):
    url = "https://" + NSXManager.address + "/api/2.0/vdn/scopes"
    headers = {"Content-Type": "application/xml"}
    basicauth = HTTPBasicAuth(NSXManager.user, NSXManager.password)

    print(f"URL: {url}, User: {NSXManager.user}, Pass: {NSXManager.password}")

    print("*** Before Request ***")
    r = requests.get(url, headers=headers, auth=basicauth, verify=False)
    print("*** After Request ***")

    if r.status_code != 200:
        print(f"***ERROR: {r.status_code}")
    else:
        print(f"Text:  {r.text}")

    # Convert XML text from ReST response to ElementTree object so it can be checked
    e = xml.etree.ElementTree.fromstring(r.content)

    print("*** After ElementTree ***")

    # Return 'None' if no match during iteration below
    object_id = None

    # Iterate through each vdnScope looking for a match
    for entry in e.iter("vdnScope"):
        print(f"Iter={entry.find('name').text},  tz={tz}")
        if entry.find("name").text == tz:
            print(f"TZ Found: {entry.find('name').text}, Object ID: {entry.find('objectId').text}")
            object_id = entry.find('objectId').text

    return object_id
