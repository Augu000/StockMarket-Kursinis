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
Polymorphism is an OOP concept where the same interface is used for different underlying forms (data types). In programming, it allows methods to do different things based on the object it is acting upon. In your Python code, polymorphism is primarily demonstrated through method overriding and dynamic method dispatch.


```python
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

Explanation of Polymorphism in the Snippet:
Method Overriding:

The fetch_stock_data method is defined in the User base class but is overridden in each of the subclasses (Developer and Trader). Each subclass has a different implementation of this method.
Developer and Trader both have a fetch_stock_data method that behaves differently: the Developer class formats the data as a JSON object for a detailed view, while the Trader class focuses on displaying the current price.
Dynamic Method Dispatch:

When you call the fetch_stock_data method on an object, Python determines which version of the method to execute based on the class of the object. This is a form of dynamic dispatch where the method that gets executed depends on the object instance, not the object type as declared.
This allows the same method call (user.fetch_stock_data(data)) to behave differently depending on what subclass of User the user object belongs to, thus utilizing polymorphism at runtime.

### Abstraction

Abstract Method:

fetch_stock_data is a method in the User class that doesn't have a concrete implementation but raises a NotImplementedError. This method acts as a placeholder, defining an interface or an expected behavior that all subclasses (like Developer and Trader) are expected to implement.
By declaring this method without a specific implementation, User class specifies what must be done (fetch and display stock data) but not how it should be done.
Abstraction of User Details:

The User class provides a simple interface (verify_password, display_info, and fetch_stock_data) to interact with user objects. The complexity of how user authentication or data display is handled internally is hidden from the user of the class.
This allows the user of the class to interact with objects of User and its subclasses without understanding the detailed implementations of how user credentials are verified or how stock data is processed.

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

    def fetch_stock_data(self, data):
        raise NotImplementedError("Subclasses should implement this method to display specific stock data.")

```




### Inheritance
Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit properties and methods from another class. In your code, inheritance is utilized to create specific types of users—Developer and Trader—that inherit from the base class User. This allows you to define common functionalities in the base class and extend or customize those functionalities in the derived classes.
``` python
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

class Developer(User):  # Inherits from User
    def fetch_stock_data(self, data):
        print("Developer Stock Data:", json.dumps(data, indent=4))

class Trader(User):  # Inherits from User
    def fetch_stock_data(self, data):
        print("Trader Stock Data: Current Price -", data.get("c"))

```
Base Class (User):

The User class defines common attributes like _username, _email, and _password, and common methods like verify_password and display_info.
It also declares a method fetch_stock_data that needs to be implemented by any subclass, which makes it an example of a polymorphic design where subclasses are expected to provide specific implementations.
Derived Classes (Developer and Trader):

Both Developer and Trader are subclasses of User. This means they inherit all the properties and methods of the User class.
They both provide their own implementation of the fetch_stock_data method, demonstrating how inherited methods can be overridden to provide specialized behavior depending on the subclass's needs.
Benefits of Using Inheritance in This Context:
Code Reusability: Common code related to user management is written once in the User class and reused in Developer and Trader.
Simplicity: Subclasses can override or extend the functionalities of the base class. This keeps the subclass code simple and focused on specific behavior.
Extensibility: It is easy to add new types of users by simply creating new subclasses of User without modifying the existing classes.

### Encapsulation

Encapsulation is a core concept in object-oriented programming that involves bundling the data (attributes) and methods that operate on the data into a single unit or class. This also often includes restricting direct access to some of an object's components, which is usually done by making some attributes or methods private, which means they can't be accessed from outside the class.

```python
class User:
    def __init__(self, username, email, password):
        self._username = username  # Private attribute
        self._email = email        # Private attribute
        self._password = password  # Private attribute

    def verify_password(self, password):
        # Public method to safely check password without exposing the actual password
        return self._password == password

    def display_info(self):
        # Public method that allows controlled access to view user information
        print(f"Username: {self._username}, Email: {self._email}")
```

## At least 2 Design Patterns




## Singleton 

The UserManager class implements the Singleton pattern. This design pattern ensures that a class has only one instance and provides a global point of access to it.<br>
The __new__ method is used to control the instantiation of the UserManager class. It checks if an instance already exists and if not, it creates one. This ensures that all parts of the application use the same instance of UserManager, which is crucial for coordinating actions across the system, such as managing user data.

```python
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

```python
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

```python
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

The code snippet for reading user data from a file is part of the load_users_from_file method in the UserManager class. This method attempts to open and read the users.json file, then parses the JSON data to reconstruct user objects.

```python
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
```

# Testing

# 3. 🟢 Results and Summary

✅ The program successfully fetches stock data from the Finnhub API and displays it to the user. <br>
✅ The program lets user to buy 

## How it would be possible to extend your application?
We could extend the application by adding additional features such as:
- Implementing a GUI for a more user-friendly interface.
- Allowing users to save favorite stocks and receive notifications for price changes.
- Incorporating more advanced stock analysis tools, such as technical indicators or sentiment analysis.


