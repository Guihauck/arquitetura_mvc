class HttpUnprocessableEntityError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.statuscode = 422
        self.name = "UnprocessableEntity"
        self.message = message
