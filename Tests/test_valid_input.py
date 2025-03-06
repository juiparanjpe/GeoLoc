import json
import subprocess
import csv
from json import JSONDecodeError

geo_loc_util = "Src/geo_loc_util.py"

def test_single_zip_code():
    process1 = subprocess.run(["python3",geo_loc_util, "94566"], stdout=subprocess.PIPE)
    assert process1.returncode == 0
    std_out = process1.stdout
    #format output in json and validate it's same as expected json format
    json_formatted_output = json.loads(std_out)
    json_formatted_output = json.dumps(json_formatted_output)
    expected_json = get_json_formatted("Pleasanton",37.6658, -121.8755)
    assert json_formatted_output == expected_json

def test_single_city_state():
    process1 = subprocess.run(["python3",geo_loc_util, "san francisco, ca"], stdout=subprocess.PIPE)
    assert process1.returncode == 0
    std_out = process1.stdout
    # format output in json and validate it's same as expected json format
    json_formatted_output = json.loads(std_out)
    json_formatted_output = json.dumps(json_formatted_output)
    expected_json = get_json_formatted("San Francisco", 37.7790262, -122.419906)
    assert json_formatted_output == expected_json
    #assert process1.stdout.decode("utf-8").strip() == "{'name': 'San Francisco','lat':'37.7790262','lon':'-122.419906'}"

def test_multi_inputs():
    process1 = subprocess.run(["python3",geo_loc_util, "Madison,WI", "53072"], stdout=subprocess.PIPE)
    assert process1.returncode == 0
    std_out_str = process1.stdout.decode("utf-8")
    out_str = std_out_str.split("}")
    # format output in json and validate it's same as expected json format
    json_formatted_output1 = json.loads(out_str[0] + "}")
    json_formatted_output1 = json.dumps(json_formatted_output1)
    json_formatted_output2 = json.loads(out_str[1] + "}")
    json_formatted_output2 = json.dumps(json_formatted_output2)
    #format both expected jsons and assert
    expected_json1 = get_json_formatted("Madison",43.074761,-89.3837613)
    expected_json2 = get_json_formatted("Village of Pewaukee",43.0788,-88.2729)
    assert expected_json1 in json_formatted_output1
    assert expected_json2 in json_formatted_output2

def test_from_testdata():
    file = open("Tests/testData.txt", 'r')
    csv_reader = csv.reader(file, delimiter='|')
    input_col = [0]
    #for each row, send the input and verify against expected city, latitude and longitude
    for row in csv_reader:
        input_to_feed = list(row[i] for i in input_col)
        expected_output = get_json_formatted(row[1],row[2],row[3])
        process1 = subprocess.run(["python3", geo_loc_util, input_to_feed[0]], stdout=subprocess.PIPE)
        assert process1.returncode == 0
        json_formatted_output = json.loads(process1.stdout)
        json_formatted_output = json.dumps(json_formatted_output)
        assert json_formatted_output == expected_output

def get_json_formatted(place, lat, lon):
    expected_object = {
        "name": place,
        "lat": float(lat),
        "lon": float(lon)
    }
    json_formatted = json.dumps(expected_object)
    return json_formatted
