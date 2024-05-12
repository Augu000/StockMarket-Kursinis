import unittest
from unittest.mock import patch, MagicMock
from main import UserManager, User  # Adjust this import based on your actual file structure and naming

class TestUser(unittest.TestCase):
    def test_verify_password(self):
        user = User("testuser", "test@example.com", "password123")
        self.assertTrue(user.verify_password("password123"))
        self.assertFalse(user.verify_password("incorrect"))

class TestUserManager(unittest.TestCase):
    def setUp(self):
        # Reset the UserManager instance for each test to avoid state leakage
        UserManager._instance = None
        self.manager = UserManager()
        self.manager.users = {
            'testuser': User('testuser', 'test@example.com', 'password123')
        }

    @patch('builtins.print')
    def test_sign_in_success(self, mock_print):
        self.manager.sign_in('testuser', 'password123')
        mock_print.assert_any_call('Login successful.')  # Use assert_any_call to check among multiple prints

    @patch('builtins.print')
    def test_sign_in_failure(self, mock_print):
        self.manager.sign_in('wronguser', 'password123')
        mock_print.assert_called_with('User not found.')

    @patch('builtins.print')
    def test_add_user_already_exists(self, mock_print):
        self.manager.add_user('testuser', 'test@example.com', 'password123')
        mock_print.assert_called_with('User testuser already exists.')

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('json.dump')
    def test_save_users_to_file(self, mock_json_dump, mock_file):
        self.manager.save_users_to_file()
        mock_file.assert_called_once_with('users.json', 'w')
        mock_json_dump.assert_called()

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='{"testuser": {"username": "testuser", "email": "test@example.com", "password": "password123"}}')
    def test_load_users_from_file(self, mock_file):
        users = self.manager.load_users_from_file()
        self.assertIn('testuser', users)
        self.assertEqual(users['testuser']._email, 'test@example.com')

    @patch('requests.get')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_fetch_stock_data(self, mock_file, mock_get):
        mock_get.return_value = MagicMock()
        mock_get.return_value.json.return_value = {
            "c": 100, "h": 110, "l": 90, "o": 95, "pc": 92, "t": 1582641000
        }
        self.manager.fetch_stock_data()  # Assuming some user input handling if required
        mock_file.assert_called()  # Checks if file is attempted to be opened for writing

if __name__ == '__main__':
    unittest.main()
