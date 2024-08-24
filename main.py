from flask import Flask, request, render_template

app = Flask(__name__)

# This list will store comments in memory (for demonstration purposes)
comments = []


@app.route('/')
def home():
    return render_template('blog.html', comments=comments)


@app.route('/comment', methods=['POST'])
def comment():
    content = request.form['comment']

    # Add the comment to the list (vulnerable to XSS)
    comments.append(content)

    return render_template('blog.html', comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
