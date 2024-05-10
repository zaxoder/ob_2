class User:
    def __init__(self, id, name, access_level):
        self.id = id
        self.name = name
        self.access_level = access_level

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_access_level(self):
        return self.access_level

class Admin(User):
    def __init__(self, id, name, access_level, admin_access):
        super().__init__(id, name, access_level)
        self.admin_access = admin_access

    def add_user(self, user):
        # Добавить пользователя в список пользователей
        pass

    def remove_user(self, user):

        pass

    def has_admin_access(self):
        return self.admin_access

admin = Admin(1, "Ivan", "Администратор", True)
user = User(2, "Анатолий", "Пользователь")

# Пример использования методов класса Admin
print(admin.has_admin_access())
admin.add_user(user)
print(len(admin.get_user()))
admin.remove_user(user)
print(len(admin.get_user()))