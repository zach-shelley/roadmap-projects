from flask import Flask, jsonify, request

# Create Flask app
app = Flask(__name__)


books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "price": 39.99},
    {"id": 2, "title": "Flask Web Development", "author": "Miguel Grinberg", "price": 44.99},
    {"id": 3, "title": "Clean Code", "author": "Robert Martin", "price": 49.99}
]

# Define a route
@app.route('/')
def home():
    return "Welcome to Bookstore API!"

@app.route('/books/<int:book_id>')
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)

    return jsonify({"error": "Book not found"}), 404

@app.route('/books')
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    if not data or 'title' not in data or 'author' not in data or 'price' not in data:
        return jsonify({'error': "Missing required fields"}), 400
    
    new_id = max(book['id'] for book in books) + 1
    new_book = {
        "id" : new_id,
        "title" : data['title'],
        "author" : data['author'],
        "price" : data['price']
    }
    books.append(new_book)
    return jsonify(new_book), 201


# Run the app

if __name__ == '__main__':
    app.run(debug=True)



