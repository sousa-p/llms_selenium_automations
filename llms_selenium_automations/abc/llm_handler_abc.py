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
  def send_prompt(self, prompt: str) -> None:
    """
    Sends a prompt to the chat interface.

    Args:
      prompt (str): The input text to be sent.
    """
    pass
  
  @abstractmethod
  def wait_to_finish_response(self) -> None:
    """
    Wait chat interface to finish prompt response.
    """
    pass

  
  @abstractmethod
  def request(self, prompt: str) -> str:
    """
    Requests a prompt to the chat interface.

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
