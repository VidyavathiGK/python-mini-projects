class MovieWatchlist:
    def __init__(self):
        # Format: { "Movie Title": {"genre": "...", "watched": False} }
        self.watchlist = {}

    def add_movie(self):
        title = input("Enter movie title: ").strip().title()
        if title in self.watchlist:
            print("Movie is already in your watchlist.")
            return
        genre = input("Enter genre (e.g., Sci-Fi, Drama, Action): ").strip().capitalize()
        self.watchlist[title] = {"genre": genre, "watched": False}
        print(f"Added '{title}' to your watchlist!")

    def mark_watched(self):
        title = input("Enter movie title you watched: ").strip().title()
        if title in self.watchlist:
            self.watchlist[title]["watched"] = True
            print(f"Marked '{title}' as watched! 🎉")
        else:
            print("Movie not found in watchlist.")

    def view_watchlist(self):
        if not self.watchlist:
            print("Your watchlist is empty.")
            return

        print("\n--- My Movie Watchlist ---")
        for title, info in self.watchlist.items():
            status = "Watched ✅" else "To Watch 📌"
            print(f"• {title} ({info['genre']}) - [{status}]")


if __name__ == "__main__":
    mw = MovieWatchlist()
    while True:
        print("\n=== Movie Watchlist Menu ===")
        print("1. Add Movie")
        print("2. Mark Movie as Watched")
        print("3. View Watchlist")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            mw.add_movie()
        elif choice == "2":
            mw.mark_watched()
        elif choice == "3":
            mw.view_watchlist()
        elif choice == "4":
            print("Enjoy your movies!")
            break
        else:
            print("Invalid choice.")
