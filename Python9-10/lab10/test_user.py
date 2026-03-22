import unittest
from user import User
from admin import Admin, Privileges


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Олексій", "Коваленко", "alex@test.com", "alex_k", True)

    def test_user_creation(self):
        self.assertEqual(self.user.first_name, "Олексій")
        self.assertEqual(self.user.last_name, "Коваленко")
        self.assertEqual(self.user.email, "alex@test.com")
        self.assertEqual(self.user.nickname, "alex_k")
        self.assertTrue(self.user.newsletter)

    def test_login_attempts_initial(self):
        self.assertEqual(self.user.login_attempts, 0)

    def test_increment_login_attempts(self):
        self.user.increment_login_attempts()
        self.user.increment_login_attempts()
        self.user.increment_login_attempts()
        self.assertEqual(self.user.login_attempts, 3)

    def test_reset_login_attempts(self):
        self.user.increment_login_attempts()
        self.user.increment_login_attempts()
        self.user.reset_login_attempts()
        self.assertEqual(self.user.login_attempts, 0)

    def test_describe_user(self):
        full_name = self.user.describe_user()
        self.assertEqual(full_name, "Олексій Коваленко")

    def test_greeting_user(self):
        greeting = self.user.greeting_user()
        self.assertEqual(greeting, "Привіт, alex_k!")


class TestPrivileges(unittest.TestCase):
    def test_privileges_creation(self):
        priv = Privileges(["add", "delete"])
        self.assertEqual(len(priv.privileges), 2)

    def test_privileges_empty(self):
        priv = Privileges()
        self.assertEqual(priv.privileges, [])

    def test_show_privileges(self):
        priv = Privileges(["Allowed to add message"])
        result = priv.show_privileges()
        self.assertIn("Allowed to add message", result)


class TestAdmin(unittest.TestCase):
    def setUp(self):
        self.admin = Admin("Адмін", "Системний", "admin@test.com", "superadmin")

    def test_admin_inherits_user(self):
        self.assertIsInstance(self.admin, User)

    def test_admin_has_privileges(self):
        self.assertIsNotNone(self.admin.priv)
        self.assertIsInstance(self.admin.priv, Privileges)

    def test_admin_default_privileges(self):
        privileges = self.admin.show_privileges()
        self.assertEqual(len(privileges), 3)
        self.assertIn("Allowed to add message", privileges)

    def test_admin_custom_privileges(self):
        admin = Admin("Test", "Admin", "t@t.com", "test", privileges=["Custom privilege"])
        privileges = admin.show_privileges()
        self.assertEqual(len(privileges), 1)
        self.assertIn("Custom privilege", privileges)


if __name__ == '__main__':
    unittest.main()
