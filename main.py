from fastapi import FastAPI

app = FastAPI()

#Product data
products = [
    {
        "id": 1, 
        "name": "Mechanical Keyboard", 
        "price": 899.99,
        "category": "Accessories"
    },

    {"id": 2, 
     "name": "Wireless Mouse", 
     "price": 25,
     "category": "Accessories"
    },

    {"id": 3, 
     "name": "Gaming monitor", 
     "price": 75,
     "category": "Monitors"
    }
]

@app.get("/")
def home():
    return {"message": "Welcome to Firecell Graphics"}
