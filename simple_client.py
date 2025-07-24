from requests import get, post

#headers = {}

item_name = "Club Sandwich"
item_price = 4.99
item_description = "The basic club sandwich with turkey, bacon, lettuce, tomato, and mayonnaise."

print(post(f"http://localhost:8000/items/{item_name}/{item_price}/{item_description}"))
print(get("http://127.0.0.1:8000/items").json())
