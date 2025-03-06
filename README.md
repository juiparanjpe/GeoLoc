# GeoLoc Utility
## Installing dependencies
Install uv, then run

```uv sync```

or use pyproject.toml to install dependencies

## Running the GeoLoc utility program
Run the command to get location details by zip code

```python3 Src/geo_loc_util.py "53072"```

Run the command to get location details by city,state

```python3 Src/geo_loc_util.py "Milwaukee,WI"```

You can give multiple arguments to the program like this

```python3 Src/geo_loc_util.py "94566" "Minneapolis,MN" "Seattle,WA"```

## Running the tests
Run command

```pytest```

Note that the "test_from_testdata" is a data driven test. 
You may add more test data to the testData.txt and verify.