# PubMed-and-searching-for-the-most-cited-article-by-keyword
![test](/img/abstract.png)

## About this project
This Python code is designed to extract data from `PubMed`, a popular online database for scientific articles, and search for the most cited article based on a given keyword. The code uses the requests library to send HTTP requests and retrieve HTML content from `PubMed`, and the BeautifulSoup library to parse the HTML content and extract relevant information.

How to use the code
* Install the necessary libraries: Make sure you have the requests and beautifulsoup4 libraries installed in your Python environment. You can install them using pip or conda by running the following commands:

pip install requests
pip install beautifulsoup4

* Set the search query and number of articles to consider: Modify the query variable to specify the keyword you want to search for in PubMed. You can also adjust the num_articles variable to specify the number of top articles you want to consider in the search results.

* Run the code: Once you have set the search query and number of articles to consider, you can run the code. It sends a request to PubMed with the specified search query, retrieves the HTML content of the search results page, and parses it using BeautifulSoup.

* Extract PubMed IDs and citation counts: The code extracts the PubMed IDs (PMIDs) of the top articles from the search results page using BeautifulSoup. It then sends requests to retrieve the HTML content of each article page, parses it using BeautifulSoup, and extracts the citation count of each article. The citation counts are stored in a list called citations.

* Find the most cited article: The code finds the index of the most cited article in the citations list using the index() function. It then uses the index to retrieve the PubMed ID, title, and citation count of the most cited article.

* Print the results: Finally, the code prints the title and citation count of the most cited article.

## Note:
The script assumes that the most cited article has a 'span' element with the class 'cit' that contains the citation count. If the structure of the PubMed website changes, the script may need to be updated accordingly.

I hope you find this script useful for extracting data from PubMed and searching for the most cited article by keyword!
