# Chainlit-LiteLLM Chatbot

A simple and powerful chatbot built using Chainlit and LiteLLM, capable of integrating with multiple LLM providers including Groq and Google's Gemini.

## Features

- Interactive chat interface powered by Chainlit
- Support for multiple LLM providers:
  - Groq (llama3-8b-8192)
  - Google Gemini (gemini-1.5-flash)
- Easy configuration through environment variables
- Asynchronous message handling

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd chainlit-litellm-bot
```

2. Install the required dependencies:
```bash
pip install chainlit litellm python-dotenv google-auth
```

## Configuration

The project supports multiple LLM providers. You can choose which one to use by uncommenting the relevant section in the code.

### For Groq:
Create a `.env` file in the project root and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### For Google Gemini:
Create a `.env` file in the project root and add your Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

1. Start the chatbot:
```bash
chainlit run main.py
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

3. Start chatting with the bot!

## Project Structure

- `main.py` - Main application file with Groq integration
- `main2.py` - Alternative implementation using Google's Gemini
- `.env` - Environment variables configuration
- `README.md` - Project documentation

## API Configuration

### Groq Configuration
```python
model="llama3-8b-8192"
api_base="https://api.groq.com/openai/v1"
```

### Gemini Configuration
```python
model="gemini/gemini-1.5-flash"
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
