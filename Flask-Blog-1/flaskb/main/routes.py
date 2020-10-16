from flask import request, render_template
from flaskb.models import Post
from flaskb import app


@app.route('/')
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_created.desc()).paginate(page=page, per_page=3)
    return render_template('index.html', posts=posts)
