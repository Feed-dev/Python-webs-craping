import requests
from bs4 import BeautifulSoup

def fetch_pdf_links(url, base_url="https://www.un-forum.org/books/library/(digimob)%20Student%20of%20the%20Occult%20Mega-Torrent%20%232.1%20(A%20-%20G)/Alchemy/"):
    pdf_links = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                # Ensure the href is concatenated correctly depending on whether it's an absolute or relative URL
                full_url = href if href.startswith('http') else base_url.rstrip('/') + '/' + href.lstrip('/')
                if href.endswith('.pdf'):
                    pdf_links.append(full_url)
                elif href.endswith('/') and not href.startswith('..'):  # Avoid going up in the directory
                    # Pass the full_url as the new base_url for recursive calls
                    pdf_links += fetch_pdf_links(full_url, full_url)
    except Exception as e:
        print(f"Error fetching or parsing {url}: {e}")
    return pdf_links

# Use the complete base URL including the directory for starting URL
starting_url = "https://www.un-forum.org/books/library/(digimob)%20Student%20of%20the%20Occult%20Mega-Torrent%20%232.1%20(A%20-%20G)/Alchemy/"
pdf_urls = fetch_pdf_links(starting_url, starting_url)

# Writing the PDF URLs to a text file
with open('pdf_links_alchemy.txt', 'w') as file:
    for url in pdf_urls:
        file.write("%s\n" % url)

print(f"PDF URLs have been collected and saved to pdf_links_corrected.txt. Total PDFs found: {len(pdf_urls)}")

