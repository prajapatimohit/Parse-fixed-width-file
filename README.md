# CSV Anonymizer

## Description

This project consists of a Python script that reads a CSV file, anonymizes specific fields (first name, last name, and address) using SHA-256 hashing, and writes the anonymized data to a new CSV file. The script is designed to handle large datasets by processing the file in chunks.

## Features

- Reads a large CSV file in chunks to handle large datasets efficiently.
- Anonymizes specified fields using SHA-256 hashing.
- Writes the anonymized data to a new CSV file.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```

3. Install any necessary packages (if any):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Modify the file paths in `your_script.py`:
    ```python
    input_file = r'C:\path\to\your\input.csv'
    output_file = r'C:\path\to\your\output.csv'
    ```

2. Run the script:
    ```bash
    python your_script.py
    ```

## Example

To anonymize the data in `large_data.csv` and save the output to `anonymised_data.csv`, set the paths in the script accordingly and run it.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
