from abc import ABC, abdstractmethod
from selenium.webdriver.remote.webdriver import WebDriver

class LLMHandlerABC(ABC):
  @abstractmethod
  def __init__(self, url: str, driver: WebDriver):
    pass
  
  @abstractmethod
  def launch(self) -> None:
    pass
  
  @abstractmethod
  def get_coversation(self) -> list[str]:
    pass
  
  @abstractmethod
  def get_last_prompt(self) -> str:
    pass
  
  @abstractmethod
  def get_last_response(self) -> str:
    pass
  
  @abstractmethod
  def send_prompt(self, prompt: str) -> None:
    pass
  
  @abstractmethod
  def quit(self) -> None:
    pass
