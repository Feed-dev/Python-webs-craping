import requests
import os

# Path to the scroll where the URLs of the tomes are enscribed
scroll_path = 'pdf_links_full_collection3.txt'

# The grand archive where all sections and tomes will be stored
archive_path = 'Great_Library_L-Z/'

# Disguise our request with headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Initiate the mapping of sections to their respective abodes
current_section = ''

# Read each URL from the scroll and summon the respective tome
with open(scroll_path, 'r') as scroll:
    for line in scroll:
        line = line.strip()  # Trim any leading/trailing whitespace

        # Detect if the line is a section title
        if line.startswith('##'):
            # Update the current section, replacing unwanted characters and spaces
            current_section = line[3:].replace('%20', ' ').replace('/', '_').replace('\\', '_')
            # Create a new directory for this section within the grand archive
            os.makedirs(os.path.join(archive_path, current_section), exist_ok=True)
            continue

        # Check if we are within a section and have a URL to process
        if current_section and line.startswith('http'):
            url = line
            file_name = url.split('/')[-1].replace('%20', ' ')  # Extract and clean the tome's name
            file_path = os.path.join(archive_path, current_section, file_name)  # Path for the tome

            # Invoke the mystical powers of the requests library to fetch the content, with our disguise
            response = requests.get(url, headers=headers)

            # Check if the spell was successful
            if response.status_code == 200:
                # Open a portal (file) and inscribe the PDF content within
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f'The tome "{file_name}" has been successfully ensconced at {file_path}.')
            else:
                print(f'Alas! The spell failed for "{file_name}". The tome could not be summoned.')
