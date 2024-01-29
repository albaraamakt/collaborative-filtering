import requests

# Example: Send a POST request to provide feedback (purchase)
# This is just an example, you'll need to replace it with actual user and food IDs
purchase_feedback = {"user_id": 1, "food_id": 25}
response = requests.post('http://localhost:5002/feedback', json=purchase_feedback)

print(response.json())  # Print the response from the server
