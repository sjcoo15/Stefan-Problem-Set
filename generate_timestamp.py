import datetime

# Function to generate and save a timestamp
def generate_timestamp():
    current_time = datetime.datetime.now()
    with open('timestamp.txt', 'a') as file:
        file.write(f'Timestamp: {current_time}\\n')

# Call the function to generate a timestamp
generate_timestamp()
