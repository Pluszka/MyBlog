from flask import Flask, render_template
from post import Post

database = Post()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", articles=database.get_blog())

@app.route('/article/<article_id>')
def article_page(article_id):
    return render_template("post.html", article=database.get_blog()[int(article_id)-1])

if __name__ == "__main__":
    app.run(debug=True)
