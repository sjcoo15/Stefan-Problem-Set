from generate_timestamp import generate_timestamp

def read_timestamp():
    try:
        with open('timestamp.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('The file timestamp.txt does not exist.')

# Generate a new timestamp before reading
generate_timestamp()

# Read and display the content of the timestamp file
read_timestamp()
