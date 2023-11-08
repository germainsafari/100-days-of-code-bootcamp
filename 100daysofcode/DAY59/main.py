from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    css_url = url_for('static', filename='static/css/styles.css')
    return render_template("index.html", css_url=css_url)

if __name__ == "__main__":
    app.run(debug=True)

