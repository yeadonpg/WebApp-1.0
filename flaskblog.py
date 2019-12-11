# Credit to Corey Shafer for providing the tutorial for this application

# This setup script is provided by The Pallets Projects here:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart
from flask import Flask, render_template

app = Flask(__name__)


posts = [
    {
        'author': 'Patrick Yeadon',
        'title': 'Blog Post - 1',
        'content': 'My first post!',
        'date_posted': 'December 11, 2019'
    },
    {
        'author': 'Patrick Yeadon',
        'title': 'Blog Post - 2',
        'content': 'My second post!',
        'date_posted': 'December 11, 2019'
    },
    {
        'author': 'Patrick Yeadon',
        'title': 'Blog Post - 3',
        'content': 'My third post!',
        'date_posted': 'December 11, 2019'
    }
]


# Home Page
@app.route('/')
@app.route('/home')
def home():
    # Return HTML
    return render_template('home.html', posts=posts)


# About Page
@app.route('/about')
def about():
    # Return HTML
    return render_template('about.html', title='About')


# If this file is run directly, launch the web application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
