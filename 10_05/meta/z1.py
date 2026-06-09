class Account:
    __allowed_fields = ["firstname", "lastname", "email"]

    def __init__(self, login, password, **kwargs):
        self.login = login
        self.password = password
        for key, value in kwargs.items():
            if key  in Account.__allowed_fields:
                setattr(self, key, value)
            else:
                raise ValueError("Klucz nie znajduje sie w liscie dozwolonych")

    def __str__(self):
        result = f"login: {self.login}\npassword: {self.password}\n"
        for key in Account.__allowed_fields:
            if hasattr(self, key):
                result += f"{key}: {getattr(self, key)}\n"
        return result


if __name__ == '__main__':
    account = Account("user", "12345", email = "user@gmail.com", firstname = "Marek", lastname = "Kowalski")
    print(account.login)
    print(account.email)
    print(account)