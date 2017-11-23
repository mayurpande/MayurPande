from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('portfolio.html')


if __name__ == "__main__":
    app.run(debug=True)
