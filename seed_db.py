from app import app, db, Book

# Create application context

with app.app_context():
    # Clear existing data
    db.drop_all()

    # Create tables
    db.create_all()

    # Add sample books
    book1 = Book(
        title='Python Crash Course',
        author='Eric Matthes',
        price=39.99
    )
    book2 = Book(
        title='Flask Web Development',
        author='Miguel Grinberg',
        price=44.99
    )

    book3 = Book(
        title='Clean Code',
        author='Robert Martin',
        price=49.99
    )
    # Add to database
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)

    # Save changes
    db.session.commit()
    print("Database seeded with sample books.")