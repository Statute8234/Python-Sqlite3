# Movie List Manager
[![sqlite3](https://img.shields.io/badge/sqlite3-brown)](https://docs.python.org/3/library/sqlite3.html)
[![random](https://img.shields.io/badge/random-pink)](https://docs.python.org/3/library/random.html)

This Python script provides a command-line interface for managing a list of movies. The script uses SQLite for database management and allows users to add, edit, display, and suggest movies, as well as manage the movie list through a "danger zone" for removing and clearing data.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

The Python script offers a command-line interface for managing a movie list using SQLite, allowing users to add, edit, display, and suggest movies, and managing the list through a "danger zone" for data removal and clearing.

## Features

- **Add a New Movie**: Add a new movie to the database with details such as title, publisher, published date, format, and rating.
- **Edit a Movie**: Edit the information of an existing movie in the database.
- **Show All Movies**: Display a list of all movies in the database.
- **Suggest a Random Movie**: Get a random movie suggestion from the database.
- **Danger Zone**: Special commands to remove a specific movie by title or clear the entire movie list.

## Installation

Prerequisites
- Python 3.6 or higher
- SQLite3
- Pillow (if image processing is needed)


## Usage

1. Clone this repository or download the script.
2. Ensure you have Python 3.x installed.
3. Install SQLite3 if it's not already installed.

## Contributing

1. Run the script using Python:

   ```bash
   python movie_manager.py
