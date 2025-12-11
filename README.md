Here is the updated README.md that reflects the new modular file structure.

code
Markdown
download
content_copy
expand_less
# Mini Knowledge Agent (Modular CLI)

A command-line AI assistant built with Python and OpenAI. This agent is designed to intelligently "route" user queries to specific tools (Weather, Web Search, Math, PDF Summarization) using OpenAI's Function Calling capabilities.

This project uses a **modular architecture**, separating configuration, tool logic, and the main execution loop for better maintainability.

## 🚀 Features

*   **Weather**: Fetches real-time weather data using OpenWeatherMap.
*   **Web Search**: Performs live internet searches using Tavily.
*   **PDF Summarization**: Reads local PDF files and generates summaries.
*   **Math**: Safely evaluates mathematical expressions.
*   **Date & Time**: Provides current date, time, and day information.
*   **Logging**: Automatically logs all tool usage and errors to `agent.log`.

## 📂 Project Structure

```text
mini_agent/
│
├── main.py                 # Entry point (Run this file)
├── config.py               # API key loading and client initialization
├── requirements.txt        # Python dependencies
├── .env                    # Secrets (API Keys)
│
├── tools/                  # Tool logic package
│   ├── __init__.py
│   ├── schemas.py          # JSON definitions sent to OpenAI
│   ├── implementations.py  # Actual Python functions (The "Hands")
│   └── registry.py         # Maps schemas to functions
│
└── utils/                  # Utilities package
    ├── __init__.py
    └── logger.py           # Logging configuration
🛠️ Prerequisites

Python 3.8+ installed.

API Keys:

OpenAI API Key: For the LLM (Brain).

OpenWeatherMap API Key: For weather data (Free tier available).

Tavily API Key: For web search (Free tier available).

📥 Installation & Setup

Clone or Download this repository.

Install Dependencies:
Run the following command in your terminal:

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt

Configure Environment Variables:
Create a file named .env in the root directory. Add your keys as follows:

code
Env
download
content_copy
expand_less
OPENAI_API_KEY=sk-proj-your-openai-key-here
OPENWEATHER_API_KEY=your-openweather-key-here
TAVILY_API_KEY=tvly-your-tavily-key-here
🏃 Usage

To start the agent, run the main.py file:

code
Bash
download
content_copy
expand_less
python main.py
Example Queries

Once the agent is running, try these inputs:

Weather: "What is the weather like in London right now?"

Search: "Who won the latest F1 race?"

Math: "Calculate 15 * 24 + 100"

Date: "What day of the week is it?"

PDF: "Summarize the file named document.pdf"

Note: Ensure document.pdf exists in the same folder as main.py.

📝 Logging

The agent automatically creates a file named agent.log in the root directory.

This file records timestamps, which tools were triggered, and any errors that occurred.

Useful for debugging if a tool fails to run.

⚠️ Limitations

PDF Reading: To save tokens and costs, the agent is currently configured to read only the first 3 pages of a PDF.

Math Safety: The math tool uses a restricted environment but should still be used with standard arithmetic expressions.

📜 License

This project is open-source and available for educational purposes.

code
Code
download
content_copy
expand_less