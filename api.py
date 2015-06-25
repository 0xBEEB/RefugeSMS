import urllib
from urllib2 import urlopen, HTTPError
import json


GOOG_URI = 'http://maps.googleapis.com/maps/api/geocode/json?'
BASE_URL = "http://www.refugerestrooms.org/api"

def getLatLong(address):
    """
    getLatLong

    Returns a dictionary of the lat long corresponding to the given address

    :param:     address str
    :return:    latlong dict
    """
    if ("portland" not in address.lower() or
        "beaverton" not in address.lower() or
        "gresham" not in address.lower()):
        address += " Portland Oregon"

    url = "%saddress=%s&sensor=false" % (GOOG_URI, "+".join(address.split()))

    try:
        f = urlopen(url)
    except HTTPError:
        return None

    response = f.read()

    data = json.loads(response)

    try:
        return data['results'][0]['geometry']['location']
    except IndexError:
        return None


def searchForRestroom(query):
    latlng = getLatLong(query)
    url = BASE_URL + "/v1/restrooms/by_location.json?" + urllib.urlencode(latlng)
    response = urlopen(url).read()

    return json.loads(response)
