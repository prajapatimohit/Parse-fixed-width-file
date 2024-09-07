# Fixed-Width File Parser

This project contains a Python solution for parsing a fixed-width file using a JSON specification and converting it into a delimited file format (e.g., CSV). The project includes functions to load the specification, generate a fixed-width file, and parse the file into a delimited format.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Project Overview
The goal of this project is to:
- Load a fixed-width file specification (column names, offsets, encodings, etc.) from a JSON file.
- Use the specification to generate and parse fixed-width files.
- Convert the fixed-width files to a delimited file format, such as CSV, while preserving data accuracy.

## Prerequisites
Before running this project, make sure you have the following:
- Python 3.7 or higher
- `json` and `csv` libraries (these are part of Python's standard library)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/fixed-width-parser.git
   ```

2. Navigate to the project directory:
   ```bash
   cd fixed-width-parser
   ```

3. Install any required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Load the specification file:**

   Update the file path for the `spec.json` file inside the script to match your local path.

   ```python
   spec_file_path = r'path_to_your_json_file'
   ```

2. **Generate a fixed-width file:**

   You can generate a fixed-width file from data using the `generate_fixed_width_file` function:
   ```python
   generate_fixed_width_file(data, offsets, output_file, encoding)
   ```

3. **Parse a fixed-width file to CSV:**

   Convert the fixed-width file into a delimited format using the `parse_fixed_width_file` function:
   ```python
   parse_fixed_width_file(input_file, output_file, column_names, offsets, fixed_width_encoding, include_header, delimited_encoding)
   ```

4. Update the file paths in the script where necessary to point to your fixed-width and CSV output files.

## Project Structure
- `spec.json`: Contains the column names, offsets, encodings, and settings for parsing the fixed-width file.
- `fixed_width_parser.py`: The main script that loads the spec file, generates a fixed-width file, and parses the file to a CSV.
- `requirements.txt`: Lists any additional libraries (if needed).

## Example
You can find an example of the `spec.json` file below:

```json
{
    "ColumnNames": ["FirstName", "LastName", "ID", "State", "JobTitle", "Salary", "Email", "PhoneNumber", "Address", "Company"],
    "Offsets": [5, 12, 3, 2, 13, 7, 10, 13, 20, 13],
    "FixedWidthEncoding": "windows-1252",
    "IncludeHeader": "True",
    "DelimitedEncoding": "utf-8"
}
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
