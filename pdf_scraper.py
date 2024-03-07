import requests
from bs4 import BeautifulSoup

def fetch_pdf_links(url, base_url, title, pdf_links, visited_urls):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        if url in visited_urls:
            return
        visited_urls.add(url)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                full_url = href if href.startswith('http') else base_url.rstrip('/') + '/' + href.lstrip('/')
                if href.endswith('.pdf'):
                    if title not in pdf_links:
                        pdf_links[title] = []
                    pdf_links[title].append(full_url)
                elif href.endswith('/') and not href.startswith('..'):  # Avoid going up in the directory
                    # Extract directory name for title
                    new_title = href.rstrip('/').split('/')[-1]
                    fetch_pdf_links(full_url, full_url, new_title, pdf_links, visited_urls)
    except Exception as e:
        print(f"Error fetching or parsing {url}: {e}")

# Use the complete base URL
base_url = "https://www.un-forum.org/books/library/(digimob)%20Student%20of%20the%20Occult%20Mega-Torrent%20%232.3%20(L%20-%20Z)/"
pdf_links = {}
visited_urls = set()

# Starting from the base_url, the title is the root directory name
fetch_pdf_links(base_url, base_url, "Root Directory", pdf_links, visited_urls)

# Writing the PDF URLs to a text file, sorted by directory
with open('pdf_links_full_collection3.txt', 'w') as file:
    for title, links in pdf_links.items():
        file.write(f"## {title}\n")
        for url in sorted(links):
            file.write(f"{url}\n")
        file.write("\n")  # Add a newline for better separation

print(f"PDF URLs have been collected and sorted by directories. Total directories found: {len(pdf_links)}")
