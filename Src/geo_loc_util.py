import json
import urllib
import urllib.request
import urllib.parse
from http.client import HTTPResponse
from typing import List
import typer

def main(locations: List[str]):
    try:
        for location in locations:
            if location.isdigit():
                data = get_zip(location)
            else:
                data = get_city_state(location)
            output = "{'name': '" + data['name'] + "','lat':'" + str(data['lat']) + "','lon':'" + str(data['lon']) + "'}"
            print(output)
    except urllib.error.HTTPError as e:
        print(f"Error occurred in processing request:{e}")
    except IndexError:
        print(f"Place not found")


def get_zip(zipCode):
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipCode},US&appid=f897a99d971b5eef57be6fafa0d83239"
    contents = make_http_request(url)
    data = json.loads(contents)
    return data


def get_city_state(cityState):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={urllib.parse.quote(cityState)},US&appid=f897a99d971b5eef57be6fafa0d83239"
    contents = make_http_request(url)
    data = json.loads(contents)
    return data[0]

def make_http_request(url):
    connection = urllib.request.urlopen(url)
    contents = connection.read()
    return contents


if __name__=="__main__":
    typer.run(main)