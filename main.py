from flask import Flask, request, render_template as render
import sqlite3
import re

sql = "SELECT * FROM bible WHERE LOWER(verse) LIKE LOWER(?) ORDER BY Book, Chapter, Versecount"
versions = [
            {'expansion': "New King James Version",      'name': "NKJV", 'db': 'databases/NKJVBible_Database.db', 'wiki': 'https://en.wikipedia.org/wiki/New_King_James_Version'},
            {'expansion': "King James Version",          'name': "KJV",  'db': 'databases/KJVBible_Database.db',  'wiki': 'https://en.wikipedia.org/wiki/King_James_Version '},
            {'expansion': "American Standard Version",   'name': "ASV",  'db': 'databases/ASVBible_Database.db',  'wiki': 'https://en.wikipedia.org/wiki/American_Standard_Version'},
            {'expansion': "Young's Literal Translation", 'name': "YLT",  'db': 'databases/YLTBible_Database.db',  'wiki': 'https://en.wikipedia.org/wiki/Young\'s_Literal_Translation'},
            {'expansion': "Darby English Bible",         'name': "DBY",  'db': 'databases/DBYBible_Database.db',  'wiki': 'https://en.wikipedia.org/wiki/Darby_Bible'},
            {'expansion': "Webster's Revision",          'name': "WBT",  'db': 'databases/WBTBible_Database.db',  'wiki': 'https://en.wikipedia.org/wiki/Webster%27s_Revision'},
            {'expansion': "World English Bible",         'name': "WEB",  'db': 'databases/WEBBible_Database.db',  'wiki': 'https://en.wikipedia.org/wiki/World_English_Bible'},
            # {'expansion': "Bible in Basic English",      'name': "BBE",  'db': 'databases/BBEBible_Database.db',  'wiki': 'https://en.wikipedia.org/wiki/Bible_in_Basic_English'}
            ]
books    = [ {
      'type': "Pentateuch", 'selected': True, 'testament': "OT1", 'id': 0,  'text': "Genesis" }, {
      'type': "Pentateuch", 'selected': True, 'testament': "OT1", 'id': 1,  'text': "Exodus" }, {
      'type': "Pentateuch", 'selected': True, 'testament': "OT1", 'id': 2,  'text': "Leviticus" }, {
      'type': "Pentateuch", 'selected': True, 'testament': "OT1", 'id': 3,  'text': "Numbers" }, {
      'type': "Pentateuch", 'selected': True, 'testament': "OT1", 'id': 4,  'text': "Deuteronomy" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 5,  'text': "Joshua" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 6,  'text': "Judges" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 7,  'text': "Ruth" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 8,  'text': "1 Samuel" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 9,  'text': "2 Samuel" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 10, 'text': "1 Kings" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 11, 'text': "2 Kings" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 12, 'text': "1 Chronicles" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 13, 'text': "2 Chronicles" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 14, 'text': "Ezra" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 15, 'text': "Nehemiah" }, {
      'type': "OTHistory",  'selected': True, 'testament': "OT1", 'id': 16, 'text': "Esther" }, {
      'type': "OTWisdom",   'selected': True, 'testament': "OT1", 'id': 17, 'text': "Job" }, {
      'type': "OTWisdom",   'selected': True, 'testament': "OT1", 'id': 18, 'text': "Psalms" }, {
      'type': "OTWisdom",   'selected': True, 'testament': "OT1", 'id': 19, 'text': "Proverbs" }, {
      'type': "OTWisdom",   'selected': True, 'testament': "OT2", 'id': 20, 'text': "Song of Songs" }, {
      'type': "OTWisdom",   'selected': True, 'testament': "OT2", 'id': 21, 'text': "Ecclesiastes" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 22, 'text': "Isaiah" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 23, 'text': "Jeremiah" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 24, 'text': "Lamentations" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 25, 'text': "Ezekiel" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 26, 'text': "Daniel" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 27, 'text': "Hosea" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 28, 'text': "Joel" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 29, 'text': "Amos" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 30, 'text': "Obadiah" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 31, 'text': "Jonah" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 32, 'text': "Micah" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 33, 'text': "Nahum" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 34, 'text': "Habakkuk" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 35, 'text': "Zephaniah" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 36, 'text': "Haggai" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 37, 'text': "Zechariah" }, {
      'type': "OTProphet",  'selected': True, 'testament': "OT2", 'id': 38, 'text': "Malachi" }, {
      'type': "Gospel",     'selected': True, 'testament': "NT1", 'id': 39, 'text': "Matthew" }, {
      'type': "Gospel",     'selected': True, 'testament': "NT1", 'id': 40, 'text': "Mark" }, {
      'type': "Gospel",     'selected': True, 'testament': "NT1", 'id': 41, 'text': "Luke" }, {
      'type': "Gospel",     'selected': True, 'testament': "NT1", 'id': 42, 'text': "John" }, {
      'type': "NTHistory",  'selected': True, 'testament': "NT1", 'id': 43, 'text': "Acts of the Apostles" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 44, 'text': "Romans" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 45, 'text': "1 Corinthians" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 46, 'text': "2 Corinthians" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 47, 'text': "Galatians" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 48, 'text': "Ephesians" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 49, 'text': "Philippians" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 50, 'text': "Colossians" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 51, 'text': "1 Thessalonians" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT1", 'id': 52, 'text': "2 Thessalonians" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 53, 'text': "1 Timothy" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 54, 'text': "2 Timothy" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 55, 'text': "Titus" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 56, 'text': "Philemon" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 57, 'text': "Hebrews" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 58, 'text': "James" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 59, 'text': "1 Peter" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 60, 'text': "2 Peter" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 61, 'text': "1 John" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 62, 'text': "2 John" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 63, 'text': "3 John" }, {
      'type': "Epistle",    'selected': True, 'testament': "NT2", 'id': 64, 'text': "Jude" }, {
      'type': "NTProphet",  'selected': True, 'testament': "NT2", 'id': 65, 'text': "Revelation" }
    ]
