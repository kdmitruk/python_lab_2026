class Account:
    __allowed_fields = ["email", "first_name"]
    def __init__(self, login, password, **kwargs):
        self.login = login
        self.password = password
        for key, value in kwargs.items():
            if key in Account.__allowed_fields:
                setattr(self, key, value)
            else:
                raise ValueError(f"Klucz {key} nie znajduje się w liście dozwolonych kluczy")

    def __str__(self):
        results = [
            f"login: {self.login}",
            f"password: {self.password}",
        ]
        for key in Account.__allowed_fields:
            if hasattr(self, key):
                results.append(f"{key}: {getattr(self, key)}")
        return "\n".join(results)

if __name__ == '__main__':
    account = Account("user", "abc", email = "user@email.com")
    print(account)