class EmptyChatException(Exception):
  def __init__(self, message="Error handling chat history", field=None):
    super().__init__(message)
    self.field = field


class ConnectionFailedException(Exception):
  def __init__(self, message="Error trying to connect to LLM site", field=None):
    super().__init__(message)
    self.field = field


class RequestFailedException(Exception):
  def __init__(self, message="Error requesting prompt", field=None):
    super().__init__(message)
    self.field = field
