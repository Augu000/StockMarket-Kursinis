import json
import requests

class User:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    def verify_password(self, password):
        return self._password == password

    def display_info(self):
        print(f"Username: {self._username}, Email: {self._email}")

    def fetch_stock_data(self, data):
        raise NotImplementedError("Subclasses should implement this method to display specific stock data.")

class Developer(User):
    def fetch_stock_data(self, data):
        print("Developer Stock Data:", json.dumps(data, indent=4))

class Trader(User):
    def fetch_stock_data(self, data):
        print("Trader Stock Data: Current Price -", data.get("c"))

class UserManager:
    _instance = None

    def __new__(cls, users_file='users.json'):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.users_file = users_file
            cls._instance.users = cls._instance.load_users_from_file()
            cls._instance.current_user = None
        return cls._instance

    def create_user(self, type, username, email, password):
        if type == 'developer':
            return Developer(username, email, password)
        elif type == 'trader':
            return Trader(username, email, password)
        else:
            raise ValueError("Unknown user type")

    def add_user(self, type, username, email, password):
        if username not in self.users:
            user = self.create_user(type, username, email, password)
            self.users[username] = user
            self.save_users_to_file()
            print(f"{type.capitalize()} {username} added.")
        else:
            print(f"User {username} already exists.")

    def save_users_to_file(self):
        try:
            with open(self.users_file, 'w') as file:
                json.dump({username: {'username': user._username, 'email': user._email, 'password': user._password}
                           for username, user in self.users.items()}, file)
        except Exception as e:
            print(f"Failed to save user data: {e}")

    def load_users_from_file(self):
        try:
            with open(self.users_file, 'r') as file:
                data = json.load(file)
            return {username: self.create_user('developer', **user_data) if 'dev' in username else self.create_user('trader', **user_data)
                    for username, user_data in data.items()}
        except FileNotFoundError:
            print(f"{self.users_file} not found. Starting with an empty user database.")
            return {}
        except Exception as e:
            print(f"Failed to load user data: {e}")
            return {}

    def sign_in(self, username, password):
        user = self.users.get(username)
        if user is None:
            print("User not found.")
            return

        if user.verify_password(password):
            self.current_user = user
            print("Login successful.")
            # Fetch stock data and let the user object decide how to display it
            symbol = input("Please enter the stock symbol you are interested in (e.g., AAPL): ")
            api_key = 'co8she9r01qj5gtj88f0co8she9r01qj5gtj88fg'
            quote_url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"
            quote_response = requests.get(quote_url)
            quote_data = quote_response.json()
            self.current_user.fetch_stock_data(quote_data)
        else:
            print("Login failed. Incorrect password.")

    def display_users(self):
        for user in self.users.values():
            user.display_info()

# Example usage
if __name__ == "__main__":
    manager = UserManager()
    manager.add_user('ZMOGUS', 'cash', 'ZMOGUS@example.com', 'money123')
    manager.add_user('developer', 'dev', 'dev@example.com', 'code123')
    manager.sign_in('cash', 'money123')
    manager.sign_in('dev', 'code123')
