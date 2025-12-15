import requests

print("=== Get /books ===")
response = requests.get('http://127.0.0.1:5000/books')
print(response.json())

response = requests.delete('http://127.0.0.1:5000/books/1')
print(response.json())
# print("=== POST /books ===")
# new_book = {
#     "title" : "Problem of Pain",
#     "author" : "C.S. Lewis",
#     "price" : 34.99,
# }
# response = requests.post('http://127.0.0.1:5000/books', json=new_book)
# print("Status:", response.status_code)
# print("Response:", response.json())



# print("=== Get /books (after adding) ===")
# response = requests.get('http://127.0.0.1:5000/books')
# print(response.json())