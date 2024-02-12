```markdown
# Django Book List Project

This Django project fetches book information from the Goodreads website using web scraping and displays the data in a clean and styled format. The project includes a simple Django app named `bookapp`.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python (version 3.x)
- Django
- BeautifulSoup4
- Requests

### Installing Dependencies

Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

### Running the Project

1. Run database migrations:

    ```bash
    python manage.py migrate
    ```

2. Start the development server:

    ```bash
    python manage.py runserver
    ```

3. Open your web browser and visit [http://localhost:8000/bookapp/book_list/](http://localhost:8000/bookapp/book_list/) to view the book list.

## Project Structure

- **bookapp**: Django app for handling book-related functionality.
    - `views.py`: Contains the view function to fetch and display book data.
    - `templates/bookapp/book_list.html`: HTML template for rendering the book list.

- **Requirements**: The `requirements.txt` file lists the project dependencies.

- **Web Scraping**: The project uses web scraping techniques to fetch book information from the Goodreads website.

- **Styling**: The `book_list.html` template includes simple CSS styles for a clean and readable display.

## Acknowledgments

- Goodreads for providing the platform to fetch book data.