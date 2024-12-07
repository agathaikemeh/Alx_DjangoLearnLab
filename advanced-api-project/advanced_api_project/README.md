#Django Books API
This is a Django REST framework-based API for managing books. It provides endpoints for listing, retrieving, creating, updating, and deleting books. Authenticated users can manage book data, while unauthenticated users have read-only access.

Features
List all books.
Retrieve details of a specific book by ID.
Create a new book (requires authentication).
Update an existing book (requires authentication).
Delete a book (requires authentication).


API Endpoints
Method	Endpoint	             Description	                         Auth Required
GET	    /books/	                 List all books.	                          No
GET	    /books/<int:pk>/	     Retrieve details of a specific book.	      No
POST	/books/add/	             Create a new book.	                          Yes
PUT	    /books/<int:pk>/edit/	 Update an existing book.	                  Yes
DELETE	/books/<int:pk>/delete/	 Delete a book.	                              Yes


Permissions
Authenticated Users: Can create, update, and delete books.
Unauthenticated Users: Have read-only access to the books.

Project Structure
models.py : Contains the Book model, which defines the structure of book data.
serializers.py: Includes the BookSerializer for serializing Book instances to JSON format and vice versa.
views.py: Implements the API views for handling book-related HTTP requests.
urls.py: Maps the API endpoints to the corresponding views.



Setup and Installation
Prerequisites
Python 3.10 or higher
Django 4.0 or higher
Django REST Framework


Installation Steps
Clone the repository:
git clone https://github.com/agathaikemeh/Alx_DjangoLearnLab.git


Create a Virtual Enviroment
python -m venv venv

Activate the virtual enviroment
venv\Scripts\activate

Install Django and Django REST Framework using pip:
pip install django djangorestframework

Create a New Django Project:
django-admin startproject advanced_api_project

Create a New Django App:
cd advanced_api_project
python manage.py startapp api




API Endpoints
1. GET /books/ - List all books
Description: Retrieves a list of all books stored in the system.
Permissions:
Public (Unauthenticated users can view the list).
Authenticated users can modify the list.
Query Parameters: None.
Response:
Returns a JSON list of all books.
Uses the BookSerializer for serialization.


2. GET /books/int:pk/ - Retrieve a book by ID
Description: Retrieves the details of a single book identified by its primary key (pk).
Permissions:
Public (Unauthenticated users can view book details).
Authenticated users can also view the details.
Query Parameters: None.
Response:
Returns a JSON object containing the book's details.
Uses the BookSerializer for serialization.

3. POST /books/add/ - Create a new book
Description: Allows authenticated users to create a new book.
Permissions:
Requires the user to be authenticated.
Unauthenticated users cannot create new books.
Request Body:
JSON object containing the book details (title, author, etc.).
Response:
Returns a JSON object containing the created book's details.

4. PUT /books/int:pk/edit/ - Update an existing book
Description: Allows authenticated users to update an existing book’s details.
Permissions:
Requires the user to be authenticated.
Unauthenticated users cannot update books.
Request Body:
JSON object containing the updated details for the book.
Response:
Returns a JSON object with the updated book's details.

5. DELETE /books/int:pk/delete/ - Delete a book
Description: Allows authenticated users to delete a specific book from the system.
Permissions:
Requires the user to be authenticated.
Unauthenticated users cannot delete books.
Response:
Returns a success message upon successful deletion.


Custom Settings and Hooks
Permission Classes:
IsAuthenticatedOrReadOnly is used in views like BookListView and BookDetailView to allow read-only access for unauthenticated users and full access for authenticated users.
IsAuthenticated is used in views like BookCreateView, BookUpdateView, and BookDeleteView to ensure only authenticated users can create, update, or delete books.
Custom Behavior:
The BookCreateView uses the BookSerializer for validating and creating new books.
The BookUpdateView similarly uses BookSerializer to validate and update the existing books.
The BookDeleteView deletes the book using the provided pk and is protected by authentication.


