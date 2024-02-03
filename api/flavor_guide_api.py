from flask import Flask, jsonify, request
from collabritive_filtering import top_similar_users, user_item_matrix, generate_recommendations

app = Flask(__name__)

# API endpoint to get recommendations for a user
@app.route('/get_recommendations', methods=['GET'])
def get_recommendations():
    user_id = int(request.args.get('user_id', default=-1))
    if user_id != -1:
        recommendations = generate_recommendations(user_id)
        response = {"user_id": user_id, "recommendations": recommendations.to_dict()}
        return jsonify(response)
    else:
        return jsonify({"error": "Invalid user_id"}), 400

@app.route('/feedback', methods=['POST'])
def handle_feedback():
    try:
        feedback_data = request.get_json()

        user_id = feedback_data['user_id']
        food_id = feedback_data['food_id']

        # Update the user-item matrix with the purchase count
        user_item_matrix.loc[user_id, food_id] += 1

        return jsonify({"message": "Feedback received and matrix updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5002)
