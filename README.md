# 1. 🟢 Introduction

## a. StockMarket application

## b. How to run the program?
To run the program, execute the Python script containing the provided code 
```
python main.py
```

## c. How to use the program?
Users can sign up by providing a username, email, and password. They can then sign in using their credentials. After signing in, they can fetch stock data by entering the stock symbol they are interested in.

# 2. 🟢 Body/Analysis

## a. Explain how the program covers functional requirements
The program covers functional requirements by providing features for user management (adding users, signing in), fetching stock data (including stock quotes and recommendation trends), and saving fetched data to files.
<br>
<br>
## Code Snippets

### User Management Class
```python
class User:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    def verify_password(self, password):
        return self._password == password

    def display_info(self):
        print(f"Username: {self._username}, Email: {self._email}")








<br>
<br>
# 3. 🟢 Results and Summary

✅ The program successfully fetches stock data from the Finnhub API and displays it to the user. <br>
✅ The program demonstrates the successful implementation of user management and stock data fetching functionalities.

## c. How it would be possible to extend your application?
We could extend the application by adding additional features such as:
- Implementing a GUI for a more user-friendly interface.
- Allowing users to save favorite stocks and receive notifications for price changes.
- Incorporating more advanced stock analysis tools, such as technical indicators or sentiment analysis.

# 4. 🟢 Optional: Resources, references list.
No external resources or references were used in the development of this program.


