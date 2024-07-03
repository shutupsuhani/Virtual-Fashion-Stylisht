from src.recommendation import generate_recommendations

if __name__ == "__main__":
    user_id = '196'
    recommendations = generate_recommendations(user_id)
    print(recommendations)
