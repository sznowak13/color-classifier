class Result:
    def __init__(self, status, message, body):
        self.status = status
        self.message = message
        self.body = body

    def __repr__(self):
        return f'{self.status}: {self.message}'
