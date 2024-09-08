# Bookify

Bookify is an AI-powered book recommendation platform that helps users discover new books based on personalized keywords. By leveraging Natural Language Processing (NLP) with SpaCy, Bookify provides smart suggestions tailored to user preferences. The app also allows users to keep track of the books they've read and plan to read.

## Features

- **Personalized Book Suggestions**: Enter keywords like "adventure," "romance," or "mystery" and get tailored book recommendations.
- **User Accounts**: Sign up for an account to manage your book lists.
- **Track Your Books**: Keep lists of books you've read and plan to read.
- **Smart Search**: The AI engine processes your keywords using SpaCy to match the best books for your interests.

## How It Works

1. **Sign Up**: Create an account to start using Bookify.
2. **Input Keywords**: Use specific keywords related to genres, themes, or emotions you're looking for in books.
3. **Get Recommendations**: Based on the keywords, Bookify will suggest books that align with your preferences.
4. **Manage Your Lists**: Add books to your "Read" or "Plan to Read" lists and track your reading journey.

## Technologies Used

- **Backend**: Python, Flask/Django
- **Frontend**: HTML, CSS, JavaScript
- **NLP**: SpaCy for keyword extraction and book matching
- **Machine Learning**: TF-IDF, Cosine Similarity for content-based recommendations
- **Database**: SQLite or PostgreSQL for storing user data and book lists
- **Authentication**: Flask-Login or Django built-in authentication for user accounts

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bookify.git
