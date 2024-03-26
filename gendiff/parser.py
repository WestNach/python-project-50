import argparse


# Function to parse command line arguments
def parse():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        # Provide a description of the script
        description='Generate difference between two files')

    # Add arguments to the parser
    parser.add_argument('path1', help='path to the first file')
    parser.add_argument('path2', help='path to the second file')

    # Add optional argument with format choices
    parser.add_argument('-f', '--format', choices=['plain', 'stylish', 'json'],
                        # Set the default format as 'stylish'
                        default='stylish',
                        # Provide a help message for the --format argument
                        help='output format (default: stylish)')

    # Parse the arguments and return them as an object
    args = parser.parse_args()
    return args
