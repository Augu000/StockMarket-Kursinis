# 1. 🟢 StockMarket application

## How to run the program?
To run the program, execute the Python script containing the provided code 

```
python main.py
```

## How to use the program?
Users can sign up by providing a username, email, and password. They can then sign in using their credentials. After signing in, they can fetch stock data by entering the stock symbol they are interested in.
If they like the price, they can perform BUY/SELL Multiple multiple stocks.

<br><br>

# 2. 🟢 Body/Analysis

## 4 OOP Pillars

### Polymotphism

### Abstraction

### Inheritance

### Encapsulation

## At least 2 Design Patterns



## Singleton 

The UserManager class implements the Singleton pattern. This design pattern ensures that a class has only one instance and provides a global point of access to it.<br>
The __new__ method is used to control the instantiation of the UserManager class. It checks if an instance already exists and if not, it creates one. This ensures that all parts of the application use the same instance of UserManager, which is crucial for coordinating actions across the system, such as managing user data.

```
class UserManager:
    _instance = None

    def __new__(cls, users_file='users.json'):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.users_file = users_file
            cls._instance.users = cls._instance.load_users_from_file()
            cls._instance.current_user = None
        return cls._instance

```

## Factory 

The create_user method in the UserManager class acts as a Factory method. This pattern provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. <br>
In your code, the create_user method decides which type of user (Developer or Trader) to instantiate based on the type argument. This method encapsulates the instantiation logic and decouples the code that generates the object from the code that uses the object.
```
def create_user(self, type, username, email, password):
    if type == 'developer':
        return Developer(username, email, password)
    elif type == 'trader':
        return Trader(username, email, password)
    else:
        raise ValueError("Unknown user type")
```

## Template 

In this example, fetch_stock_data is defined in the User class but raises NotImplementedError, indicating that it must be overridden. The Developer and Trader classes provide specific implementations of how they fetch and display stock data, which are different from each other.

```
class User:
    def fetch_stock_data(self, data):
        raise NotImplementedError("Subclasses should implement this method to display specific stock data.")

class Developer(User):
    def fetch_stock_data(self, data):
        print("Developer Stock Data:", json.dumps(data, indent=4))

class Trader(User):
    def fetch_stock_data(self, data):
        print("Trader Stock Data: Current Price -", data.get("c"))

```

## Reading from file and writting to file

# Testing

# 3. 🟢 Results and Summary

✅ The program successfully fetches stock data from the Finnhub API and displays it to the user. <br>
✅ The program lets user to buy 

## How it would be possible to extend your application?
We could extend the application by adding additional features such as:
- Implementing a GUI for a more user-friendly interface.
- Allowing users to save favorite stocks and receive notifications for price changes.
- Incorporating more advanced stock analysis tools, such as technical indicators or sentiment analysis.


