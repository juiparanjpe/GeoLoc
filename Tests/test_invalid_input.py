import subprocess

def test_http_error_zipcode():
    process1 = subprocess.run(["python3","Src/geo_loc_util.py", "00000"], capture_output=True)
    assert process1.returncode == 1
    assert "HTTP Error" in process1.stdout.decode("utf-8").strip()

def test_city_state_not_found():
    process1 = subprocess.run(["python3","Src/geo_loc_util.py", "city,zz" "madison.wi"], capture_output=True)
    assert process1.returncode == 1
    assert "not found" in process1.stdout.decode("utf-8").strip()

def test_missing_arguments():
    process1 = subprocess.run(["python3","Src/geo_loc_util.py"], capture_output=True)
    assert process1.returncode == 2