# bookapp/views.py
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re


def book_list(request):
    url = "https://www.goodreads.com/search?utf8=%E2%9C%93&query=shakespear"
    books = []

    # Scraping data from the first to the fifth page
    for page_number in range(1, 6):
        response = requests.get(url + str(page_number))
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information from each book element
        for book_element in soup.find_all('tr', {'itemtype': 'http://schema.org/Book'}):
            title = book_element.find('span', {'itemprop': 'name'}).text.strip()
            author = book_element.find('span', {'itemprop': 'author'}).find('span', {'itemprop': 'name'}).text.strip()
            rating = book_element.find('span', {'class': 'minirating'}).text.strip()

            # Extracting published date and number of editions
            info_span = book_element.find('span', {'class': 'greyText smallText uitext'})

            # Extract published date using regular expressions
            published_text = info_span.get_text(strip=True)
            published_match = re.search(r'published (\d{4})', published_text)

            
            published_date = published_match.group(1) if published_match else 'N/A'
            num_editions = info_span.find('a', {'class': 'greyText'}).text.strip().split()[0]

            
            # Add the extracted information to the list
            books.append({
                'title': title,
                'author': author,
                'rating': rating,
                'published_date': published_date,
                'num_editions': num_editions,
            })

    return render(request, 'bookapp/book_list.html', {'books': books})
