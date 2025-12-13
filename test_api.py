import requests

print("=== Get /books ===")
response = requests.get('http://127.0.0.1:5000/books')
print(response.json())


print("=== POST /books ===")
new_book = {
    "title" : "Learning Flask",
    "author" : "Zach Shelley",
    "price" : 34.99,
}
response = requests.post('http://127.0.0.1:5000/books', json=new_book)
print(response)
print(response.json())

print("=== Get /books (after adding) ===")
response = requests.get('http://127.0.0.1:5000/books')
print(response.json())