tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City and country, e.g. London, UK"}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the internet for current events or general knowledge",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "summarize_pdf",
            "description": "Read a local PDF file to summarize its content",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {"type": "string", "description": "The local path to the PDF file"}
                },
                "required": ["file_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_expression",
            "description": "Calculate a math expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "The math expression, e.g., '15 * 92'"}
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_date_info",
            "description": "Get current date and time information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Context of the date query"}
                },
                "required": ["query"]
            }
        }
    }
]