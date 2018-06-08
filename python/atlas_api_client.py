import requests

api_user = "admin"
api_password = "admin"
api_endpoint = "http://atlas.dev.gdpdentsu.com:21000"


def get_all_for_type(type_name):
    path = "/api/atlas/v2/search/dsl"
    query = "?typeName={}".format(type_name)
    try:
        response = requests.get(api_endpoint+path+query, auth=(api_user, api_password))
        return response.json()['entities']
    except Exception as e:
        print(e)


def get_single_entity_details(type_name,
                              entity_name
                              ):
    path = "/api/atlas/v2/search/dsl"
    query = "?typeName={}&query=where%20name%3D%22{}%22".format(type_name, entity_name)
    try:
        response = requests.get(api_endpoint+path+query, auth=(api_user, api_password))
        return response.json()['entities'][0]
    except Exception as e:
        print(e)

classification_type_name = "PII"
attributes = {
    "Date added": "2018-06-17T23:20:50.52Z"
}
guids = ["a3dedac5-e445-41a9-8baf-c1fd96aec451"]


def add_tag(guids: list,
            classification_type_name: str,
            attributes: dict):
    data_dict = {
                      "classification": {
                        "typeName": classification_type_name,
                        "attributes": attributes
                      },
                      "entityGuids": guids
                }
    path = "/api/atlas/v2/entity/bulk/classification"

    try:
        response = requests.post(api_endpoint+path, auth=(api_user, api_password), json=data_dict)
        return response
    except Exception as e:
        print(e)


out3 =  add_tag(guids=guids,
        classification_type_name=classification_type_name,
        attributes=attributes)

print()
# json_data = json.loads(json_str)

# out = get_all_for_type("hive_table")
# out2 = get_single_entity_details("hive_table", "my_agg12")

# print(out2['guid'])
# out = requests.get(api_endpoint, auth=(api_user, api_password))
