class LoginException(Exception):
    def __init__(self, mensaje):
        super(LoginException, self).__init__(mensaje)
