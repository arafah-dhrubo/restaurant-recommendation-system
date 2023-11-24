import random

class RestaurantRecommendationSystem:
    def __init__(self):
        self.restaurants = {
            'Restaurant A': {'cuisine': 'Italian', 'rating': 4.5, 'proximity': 5},
            'Restaurant B': {'cuisine': 'Japanese', 'rating': 4.2, 'proximity': 3},
            'Restaurant C': {'cuisine': 'Mexican', 'rating': 4.0, 'proximity': 7},
            'Restaurant D': {'cuisine': 'Bengali', 'rating': 4.9, 'proximity': 8},
        }

    # Define a sorting function
    def sort_key(self, item):
        # Sorting based on rating (ascending) and proximity (descending)
        return (item[1]['rating'], -item[1]['proximity'])

    def recommend_restaurants(self, user_input):
        try:
            user_input = user_input.lower()
            
            filtered_restaurants = {}
            for name, info in self.restaurants.items():
                if user_input in info['cuisine'].lower():
                    filtered_restaurants[name] = info

            if not filtered_restaurants:
                raise ValueError("No restaurants found for the given cuisine.")

            # Convert the dictionary items to a list of tuples
            restaurant_tuples = list(filtered_restaurants.items())
            sorted_restaurants = sorted(restaurant_tuples, key=self.sort_key, reverse=True)
            for restaurant_name, restaurant_info in sorted_restaurants:
                print(f"{restaurant_name}: "
      f"\nCuisine - {restaurant_info['cuisine']}, "
      f"\nRating - {restaurant_info['rating']/5.0}, "
      f"\nProximity - {restaurant_info['proximity']}km from your home")

            # Return the top recommendation
            return sorted_restaurants[0][0]

        except ValueError as ve:
            return str(ve)