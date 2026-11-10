import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}  # { short_code: long_url }
        self.stats = {}    # { short_code: click_count }

    def shorten_url(self, long_url):
        if not long_url.startswith(("http://", "https://")):
            long_url = "https://" + long_url

        # Generate a random 6-character code
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        while code in self.url_map:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        self.url_map[code] = long_url
        self.stats[code] = 0
        short_link = f"http://short.ly/{code}"
        print(f"\nShortened link generated: {short_link}")
        return code

    def redirect(self, code):
        if code in self.url_map:
            self.stats[code] += 1
            print(f"\nRedirecting to: {self.url_map[code]}")
            print(f"Total visits: {self.stats[code]}")
        else:
            print("Error: Short URL code not found.")


if __name__ == "__main__":
    shortener = URLShortener()
    while True:
        print("\n=== URL Shortener Menu ===")
        print("1. Shorten Long URL")
        print("2. Simulate Visit (Redirect)")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            url = input("Enter long URL: ").strip()
            if url:
                shortener.shorten_url(url)
        elif choice == "2":
            code_input = input("Enter short code (e.g., Ab3Xy9): ").strip()
            shortener.redirect(code_input)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
