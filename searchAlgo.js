const express = require('express')
var   sqlite3 = require('sqlite3');

const app     = express()
const port    = 3000
var   count   = 0;

let db = new sqlite3.Database(
  'NKJVBible_Database.db',
  sqlite3.OPEN_READONLY,
  function(err) {
    if (err) {
return console.error(err.message);
    }
    console.log('~~~ Search Results ~~~\n\n');
  }
);

let sql        = 'SELECT Book BookNum, Chapter ChapterNum, Versecount VerseNum, verse Verse FROM bible WHERE BookNum = ? ORDER BY BookNum';
let searchText = 'Lord';
let caseCheck  = false;
let searchBkLt = [];
var Books      = ["Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", "Song of Songs", "Ecclesiastes", "Isaiah", "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts of the Apostles", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"];
var inputBooks = ["Matthew", "Mark", "Luke"]

for (let i = 0; i < inputBooks.length; i++) {
  searchBkLt.push(Books.indexOf(inputBooks[i]));
}

for (let i = 0; i < searchBkLt.length; i++) {
  db.each(
  	sql,
  	[searchBkLt[i]],
  	function(err, row) {
		  if (err) return console.error(err.message);
		  if (row.Verse.toLowerCase().includes(searchText.toLowerCase()) > 0) {
  			if (!(caseCheck) || (row.Verse.search(searchText) > -1)) {
				  /*if (count == 0) {
  					var ul = document.createElement('ul');
					 ul.className = 'myUL';
					 document.getElementById('displayVerses').appendChild(ul);
				  }*/
				  count = count + 1;
				  let verseData = ' '+ count + ': ' + Books[row.BookNum] + ' ' + row.ChapterNum + ':' + row.VerseNum + ' - ' + row.Verse + '\n'
				  console.log(verseData);
				  /// app.get('/verse', (req, res) => res.send(verseData))
				  // app.listen(port, ()=> console.log('Listening at http://localhost:${port}/verse'))
				  /*var li = document.createElement('li style="padding-bottom: 4px;"');
				  ul.appendChild(li);
				  li.innerHTML += verData;
				  li.className = "myList";*/
			 }
		  }
	 }
  );	
}

db.close(function(err) {
  if (err) return console.error(err.message);
  console.log('\n\n~~~ The End ~~~');
});