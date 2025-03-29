# LLMs Selenium Automations

## Requirements

- Python 3.11 
- Selenium  
- A WebDriver compatible with your browser (ChromeDriver, GeckoDriver, etc.)  
- Recommended: Use an `undetectable chromedriver` to avoid detection and blocks  

### Available Methods

- `launch()`: Opens the Grok page in the browser.  
- `delete_tokens()`: Removes stored tokens from `localStorage` and reloads the page.  
- `send_prompt(prompt: str)`: Sends a prompt to the chatbot.  
- `wait_to_finish_response()`: Waits for the chatbot's response to complete.  
- `request(prompt: str) -> str`: Sends a prompt and returns the chatbot's response.  
- `quit()`: Closes and terminates the WebDriver session.  


## Contribution

Feel free to contribute with improvements. To do so:  

1. Fork the repository  
2. Create a new branch (`git checkout -b feature/new-feature`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the repository (`git push origin feature/new-feature`)  
5. Open a Pull Request  

## License

This project is licensed under the [MIT License](LICENSE).
