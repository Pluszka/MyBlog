from flask import Flask, render_template
from post import Post

database = Post()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", articles=database.get_blog() )

if __name__ == "__main__":
    app.run(debug=True)
