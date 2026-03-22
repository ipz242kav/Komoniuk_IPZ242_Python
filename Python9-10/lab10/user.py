class User:
    def __init__(self, first_name, last_name, email, nickname, newsletter=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.newsletter = newsletter
        self.login_attempts = 0

    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Користувач: {full_name}, Email: {self.email}, Нікнейм: {self.nickname}")
        return full_name

    def greeting_user(self):
        greeting = f"Привіт, {self.nickname}!"
        print(greeting)
        return greeting

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
