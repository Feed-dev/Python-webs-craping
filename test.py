import requests

# The headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Test the subdirectory with headers
subdirectory_url = ''
response_subdirectory = requests.get(subdirectory_url, headers=headers)
print(f"Access to subdirectory with headers: {'Successful' if response_subdirectory.status_code == 200 else 'Failed'}")

# Test the direct PDF link with headers
pdf_url = ''
response_pdf = requests.get(pdf_url, headers=headers)
print(f"Access to direct PDF with headers: {'Successful' if response_pdf.status_code == 200 else 'Failed'}")

