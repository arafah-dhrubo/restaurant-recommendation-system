from main import RestaurantRecommendationSystem

def test_recommendation_system():
    recommendation_system = RestaurantRecommendationSystem()

    # Test case 1: Valid input
    user_input_1 = 'italian'
    assert recommendation_system.recommend_restaurants(user_input_1) == 'Restaurant A'

    # Test case 2: Valid input, multiple options
    user_input_2 = 'mexican'
    assert recommendation_system.recommend_restaurants(user_input_2) in ['Restaurant C']

    # Test case 3: Invalid input
    user_input_3 = 'indian'
    assert recommendation_system.recommend_restaurants(user_input_3) == 'No restaurants found for the given cuisine.'

    print("All test cases passed.")

if __name__ == "__main__":
    test_recommendation_system()