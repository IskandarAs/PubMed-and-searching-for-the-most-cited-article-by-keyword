import requests
from bs4 import BeautifulSoup

# Define the search query and the number of articles to consider
query = 'machine_learning'
num_articles = 500

# Create the PubMed URL
url = 'https://pubmed.ncbi.nlm.nih.gov/?term=' + query

# Send a request to the URL
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the PubMed IDs of the top articles
pmids = [i.get('data-article-id') for i in soup.find_all('a', {'class': 'docsum-title'}, href=True)][:num_articles]

# Extract the citation count of each article
citations = []
for pmid in pmids:
    article_url = 'https://pubmed.ncbi.nlm.nih.gov/' + pmid
    article_response = requests.get(article_url)
    article_soup = BeautifulSoup(article_response.content, 'html.parser')
    citation_count = article_soup.find('span', {'class': 'cit'}).text
    citations.append(int(citation_count.split()[0]))

# Find the index of the most-cited article
most_cited_index = citations.index(max(citations))

# Print the title and citation count of the most-cited article
most_cited_article_url = 'https://pubmed.ncbi.nlm.nih.gov/' + pmids[most_cited_index]
most_cited_article_response = requests.get(most_cited_article_url)
most_cited_article_soup = BeautifulSoup(most_cited_article_response.content, 'html.parser')
most_cited_article_title = most_cited_article_soup.find('h1', {'class': 'heading-title'}).text
most_cited_article_citations = citations[most_cited_index]
print(f'Most-cited article: {most_cited_article_title}\nCitation count: {most_cited_article_citations}')
