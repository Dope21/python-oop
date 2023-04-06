import requests

url = "http://localhost:8000/add_cart?email=customer@example.com"
payload = {
    "cart_item": {
        "product": {
            "name": "Product 1",
            "price": 10.99
        },
        "quantity": 2
    }
}
response = requests.post(url, json=payload)
print(response.json())
