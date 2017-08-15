import NSX_v
import requests
import xmltodict
from requests.auth import HTTPBasicAuth  # Still need to understand why requests.auth.HTTPBasicAuth() is not valid.


def transportzone_oid(NSXManager, tz):
    url = "https://" + NSXManager.address + "/api/2.0/vdn/scopes"
    headers = {"Content-Type": "application/xml"}
    auth = HTTPBasicAuth(NSXManager.user, NSXManager.password)

    print("URL: {}".format(url))

    r = requests.get(url, headers=headers, auth=auth, verify=False)

    if r.status_code != 200:
        print(f"***ERROR: {r.status_code}")
    else:
        print(f"Text:  {r.text}")

    # ToDo: Need to figure out how to use xmltodict to convert the r.text xml output to dict so key can be querried.
    object_id = r.text

    return object_id[tz]
