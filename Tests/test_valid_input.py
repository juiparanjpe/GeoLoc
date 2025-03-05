import subprocess
import csv

geo_loc_util = "Src/geo_loc_util.py"

def test_single_zip_code():
    process1 = subprocess.run(["python3",geo_loc_util, "94566"], capture_output=True)
    assert process1.returncode == 0
    assert process1.stdout.decode("utf-8").strip() == "{'name': 'Pleasanton','lat':'37.6658','lon':'-121.8755'}"

def test_single_city_state():
    process1 = subprocess.run(["python3",geo_loc_util, "san francisco, ca"], capture_output=True)
    assert process1.returncode == 0
    assert process1.stdout.decode("utf-8").strip() == "{'name': 'San Francisco','lat':'37.7790262','lon':'-122.419906'}"

def test_multi_inputs():
    process1 = subprocess.run(["python3",geo_loc_util, "fremont,ca", "94566"], capture_output=True)
    assert process1.returncode == 0
    assert process1.stdout.decode("utf-8").strip() == "{'name': 'Fremont','lat':'37.5482697','lon':'-121.988571'}\r\n{'name': 'Pleasanton','lat':'37.6658','lon':'-121.8755'}"

def test_from_testdata():
    file = open("Tests/testData.txt", 'r')
    csv_reader = csv.reader(file, delimiter='|')
    input_cols = [0]
    output_cols = [1]
    for row in csv_reader:
        input_to_feed = list(row[i] for i in input_cols)
        expected_output = list(row[i] for i in output_cols)
        process1 = subprocess.run(["python3", geo_loc_util, input_to_feed[0]], capture_output=True)
        assert process1.returncode == 0
        assert process1.stdout.decode("utf-8").strip() == expected_output[0]

