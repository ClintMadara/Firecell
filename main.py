from fastapi import FastAPI, HTTPException

app = FastAPI()

#Product data
products = [
    {
        "id": 1, 
        "name": "Mechanical Keyboard", 
        "price": 899.99,
        "category": "Accessories"
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
    return {"message": "Welcome to Firecell"}


@app.get("/api/products")
def get_products():
    return products

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
        
    raise HTTPException(
        status_code=404, 
        detail="Product not found"
    )
