from main import RestaurantRecommendationSystem as System

def run_recommendation_system():
    try:
        user_input = input("Enter the type of food you are looking for:\n")
        recommendation_system = System()
        recommendation = recommendation_system.recommend_restaurants(user_input)
        print(f"Recommended restaurant: {recommendation}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    run_recommendation_system()
