from flask import Flask, url_for, request, render_template
from dbm import connection

app = Flask(__name__)


@app.route('/')
def main():
    with connection.cursor() as cursor:
        select_port_data = "SELECT * FROM port_items"
        cursor.execute(select_port_data)
        rows = cursor.fetchall()
        return render_template('portfolio.html',data=rows)


@app.route('/portfolio/<title>')
def portfolio(title):
    print(title)
    return ""


if __name__ == "__main__":
    app.run(debug=True)
