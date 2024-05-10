class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'Пользователь'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def __str__(self):
        return f"ID: {self._user_id}, Имя: {self._name}, Права доступа: {self._access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'Администратор'
        self._users_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users_list.append(user)
            print(f"Пользователь {user.get_name()} успешно добавлен.")
        else:
            print("Нет пользователя с таким именем.")

    def remove_user(self, user_id):
        for user in self._users_list:
            if user.get_user_id() == user_id:
                self._users_list.remove(user)
                print(f"Пользователь ID {user_id} успешно удален.")
                return
        print(f"Пользователь ID {user_id} не найден.")

    def list_users(self):
        for user in self._users_list:
            print(user)


if __name__ == "__main__":

    admin = Admin(1, "Виктор")
    print(admin)


    user1 = User(2, "Борис")
    user2 = User(3, "Иван")
    user3 = User(4, "Петр")

    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)

    admin.list_users()
    admin.remove_user(2)
    admin.list_users()