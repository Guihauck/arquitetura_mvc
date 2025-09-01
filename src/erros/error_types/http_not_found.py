class HttpNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.statuscode = 404
        self.name = "NotFound"
        self.message = message
