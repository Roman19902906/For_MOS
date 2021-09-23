from For_MOS.tools.Json.path import Tools
class ConfigTools():

    # Корректный логин пользователя для входа
    @staticmethod
    def login():
        return Tools.data['login']

    # Корректный пароль пользователя для входа
    @staticmethod
    def password():
        return Tools.data['password']

    # Корректный логин пользователя для входа
    @staticmethod
    def login1():
        return Tools.data['login1']

    # Корректный пароль пользователя для входа
    @staticmethod
    def password1():
        return Tools.data['password1']
