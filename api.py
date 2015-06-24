import urllib
import urllib2
import json


BASE_URL = "http://www.refugerestrooms.org/api"

def searchForRestroom(query):
    qs = {'query': query}
    url = BASE_URL + "/v1/restrooms/search.json?" + urllib.urlencode(qs)
    response = urllib2.urlopen(url).read()
    return json.loads(response)
