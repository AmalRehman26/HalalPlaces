import requests

BASE_URL = "http://localhost:8000"

def add_restaurant(name, city, cuisine, address=None, phone=None):
    """Add a restaurant to the database"""
    data = {
        "name": name,
        "city": city,
        "cuisine": cuisine,
        "address": address,
        "phone": phone
    }
    
    response = requests.post(f"{BASE_URL}/restaurants/api", json=data)
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Added: {name}")
        return result.get("restaurant", {}).get("id")
    else:
        print(f"❌ Error adding {name}: {response.text}")
        return None

def add_review(restaurant_id, rating, text):
    """Add a review to a restaurant"""
    data = {
        "rating": rating,
        "text": text
    }
    
    response = requests.post(
        f"{BASE_URL}/reviews/api/restaurants/{restaurant_id}/reviews",
        json=data
    )
    
    if response.status_code == 201:
        print(f"   ✅ Added review with {rating} stars")
        return True
    else:
        print(f"   ❌ Error adding review: {response.text}")
        return False

def main():
    print("🍽️  Adding restaurants to database...\n")
    
    
    print("📍 Restaurant 1:")
    royal_id = add_restaurant(
        name="Royal Chicken and Kabab",
        city="Amherst",  
        cuisine="Greek-Middle Eastern",
        address=None,  
        phone=None    
    )
    
    if royal_id:
        add_review(
            restaurant_id=royal_id,
            rating=5, 
            text="Just had a great first visit here! Awesome customer service, beautiful restaurant, the food is delicious. I'm excited to return!"
        )
    
    print()
    

    print("📍 Restaurant 2:")
    halal_cart_id = add_restaurant(
        name="Halal Cart",
        city="Amherst",
        cuisine="Greek-Middle Eastern",
        address=None,
        phone=None
    )
    
    if halal_cart_id:
        add_review(
            restaurant_id=halal_cart_id,
            rating=4,
            text="Good food and reasonable prices. A solid option for halal Mediterranean cuisine."
        )
    
    print()
    
    
    print("\n✨ Done! Visit http://localhost:8000 to see your restaurants!")

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the server.")
        print("Make sure your FastAPI application is running on http://localhost:8000")
        print("Run: python3 main.py")
    except Exception as e:
        print(f"❌ Error: {e}")