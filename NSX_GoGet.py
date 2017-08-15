import NSX_v
import requests
import xml.etree.ElementTree

from requests.auth import HTTPBasicAuth  # Still need to understand why requests.auth.HTTPBasicAuth() is not valid.


def transportzone_oid(NSXManager, tz):
    url = "https://" + NSXManager.address + "/api/2.0/vdn/scopes"
    headers = {"Content-Type": "application/xml"}
    auth = HTTPBasicAuth(NSXManager.user, NSXManager.password)

    print(f"URL: {url}, User: {NSXManager.user}, Pass: {NSXManager.password}")

    r = requests.get(url, headers=headers, auth=auth, verify=False)

    if r.status_code != 200:
        print(f"***ERROR: {r.status_code}")
    else:
        print(f"Text:  {r.text}")

    # Convert XML text from ReST response to ElementTree object so it can be checked
    e = xml.etree.ElementTree.parse(r.text).getroot()

    #Return 'None' if no match during iteration below
    object_id = None

    # Iterate through each vdnScope looking for a match
    for entry in e.iter("vdnScope"):
        if entry.find("name").text == tz:
            print(f"TZ Found: {entry.find('name').text}, Object ID: {entry.find('objectId').text}")
            object_id = entry.find('objectId').text

    return object_id
