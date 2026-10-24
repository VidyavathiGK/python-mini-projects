class Recipe:
    def __init__(self, title, prep_time, ingredients, instructions):
        self.title = title
        self.prep_time = prep_time
        self.ingredients = ingredients
        self.instructions = instructions

    def display_recipe(self):
        print(f"\n--- {self.title} ---")
        print(f"Prep Time: {self.prep_time} mins")
        print("Ingredients:")
        for item in self.ingredients:
            print(f"  - {item}")
        print(f"Instructions:\n{self.instructions}")


class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self):
        title = input("Enter recipe name: ").strip().title()
        if title in self.recipes:
            print("Recipe already exists!")
            return
        
        try:
            prep_time = int(input("Enter prep time (in minutes): "))
        except ValueError:
            print("Invalid prep time. Please enter a number.")
            return

        print("Enter ingredients (type 'done' when finished):")
        ingredients = []
        while True:
            ing = input("  -> Ingredient: ").strip()
            if ing.lower() == 'done':
                break
            if ing:
                ingredients.append(ing)

        instructions = input("Enter step-by-step instructions: ").strip()
        
        self.recipes[title] = Recipe(title, prep_time, ingredients, instructions)
        print(f"Recipe '{title}' added successfully!")

    def view_recipes(self):
        if not self.recipes:
            print("No recipes stored yet.")
            return
        print("\n--- Saved Recipes ---")
        for name in self.recipes:
            print(f"  * {name}")

    def search_recipe(self):
        query = input("Enter recipe name to search: ").strip().title()
        recipe = self.recipes.get(query)
        if recipe:
            recipe.display_recipe()
        else:
            print("Recipe not found.")


if __name__ == "__main__":
    book = RecipeBook()
    while True:
        print("\n=== Recipe Book Menu ===")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. Search Recipe")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            book.add_recipe()
        elif choice == "2":
            book.view_recipes()
        elif choice == "3":
            book.search_recipe()
        elif choice == "4":
            print("Happy cooking!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")
