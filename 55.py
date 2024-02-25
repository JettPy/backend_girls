from datetime import datetime

from flask import Flask, render_template, url_for,request

app = Flask(__name__)


posts = []

@app.route("/")
def index():
    return render_template("index1.html")


@app.route("/blog",methods=["GET","POST"])
def blog():
    if request.method =="POST":
        title = request.form["title"]
        content = request.form["content"]
        post = {"title": title,"content": content,"date": datetime.now()}
        posts.append(post)
    return render_template("blog.html",posts=posts)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
