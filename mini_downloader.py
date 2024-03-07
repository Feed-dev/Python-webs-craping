import requests

# Path to the scroll where the URLs of the tomes are enscribed
scroll_path = 'pdf_links_alchemy.txt'

# Disguise our request with headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Read each URL from the scroll and summon the respective tome
with open(scroll_path, 'r') as scroll:
    for url in scroll.readlines():
        url = url.strip()  # Remove any extraneous whitespace
        file_name = url.split('/')[-1]  # Extract the tome's name from its URL

        # Invoke the mystical powers of the requests library to fetch the content, with our disguise
        response = requests.get(url, headers=headers)

        # Check if the spell was successful
        if response.status_code == 200:
            # Specify the local abode for the summoned PDF
            file_path = f'downloaded_tomes/Alchemy/{file_name}'  # Adjust path as necessary

            # Open a portal (file) and inscribe the PDF content within
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f'The tome "{file_name}" has been successfully ensconced at {file_path}.')
        else:
            print(f'Alas! The spell failed for "{file_name}". The tome could not be summoned.')
