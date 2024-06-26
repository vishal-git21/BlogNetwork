# BlogNetwork

BlogNetwork is a blog-style web application built with Django. It allows users to write blog posts and Twitter-style updates, interact with posts through likes and comments, and manage content with pagination. It also includes a robust authentication system to manage user accounts.

## Features

- User Authentication (Sign up, Log in, Log out)
- Create, edit, and delete blog posts and Twitter-style updates
- Like and comment on posts
- Pagination for posts and comments
- User profile management

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** MySQL (default, can be changed to PostgreSQL, MySQL, etc.)
- **Authentication:** Django based authentication system

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Configuration

- **Database:** The project uses MySQL by default. To use a different database.

- **Static Files:** Static files (CSS, JavaScript) are managed with Django's static files app.

### Project Structure

- `blognetwork/`: Project settings and URLs
- `users/`: User authentication and profile management
- `posts/`: Blog posts and Twitter-style updates
- `comments/`: Comment functionality for posts

### API Endpoints

- **Authentication:** `/api/auth/`
  - Sign up, log in, log out
- **Posts:** `/api/posts/`
  - List, create, retrieve, update, delete posts
- **Comments:** `/api/comments/`
  - List, create, retrieve, update, delete comments
- **Likes:** `/api/likes/`
  - Like and unlike posts

