
from pprint import pprint

import requests




headers = {"Authorization": "Bearer e242964eff94e47874066ab1af533a0d4238f92a01362e33706cf12b4faa3f08",
           "cache-control": "no-cache"}
url = 'https://api.smartlook.cloud'


# get information about all visitors
#request_events = requests.post(url + '/api/v1/visitors/search', headers=headers, json={"filters": []})
#pprint(request_events.json())


# function add values of resource (events, sessions of visitor...) to list
# also makes another request to get more values, if there are any
def get_resource(list, request,resource ):
    for key, value in request.json().items():
        if key == resource:
            for event in value:
                list.append(event)
        if key == "_links":
            try:
                get_resource(list, requests.get(url + value["nextPage"], headers=headers), resource)
            except:
                pass


request_events = requests.get(url + '/api/v1/events', headers=headers)
list_events = []
get_resource(list_events, request_events, "events")


request_sessions =  requests.get(url + '/api/v1/visitors/Wr04Emgfx8/sessions', headers=headers)
list_sessions = []
get_resource(list_sessions, request_sessions, "sessions")



