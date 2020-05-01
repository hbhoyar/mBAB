Vue.component("book_button", {
  props: ["book"],
  template:
    '<li>\
      <div v-if="!(book.selected)">\
        <button class="btn-gradient blue mini" v-on:click="chooseBook(book)">\
          {{ book.text }}\
        </button>\
      </div>\
      <div v-if="book.selected">\
        <button class="btn-gradient red mini" v-on:click="chooseBook(book)">\
          {{ book.text }}\
        </button>\
      </div>\
    </li>',
  methods: {
    chooseBook: function(book) {
      var link = "/Books/" + book.text + ".html";
      book.selected = !(book.selected);
      // window.open(link, "_blank");
    }
  }
});

var app = new Vue({
  el: "#app",
  data: {
    version: "NKJV",
    wordSequence: "",
    books: [ {
      type: "Pentateuch", selected: false, testament: "OT1", id: 0,  text: "Genesis" }, {
      type: "Pentateuch", selected: false, testament: "OT1", id: 1,  text: "Exodus" }, {
      type: "Pentateuch", selected: false, testament: "OT1", id: 2,  text: "Leviticus" }, {
      type: "Pentateuch", selected: false, testament: "OT1", id: 3,  text: "Numbers" }, {
      type: "Pentateuch", selected: false, testament: "OT1", id: 4,  text: "Deuteronomy" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 5,  text: "Joshua" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 6,  text: "Judges" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 7,  text: "Ruth" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 8,  text: "1 Samuel" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 9,  text: "2 Samuel" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 10, text: "1 Kings" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 11, text: "2 Kings" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 12, text: "1 Chronicles" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 13, text: "2 Chronicles" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 14, text: "Ezra" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 15, text: "Nehemiah" }, {
      type: "OTHistory",  selected: false, testament: "OT1", id: 16, text: "Esther" }, {
      type: "OTWisdom",   selected: false, testament: "OT1", id: 17, text: "Job" }, {
      type: "OTWisdom",   selected: false, testament: "OT1", id: 18, text: "Psalms" }, {
      type: "OTWisdom",   selected: false, testament: "OT1", id: 19, text: "Proverbs" }, {
      type: "OTWisdom",   selected: false, testament: "OT1", id: 20, text: "Song of Songs" }, {
      type: "OTWisdom",   selected: false, testament: "OT1", id: 21, text: "Ecclesiastes" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 22, text: "Isaiah" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 23, text: "Jeremiah" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 24, text: "Lamentations" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 25, text: "Ezekiel" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 26, text: "Daniel" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 27, text: "Hosea" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 28, text: "Joel" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 29, text: "Amos" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 30, text: "Obadiah" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 31, text: "Jonah" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 32, text: "Micah" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 33, text: "Nahum" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 34, text: "Habakkuk" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 35, text: "Zephaniah" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 36, text: "Haggai" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 37, text: "Zechariah" }, {
      type: "OTProphet",  selected: false, testament: "OT2", id: 38, text: "Malachi" }, {
      type: "Gospel",     selected: false, testament: "NT",  id: 39, text: "Matthew" }, {
      type: "Gospel",     selected: false, testament: "NT",  id: 40, text: "Mark" }, {
      type: "Gospel",     selected: false, testament: "NT",  id: 41, text: "Luke" }, {
      type: "Gospel",     selected: false, testament: "NT",  id: 42, text: "John" }, {
      type: "NTHistory",  selected: false, testament: "NT",  id: 43, text: "Acts of the Apostles" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 44, text: "Romans" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 45, text: "1 Corinthians" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 46, text: "2 Corinthians" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 47, text: "Galatians" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 48, text: "Ephesians" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 49, text: "Philippians" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 50, text: "Colossians" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 51, text: "1 Thessalonians" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 52, text: "2 Thessalonians" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 53, text: "1 Timothy" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 54, text: "2 Timothy" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 55, text: "Titus" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 56, text: "Philemon" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 57, text: "Hebrews" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 58, text: "James" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 59, text: "1 Peter" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 60, text: "2 Peter" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 61, text: "1 John" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 62, text: "2 John" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 63, text: "3 John" }, {
      type: "Epistle",    selected: false, testament: "NT",  id: 64, text: "Jude" }, {
      type: "NTProphet",  selected: false, testament: "NT",  id: 65, text: "Revelation" }
    ]
  }
});
