class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут
        self._name = name  # Защищенный атрибут
        self._access_level = 'user'  # Защищенный атрибут, по умолчанию для всех пользователей

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level

class Admin(User):  # Наследование от класса User
    def __init__(self, user_id, name):
        super().__init__(user_id, name)  # Инициализация базового класса
        self._access_level = 'admin'  # Изменение уровня доступа для администратора

    def add_user(self, users_list, user): # добавление нового пользователя
        if user not in users_list:
            users_list.append(user)
            print(f"User {user.get_name()} added successfully.")
        else:
            print("User already exists.")

    def remove_user(self, users_list, user):
        if user in users_list:
            users_list.remove(user)
            print(f"User {user.get_name()} removed successfully.")
        else:
            print("User not found.")




# Создаем список пользователей
users_list = []

# Создаем администратора
admin = Admin(user_id="admin01", name="Admin User")

# Создаем обычных пользователей
user1 = User(user_id="user01", name="John Doe")
user2 = User(user_id="user02", name="Jane Doe")

# Администратор добавляет пользователей в список
admin.add_user(users_list, user1)
admin.add_user(users_list, user2)

# Попытка добавить пользователя, который уже существует
admin.add_user(users_list, user1)

# Показываем текущих пользователей
print("Current users:")
for user in users_list:
    print(f"- {user.get_name()}")

# Администратор удаляет пользователя
admin.remove_user(users_list, user1)

# Попытка удалить пользователя, который уже был удален
admin.remove_user(users_list, user2)
admin.remove_user(users_list, user2)

# Показываем текущих пользователей после удаления
print("Users after removal:")
for user in users_list:
    print(f"- {user.get_name()}")
