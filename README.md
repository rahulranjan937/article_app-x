# Welcome to Article-App

## Description

This is a simple app that allows you to create articles and share them with other users.

## Getting Started

To get started with the app, clone the repo and then create a new python virtual environment.

## Installation

    ```
    git clone https://github.com/rahulranjandev/article_app-x.git
    cd article-app
    python3 -m venv .venv
    source .venv/bin/activate # for linux and mac
    .venv\Scripts\activate # for windows
    ```

Next, install the needed packages (while the virtual environment is activated):

    ```
    (.venv)$ pip install -r requirements.txt
    ```

Finally, run the development server:

    ```
    (.venv)$ python app.py runserver
    ```

The app will be available at [localhost](http://localhost:5001/).

## Technologies Used

- Flask
- MySQL
- DajngoHTML
- Bootstrap
- Gunicorn

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Author

[Rahul Ranjan](https://github.com/rahulranjandev)
