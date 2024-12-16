# Django Blog Project

Welcome to the Django Blog Project! This application is built using Django and provides functionality for users to create, view, update, and delete blog posts. It includes user authentication and profile management, ensuring secure access and personalized experiences for users.

---

## **Features**
- **User Authentication**:
  - User registration, login, and logout.
  - Profile management with the ability to update the email address.

- **Blog Post Management (CRUD)**:
  - **Create**: Authenticated users can create new blog posts.
  - **Read**: All users can view a list of posts and their details.
  - **Update**: Only the author of a post can edit it.
  - **Delete**: Only the author of a post can delete it.

- **Permissions**:
  - Public access to view posts.
  - Restricted access to create, edit, or delete posts.

---

## **Getting Started**

### **1. Clone the Repository**
Clone the project from the GitHub repository:
```bash
git clone https://github.com/agathaikemeh/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/django_blog


Install dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py makemigrations
python manage.py migrate

Start the development server:
python manage.py runserver

Open the application in the browser:
http://127.0.0.1:8000


User Authentication
Register
Navigate to /register/ to create a new account.

Login
Navigate to /login/ to log into your account.

Logout
Navigate to /logout/ to log out.

Profile Management
Navigate to /profile/ to view and update your profile information


Blog Post Management
Create a Post
Log in to your account.
Navigate to /post/new/.
Fill out the form with the post title and content, then submit.

View All Posts
Navigate to the homepage (/).
Browse the list of posts. Each post displays its title, a snippet of content, and the author.

View a Single Post
Click on a post title from the homepage or navigate to /post/<id>/ (replace <id> with the post's ID).
View the full content of the post along with its details.

Edit a Post
Navigate to /post/<id>/edit/ (replace <id> with the post's ID).
Update the title or content of the post and submit.

Delete a Post
Navigate to /post/<id>/delete/ (replace <id> with the post's ID).
Confirm deletion.

Permission Handling
Authenticated Users:
Only logged-in users can create new posts.
Anonymous users are redirected to the login page if they attempt to access restricted pages like /post/new/.

Post Authors:
Only the author of a post can edit or delete it.
If another user or an unauthenticated user tries to edit or delete a post, they will receive a "permission denied" message or be redirected.

Public Access:
The homepage (/) and individual post pages (/post/<id>/) are accessible to all users, including anonymous users.


Project Structure
django_blog/
├── blog/
│   ├── templates/blog/      # HTML templates
│   ├── static/              # CSS, JavaScript, and other static files
│   ├── models.py            # Models for database
│   ├── views.py             # Views for handling requests
│   ├── urls.py              # URL patterns for the blog app
│   ├── forms.py             # Custom forms for user and post handling
│   └── ...
├── django_blog/
│   ├── settings.py          # Django project settings
│   ├── urls.py              # URL patterns for the entire project
│   └── ...
├── db.sqlite3               # SQLite database
└── manage.py                # Django management script


Testing the Features
Test the user authentication by registering, logging in, and logging out.
Test blog post management:
Create posts as a logged-in user.
View the list of posts and individual post details.
Edit and delete posts, ensuring only the author can perform these actions.
Check the navigation:
Test links between pages (e.g., from the post list to the detail page).
Verify that buttons like "Create Post" and "Edit Post" redirect appropriately.