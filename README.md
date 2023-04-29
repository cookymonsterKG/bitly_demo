# Bitly Backend Engineer - Coding Challenge

This repository contains a Python 3 solution to the Bitly Backend Engineer coding challenge. The program calculates the number of clicks from 2021 for each record in the `encodes.csv` dataset, using the provided `decodes.json` file.

## Dependencies

This project uses Python 3.11 and does not require any external dependencies. All the libraries used in the solution are part of the Python Standard Library. The following built-in libraries are used:

- `csv`
- `json`
- `collections`
- `datetime`

Make sure that your Python version is `3.11` or above

## Running the Application

To run the script, make sure you have Python 3 installed on your system. Then, run the script with the following command:

```sh
python3 index.py
```

The script will output a sorted array of JSON objects containing the long URL as the key and the click count as the value.

## Running the Unit tests
```sh
python3 test.py
```
## Design Decisions

1. The solution was developed using Python 3 due to its ease of use, readability, and built-in libraries for handling CSV and JSON files, as well as datetime operations.

2. The program is designed with separate functions for each step in the process:
   - Reading the `encodes.csv` and `decodes.json` files
   - Filtering records in `decodes.json` by year
   - Calculating clicks for each long URL

   This modular approach promotes code readability, maintainability, and testability.

3. The program filters decodes by year using the `datetime.fromisoformat()` function, which parses ISO 8601 formatted timestamp strings. This is chosen based on the fact that all `timestamp` in `decodes.json` file are in this format '2020-06-20T00:00:00Z'. 

4. Unit tests are implemented using Python's built-in `unittest` framework to ensure the proper functioning of each individual function.

---
