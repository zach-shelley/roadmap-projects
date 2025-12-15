from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)


# Define Book model (represents database table)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert Book object to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price
        }


# Routes (we'll update these next)
@app.route('/')
def home():
    return "Welcome to Bookstore API with Database!"

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)

    if book:
        return jsonify(book.to_dict())
    else:
        return jsonify({"Error":"Book not found"}), 404


@app.route('/books')
def get_books():
    # OLD: return jsonify(books)
    # NEW: Query database
    all_books = Book.query.all()
    return jsonify([book.to_dict() for book in all_books])

@app.route('/books', methods=['POST'])

def add_book():
    data = request.get_json()
    if 'title' not in data or 'author' not in data or 'price' not in data:
        return jsonify({"error": "Missing required fields"}), 400

        # Check if values are not empty
    if not data['title'] or not data['author'] or not data['price']:
        return jsonify({"error": "Fields cannot be empty"}), 400

    new_book = Book(title=data['title'], author=data['author'], price=data['price'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)

    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"Success": "Book deleted."}), 204
    else:
        return jsonify({"Error": f"Book for book ID: {book_id} not found"}), 404

if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)



