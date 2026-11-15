from fastapi import FastAPI

app = FastAPI()

#Product data
products = [
    {
        "id": 1, 
        "name": "Mechanical Keyboard", 
        "price": 899.99,
        "category": "sunga"
    },

    {
        "id": 2, 
        "name": "Wireless Mouse", 
        "price": 449.99,
        "category": "Accessories"
    },

    {
        "id": 3, 
        "name": "Gaming monitor", 
        "price": 3499.99,
        "category": "Monitors"
    }
]

@app.get("/")
def home():
    return {"message": "Welcome to Firecell Graphics"}


@app.get("/api/products")
def get_products():
    return products
