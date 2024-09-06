import json

#loading the spec file
def load_spec(file_path):
    with open(file_path, 'r') as f:
        spec = json.load(f)
    column_names = spec['ColumnNames']
    offsets = list(map(int, spec['Offsets']))
    fixed_width_encoding = spec['FixedWidthEncoding']
    include_header = spec['IncludeHeader'].lower() == 'true'
    delimited_encoding = spec['DelimitedEncoding']
    return column_names, offsets, fixed_width_encoding, include_header, delimited_encoding



# Call the function with a properly formatted file path
spec_file_path = r'C:\Users\rajes\Downloads\google_data\DE challenge\Fixed_width_file\spec.json'
column_names, offsets, fixed_width_encoding, include_header, delimited_encoding = load_spec(spec_file_path)
print("loded_spec:",load_spec(spec_file_path))


#Generate fixed widht file using
def generate_fixed_width_file(data, offsets, output_file, encoding):
    with open(output_file, 'w', encoding=encoding) as f:
        for row in data:
            fixed_width_row = ''.join(f'{str(field):<{length}}'[:length] for field, length in zip(row, offsets))
            f.write(fixed_width_row + '\n')


data = [
    ['John', 'Doe', '12345', 'NY', 'Engineer', '10000', 'john.doe@example.com', '1234567890', 'Address Line 1', 'Company ABC'],
    ['Jane', 'Smith', '67890', 'LA', 'Manager', '20000', 'jane.smith@example.com', '0987654321', 'Address Line 2', 'Company XYZ']
]


# Offsets: The lengths of each column
offsets = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]  # Example offsets from your spec.json

# Output file path
output_file = r'C:\Users\rajes\Downloads\google_data\DE challenge\Fixed_width_file\fixed_width_output.txt'
# Encoding: For example, use "windows-1252" as mentioned in the spec
encoding = "windows-1252"


# Call the function
generate_fixed_width_file(data, offsets, output_file, encoding)
print("Here")
print(generate_fixed_width_file)



import csv
def parse_fixed_width_file(input_file, output_file, column_names, offsets, fixed_width_encoding, include_header, delimited_encoding):
    with open(input_file, 'r', encoding=fixed_width_encoding) as infile, open(output_file, 'w', newline='', encoding=delimited_encoding) as outfile:
        writer = csv.writer(outfile)
        
        if include_header:
            writer.writerow(column_names)
        
        for line in infile:
            start = 0
            row = []
            for length in offsets:
                row.append(line[start:start + length].strip())
                start += length
            writer.writerow(row)


# Define the input and output file paths
input_file = r'C:\Users\rajes\Downloads\google_data\DE challenge\Fixed_width_file\fixed_width_output.txt'
output_file = r'C:\Users\rajes\Downloads\google_data\DE challenge\Fixed_width_file\csv_output.csv'

# Call the function
parse_fixed_width_file(input_file, output_file, column_names, offsets, fixed_width_encoding, include_header, delimited_encoding)






