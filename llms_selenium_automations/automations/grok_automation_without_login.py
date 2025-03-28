from llms_selenium_automations.abc.llm_handler_abc import LLMHandlerABC
from llms_selenium_automations.exceptions import ConnectionFailedException
from llms_selenium_automations.logger import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class GrokAutomationWithoutLogin(LLMHandlerABC):
  """
  Class for automating Grok without login, using Selenium to interact with the web interface.
  """
  def __init__(self, driver: WebDriver, url="https://grok.com", logger=logger):
    """
    Initializes the automation instance.
    
    :param driver: Selenium WebDriver instance.
    :param url: Grok service URL.
    :param logger: Logger to record events.
    """
    self.url = url
    self.driver = driver
    self.logger = logger
    
    self.TAG = self.__class__.__name__
    self.TIMEOUT_IN_SECONDS = 60
    self.REST_TIME_IN_SECONDS = 0.5
    
    self.CHAT_SELECTOR = "textarea"
    self.MESSAGES_SELECTOR = ".relative.group.items-start"
    self.ERROR_SELECTOR = f"{self.MESSAGES_SELECTOR} > p.text-secondary.italic"
    self.END_BTN_SELECTOR = f"{self.MESSAGES_SELECTOR} > .flex.items-center > button"
  
  def launch(self) -> None:
    """
    Launches the Grok URL in the browser controlled by Selenium.
    """
    try:
      self.driver.get(self.url)
      self.logger.info(f"{self.TAG} - Successfully launched {self.url}")
    except Exception as e:
      self.logger.error(f"{self.TAG} - Launch error {e}")
      raise ConnectionFailedException()
  
  def delete_tokens(self) -> None:
    """
    Removes stored tokens from localStorage and reloads the page.
    """
    try:
      self.logger.info(f"{self.TAG} - Deleting tokens")
      self.driver.execute_script("localStorage.clear()")

      self.logger.info(f"{self.TAG} - Refreshing page")
      self.driver.refresh()
      
      self.logger.info(f"{self.TAG} - Waiting for page")
      WebDriverWait(self.driver, self.TIMEOUT_IN_SECONDS).until(
        EC.presence_of_element_located((By.TAG_NAME, self.MESSAGES_SELECTOR))
      )
    except Exception as e:
      self.logger.error("{self.TAG} - Delete tokens error {e}")
      raise
  
  def send_prompt(self, prompt: str) -> None:
    """
    Sends a text prompt to the Grok chatbot.
    
    :param prompt: Text of the prompt to be sent.
    """
    try:
      self.logger.info(f"{self.TAG} - Sending prompt: {prompt}")
      textarea_box = self.driver.find_element(By.TAG_NAME, self.CHAT_SELECTOR)
      self.driver.execute_script(f"arguments[0].value = '{prompt}';", textarea_box)
      textarea_box.send_keys(Keys.RETURN)
      textarea_box.submit()
      self.logger.info(f"{self.TAG} - Prompt submitted")
    except Exception as e:
      self.logger.error(f"{self.TAG} - Send prompt error {e}")
      raise
  
  def wait_to_finish_response(self):
    """
    Waits for the chatbot's response to be completed.
    """
    try:
      start_time = time.time()
      self.logger.info(f"{self.TAG} - Start waiting: {time.time()}")
      
      WebDriverWait(self.driver, self.TIMEOUT_IN_SECONDS).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, self.END_BTN_SELECTOR))
      )
      actual_time = time.time()
      self.logger.info(f"{self.TAG} - Total wait time {start_time - actual_time}")
      time.sleep(self.REST_TIME_IN_SECONDS)
    except Exception as e:
      self.logger.error("{self.TAG} - Wait to finish response error {e}")
      raise
  
  def request(self, prompt: str) -> str:
    """
    Makes a request to the Grok chatbot and returns the response.
    
    :param prompt: Text of the prompt to be sent.
    :return: Chatbot response.
    """
    try:
      self.delete_tokens()
      self.send_prompt(prompt)
      self.wait_to_finish_response()
    except Exception as e:
      self.logger.error(f"{self.TAG} - Error making request")
      raise
    
    try:
      last_response_element = self.driver.find_elements(By.CSS_SELECTOR, self.MESSAGES_SELECTOR)[-1]
      return last_response_element.text
    except Exception as e:
      self.logger.error(f"{self.TAG} - Error retrieving response")
      raise
  
  def quit(self) -> None:
    """
    Closes and terminates the Selenium WebDriver.
    """
    self.logger.info(f"{self.TAG} - Closing WebDriver")
    self.driver.close()
    self.driver.quit()
