# Heisenberg-AI

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Streamlit-based chatbot application that lets you interact with a fictional Walter White (Heisenberg) character from the popular TV series Breaking Bad.

## Overview

Heisenberg-AI is an interactive chatbot that simulates conversations with Walter White, the chemistry teacher turned methamphetamine manufacturer from Breaking Bad. The AI is designed to respond as Walter would, focusing primarily on chemistry-related topics while maintaining his distinctive personality.

## Features

- Real-time chat interface with Walter White's character
- Stylized message bubbles for a better chat experience
- Responses generated using the Microsoft MAI-DS-R1 AI model via OpenRouter
- Walter responds primarily to chemistry-related topics and questions about himself
- HTML-formatted responses for richer text display

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Yahya/Heisenberg-AI.git
   cd Heisenberg-AI
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install streamlit openai python-dotenv
   ```

4. Create a `.env` file in the project root with your OpenRouter API key:
   ```
   OPEN_ROUTER_API_KEY=your_openrouter_api_key
   ```

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run WalterWhite.py
   ```

2. Your browser should automatically open to `http://localhost:8501`

3. Start chatting with Walter White by typing messages in the input box and clicking "Send"

## Project Structure

- `WalterWhite.py` - Main Streamlit application that handles the chat interface
- `ai.py` - Backend module that interacts with the OpenRouter API to generate responses
- `.env` - Contains API key (not included in repository)
- `.gitignore` - Specifies files to be ignored by Git
- `LICENSE` - MIT license file
- `README.md` - This documentation file

## Configuration

The AI's behavior is defined in the system prompt within `ai.py`. You can modify this prompt to adjust Walter's personality or knowledge domains.

## API Usage

This application uses the OpenRouter API with the Microsoft MAI-DS-R1 model. You'll need to:

1. Sign up for an account at [OpenRouter](https://openrouter.ai/)
2. Generate an API key
3. Add the key to your `.env` file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This application is created for entertainment and educational purposes only. It simulates a fictional character and should not be used to generate harmful content or promote illegal activities.
