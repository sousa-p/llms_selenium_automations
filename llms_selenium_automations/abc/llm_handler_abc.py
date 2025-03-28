from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from llms_selenium_automations.logger import logger

class LLMHandlerABC(ABC):
  """Abstract base class for handling LLM-based chat automation using Selenium."""

  @abstractmethod
  def __init__(self, url: str, driver: WebDriver, logger=logger):
    """
    Initializes the LLM handler.

    Args:
      url (str): The URL of the chat interface.
      driver (WebDriver): The Selenium WebDriver instance.
    """
    pass

  @abstractmethod
  def launch(self) -> None:
    """
    Launches the chat interface by opening the specified URL.
    """
    pass

  @abstractmethod
  def get_conversation(self) -> list[str]:
    """
    Retrieves the conversation history as a list of messages.

    Returns:
      list[str]: The conversation history.
    """
    pass

  @abstractmethod
  def get_last_prompt(self) -> str:
    """
    Retrieves the last prompt sent by the user.

    Returns:
      str: The last user input.
    """
    pass

  @abstractmethod
  def get_last_response(self) -> str:
    """
    Retrieves the last response received from the chat.

    Returns:
      str: The last chatbot response.
    """
    pass

  @abstractmethod
  def send_prompt(self, prompt: str) -> None:
    """
    Sends a prompt to the chat interface.

    Args:
      prompt (str): The input text to be sent.
    """
    pass

  @abstractmethod
  def quit(self) -> None:
    """
    Closes the WebDriver and terminates the session.
    """
    pass
