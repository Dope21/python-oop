import requests

url = "http://localhost:8000/add_cart"
payload = {
    "email": "customer@example.com",
    "cart_item": {
        "product": {
            "name": "Product Name",
            "price": 9.99
        },
        "quantity": 2
    }
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

assert response.status_code == 200, f"Request failed with status code {response.status_code}: {response.json()['detail']}"
