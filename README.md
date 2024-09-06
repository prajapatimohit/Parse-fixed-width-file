# Fixed-Width File Parser

This project contains a Python script that parses a fixed-width file and generates a delimited file (like CSV) based on a given spec. The spec file contains details about the length of each field in the fixed-width file.

## Features
- **Parsing**: Handles fixed-width file parsing using field lengths provided in the spec.
- **Output**: Generates a delimited file (e.g., CSV).
- **Encoding**: Supports custom encoding as per spec.
- **Bonus**: Docker container provided for easy execution.

## How to Run

### Prerequisites
- Python 3.x
- (Optional) Docker, if you want to run the solution inside a container.

##### Running the Script

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fixed-width-parser.git
   cd fixed-width-parser

