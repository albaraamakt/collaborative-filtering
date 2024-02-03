import requests

# Example: Send a POST request to provide feedback (purchase)
# This is just an example, you'll need to replace it with actual user and food IDs
user = int(input("User ID: "))
purchased_meal = int(input("Meal ID: "))
json_data = {"user_id": user, "food_id": purchased_meal}
response = requests.post('http://localhost:5002/feedback', json=json_data)

print(response.json())  # Print the response from the server
