from flask import Flask, render_template
from post import Post
import requests

URL_SAMPLE_BLOG="https://api.npoint.io/c790b4d5cab58020d391"

posts = requests.get(URL_SAMPLE_BLOG)
posts_json = posts.json()
post_objects = []
for post in posts_json:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    print (post_object.title, post_object.subtitle, post_object.body, post_object.id)
    post_objects.append(post_object)

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
