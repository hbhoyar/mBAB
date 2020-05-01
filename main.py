from flask import Flask, request, render_template as render
import sqlite3
import os

sql = "SELECT * FROM bible WHERE LOWER(verse) LIKE LOWER(?) ORDER BY Book, Chapter, Versecount"
versions = {"NKJV": 'databases/NKJVBible_Database', "NIV": 'databases/NIVBible_Database', "ASV": 'databases/ASVBible_Database'}
version  = "NKJV"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render('index.html', rows=[])


@app.route('/result', methods=['GET'])
def search():
    keyword = '%' + request.args.get('keyword', '') + '%'

    db = sqlite3.connect(versions["NKJV"])
    db.row_factory = dict_factory
    cur = db.cursor()
    cur.execute(sql, [keyword])
    rows = cur.fetchall()
    cur.close()
    
    return render('index.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
