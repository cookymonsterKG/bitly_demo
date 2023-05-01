# Bitly Backend Engineer - Coding Challenge

This repository contains a Python 3 solution to the Bitly Backend Engineer coding challenge. The program calculates the number of clicks from 2021 for each record in the `encodes.csv` dataset, using the provided `decodes.json` file.

## Dependencies

This project uses Python 3.11 and does not require any external dependencies. All the libraries used in the solution are part of the Python Standard Library. The following built-in libraries are used:

- `csv`
- `json`
- `typing`
- `datetime`

Make sure that your Python version is `3.11` or above

## Docker Alternative
If you have Docker installed on your host machine, you can use the `Dockerfile` provided in this repository to build and run the application in a Docker container. To do so, follow these steps:

1. Make sure that the Docker daemon is running on your host machine.

2. Open a terminal window and navigate to the repository directory.

3. Build a new Docker image from the `Dockerfile` by running the following command:

   ```
   docker build -t bitly_demo .
   ```

   This will create a new Docker image with the name `bitly_demo` based on the instructions in the `Dockerfile`.

4. Run the Docker container by executing the following command:

   ```
   docker run -it --rm bitly_demo
   ```

   This will start a new Docker container from the `bitly_demo` image and run the application inside the container.

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
