from surprise import Dataset, SVD
from surprise.model_selection import train_test_split

def generate_recommendations(user_id):
    # Load the dataset
    data = Dataset.load_builtin('ml-100k')
    trainset, testset = train_test_split(data, test_size=0.25)

    # Train the SVD algorithm
    algo = SVD()
    algo.fit(trainset)

    # Generate recommendations for the given user_id
    recommendations = []
    for item_id in range(1, 1683):  # Example item IDs
        prediction = algo.predict(user_id, str(item_id))
        recommendations.append((item_id, prediction.est))
    
    # Sort recommendations by estimated rating
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations[:10]
