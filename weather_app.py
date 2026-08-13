import random
import time

def get_simulated_forecast(city):
    """Generates a random, simulated 3-day weather forecast for a city."""
    
    print(f"\n--- Generating a Simulated Forecast for {city} ---")
    
    # A list of possible weather conditions to choose from
    conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Rainy", "Windy", "Stormy"]
    
    # Simulate a 3-day forecast
    for i in range(3):
        # Determine the day's name
        if i == 0:
            day_name = "Today"
        elif i == 1:
            day_name = "Tomorrow"
        else:
            day_name = "The Day After Tomorrow"
            
        # Generate random weather data
        condition = random.choice(conditions)
        max_temp = random.randint(20, 35)  # Random max temp between 20 and 35 C
        min_temp = random.randint(10, max_temp - 5) # Random min temp, ensuring it's lower than max
        
        # Print the simulated forecast for the day
        print(f"\n{day_name}:")
        print(f"  - Condition: {condition}")
        print(f"  - Max Temp:  {max_temp}°C")
        print(f"  - Min Temp:  {min_temp}°C")
        
        # A small delay to make it feel like it's "calculating"
        time.sleep(0.5)

def main():
    """Main function to run the Offline Weather Simulator."""
    print("--- Welcome to the Offline Weather Simulator ---")
    print("Enter any city name to get a simulated forecast, or type 'quit' to exit.")
    
    while True:
        city = input("\nEnter a city name: ").strip()
        
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        
        if city:
            get_simulated_forecast(city)
        else:
            print("Please enter a city name.")

if __name__ == "__main__":
    main()
