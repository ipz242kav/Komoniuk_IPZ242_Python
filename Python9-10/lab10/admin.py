from user import User


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Привілеї адміністратора:")
        for priv in self.privileges:
            print(f"  - {priv}")
        return self.privileges


class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, newsletter=False, privileges=None):
        super().__init__(first_name, last_name, email, nickname, newsletter)
        if privileges is None:
            privileges = [
                "Allowed to add message",
                "Allowed to delete users",
                "Allowed to ban users"
            ]
        self.priv = Privileges(privileges)

    def show_privileges(self):
        return self.priv.show_privileges()