version  = versions[0]
keyword  = ""
rows     = []
caseSns  = False
ot       = False
nt       = False

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def keywordSplitter(keywordInp):
    keywords = keywordInp.split(',')
    return keywords

app = Flask(__name__)

# resultSorted() idea incorporated from https://web.archive.org/web/20150222160237/stygianvision.net/updates/python-sort-list-object-dictionary-multiple-key/
def resultSorter(rows=[]):
    return sorted(rows, key = lambda row: (row['Book'], row['Chapter'], row['Versecount']))

def bookUpdate(keywords, rows=[]):
    chBooks = []
    for book in books:
        if book['selected'] == True:
            chBooks.append(book['id'])
    editRows = []
    for row in rows:
        exactMatch = False
        for word in keywords:
            if (word in row['verse']):
                exactMatch = True
                break

        if (row['Book'] in chBooks) and (not caseSns or exactMatch):
            book = next(item for item in books if item['id'] == row['Book'])['text']
            editRows.append({'Book': book, 'Chapter': row['Chapter'], 'Versecount': row['Versecount'], 'verse': row['verse']})
    return editRows

def dbRefresh():
    global version, versions, sql, keyword, rows
    db = sqlite3.connect(next(item for item in versions if item['name'] == version['name'])['db'])
    db.row_factory = dict_factory
    rows = []
    cur  = db.cursor()
    
    # Search ORing, ANDing ...
    keywords = keywordSplitter(keyword)
    
    for word in keywords:
        cur.execute(sql, ['%' + word + '%'])
        for row in cur.fetchall():
            if row not in rows:
                rows.append(row)
    
    cur.close()
    rows = resultSorter(rows)
    rows = bookUpdate(keywords, rows)
    for row in rows:
        row['verse'] = str(row['verse'])
        if (keyword == ""):
            row['verse'] = re.split("( )", row['verse'], flags=re.IGNORECASE)
        else:
            wordSeq = ["("]
            for word in keywords:
                wordSeq.append(word)
                wordSeq.append("|")
            wordSeq.pop()
            wordSeq.append(")")
            wordSeq = ''.join(wordSeq)
            row['verse'] = re.split(wordSeq, row['verse'], flags=re.IGNORECASE)
    return render('index.html', rows = rows, version = version, versions = versions, keyword = keyword, books = books, caseSns = caseSns, keywords = keywords)

@app.route('/', methods=['GET'])
def index():
    global version, versions, sql, keyword, caseSns, rows, ot, nt
    version = versions[0]
    keyword = ""
    rows    = []
    caseSns = False
    ot      = False
    nt      = False
    for book in books:
        book['selected'] = True
    return render('index.html', rows = [],   version = version, versions = versions, keyword = keyword, books = books, caseSns = caseSns)

@app.route('/result', methods=['GET'])
def search():
    global version, versions, sql, keyword
    keyword     = request.args.get('keyword')
    versionName = request.args.get('version')
    caseSns     = request.args.get('caseSns')

    for v in versions:
        if v['name'] == versionName:
            version = v
            break  
    return dbRefresh()

@app.route('/case', methods=['GET'])
def caseFlip():
    global version, versions, sql, keyword, caseSns
    caseSns = not(caseSns)
    return dbRefresh()

def updateSelection(list):
    for book in books:
        if book['testament'] in list:
            book['selected'] = not book['selected']
    return

@app.route('/testChoose/<test>', methods=['GET'])
def updateTestament(test):
    if test=="ot":
        updateSelection(["OT1", "OT2"])
    elif test=="nt":
        updateSelection(["NT1", "NT2"])
    else:
        if all(book['selected'] for book in books):
            updateSelection(["OT1", "OT2", "NT1", "NT2"])
        else:
            for book in books:
                book['selected'] = True
    return dbRefresh()

@app.route('/bookChoose', methods=['GET'])
def bookSelect():
    global version, versions, sql, keyword, ot, nt
    bkName  = request.args.get("book")
        
    for book in books:
        if book['text'] == bkName: 
            book['selected'] = not book['selected']
            break
    return dbRefresh()

# utility_functions() incorporated from https://stackoverflow.com/a/42888467/6539635
@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))

    return dict(mdebug=print_in_console)

if __name__ == '__main__':
    app.run(debug=True)
