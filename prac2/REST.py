from flask import Flask, request, jsonify, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)

books = [
    {"id": 1, "title": "CC & WS", "author": "Dr. XYZ"},
    {"id": 2, "title": "DS", "author": "Dr. LMN"}
]

# Get all books (JSON)
@app.route("/books")
def get_books():
    return jsonify(books)


# Get all books (XML)
@app.route("/books/xml")
def get_books_xml():
    root = ET.Element("books")
    for b in books:
        book = ET.SubElement(root, "book", id=str(b["id"]))
        ET.SubElement(book, "title").text = b["title"]
        ET.SubElement(book, "author").text = b["author"]
    return Response(ET.tostring(root), mimetype="text/xml")


# Get book by ID
@app.route("/book/<int:id>")
def get_book(id):
    book = next((b for b in books if b["id"] == id), None)
    return jsonify(book if book else {"Error": "Book not found"})


# Add book
@app.route("/addbook", methods=["POST"])
def add_book():
    data = request.json
    book = {"id": len(books)+1, "title": data["title"], "author": data["author"]}
    books.append(book)
    return jsonify(book)


# Update book
@app.route("/updatebook/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.json
    for b in books:
        if b["id"] == id:
            b.update(data)
            return jsonify(b)
    return jsonify({"Error": "Book not found"})


# Delete book
@app.route("/deletebook/<int:id>", methods=["DELETE"])
def delete_book(id):
    for b in books:
        if b["id"] == id:
            books.remove(b)
            return jsonify({"Msg": "Book deleted"})
    return jsonify({"Error": "Book not found"})


if __name__ == "__main__":
    app.run(debug=True, port=2546)