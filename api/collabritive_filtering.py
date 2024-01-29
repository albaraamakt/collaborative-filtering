import pandas as pd

# Load dataset
all_user_orders = pd.read_csv('../orders.csv')

# Create a user-item matrix with order counts
user_item_matrix = all_user_orders.groupby(['user_id', 'meal_id']).size().unstack(fill_value=0)

df = pd.DataFrame(user_item_matrix)

from sklearn.metrics.pairwise import cosine_similarity

# Calculate cosine similarity
user_similarity_matrix = pd.DataFrame(cosine_similarity(user_item_matrix), index=user_item_matrix.index, columns=user_item_matrix.index)

# Display the user similarity matrix
print(user_similarity_matrix)

# Specify the neighborhood size
neighborhood_size = 5

# Identify top-N similar users for each user
top_similar_users = user_similarity_matrix.apply(lambda row: row.nlargest(neighborhood_size).index.tolist(), axis=1)

# Function to generate recommendations for a user
def generate_recommendations(user_id):
    similar_users = top_similar_users.loc[user_id]
    user_orders = user_item_matrix.loc[user_id]

    # Identify food items not ordered by the target user
    not_ordered_items = user_orders[user_orders == 0].index

    # Aggregate food items ordered by similar users
    similar_users_orders = user_item_matrix.loc[similar_users].sum()

    # Exclude items already ordered by the target user
    recommended_items = similar_users_orders[not_ordered_items]

    # Sort recommended items by order count in descending order
    recommended_items = recommended_items.sort_values(ascending=False)

    return recommended_items

food_data = pd.read_csv('../food_data_1.csv')

# Function to display recommendations when a user logs in
def display_recommendations_on_login(user_id):
    recommendations = generate_recommendations(user_id)

    # Assuming you have a user interface, you can display the recommendations there
    print(f"Hello User {user_id}! Here are your personalized recommendations:")
    for food_id, order_count in recommendations.items():
        print(f"Meal ID: {food_id}, Meal: {food_data.loc[food_id]['name']}, Order Count: {order_count}")
    print('\n')
# Example: Display recommendations when User 0 logs in
user_id_logged_in = 0
display_recommendations_on_login(user_id_logged_in)

user_ids = [0, 1, 2, 3]
for user in user_ids:
    display_recommendations_on_login(user)
