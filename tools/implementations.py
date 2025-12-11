import json
import requests
import os
import math
import datetime
from pypdf import PdfReader
from config import OPENWEATHER_API_KEY, tavily_client
from utils.logger import logger

def get_weather(location):
    logger.info(f"Tool Triggered: get_weather for {location}")
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            return json.dumps({"location": location, "temperature": temp, "condition": weather_desc})
        else:
            return json.dumps({"error": "Location not found or API error."})
    except Exception as e:
        logger.error(f"Error in get_weather: {str(e)}")
        return json.dumps({"error": str(e)})

def search_web(query):
    logger.info(f"Tool Triggered: search_web for {query}")
    try:
        response = tavily_client.search(query)
        results = [{"title": res['title'], "content": res['content']} for res in response['results'][:2]]
        return json.dumps(results)
    except Exception as e:
        logger.error(f"Error in search_web: {str(e)}")
        return json.dumps({"error": str(e)})

def summarize_pdf(file_path):
    logger.info(f"Tool Triggered: summarize_pdf for {file_path}")
    try:
        if not os.path.exists(file_path):
            return json.dumps({"error": "File not found."})
            
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages[:3]: 
            text += page.extract_text() + "\n"
            
        return json.dumps({"content": text[:4000]})
    except Exception as e:
        logger.error(f"Error in summarize_pdf: {str(e)}")
        return json.dumps({"error": str(e)})

def calculate_expression(expression):
    logger.info(f"Tool Triggered: calculate_expression for {expression}")
    try:
        allowed_names = {"math": math, "abs": abs, "round": round}
        code = compile(expression, "<string>", "eval")
        for name in code.co_names:
            if name not in allowed_names:
                raise NameError(f"Use of {name} is not allowed")
        
        result = eval(code, {"__builtins__": {}}, allowed_names)
        return json.dumps({"expression": expression, "result": result})
    except Exception as e:
        logger.error(f"Error in calculate_expression: {str(e)}")
        return json.dumps({"error": "Invalid expression"})

def get_date_info(query):
    logger.info(f"Tool Triggered: get_date_info for {query}")
    now = datetime.datetime.now()
    return json.dumps({
        "current_datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "day_of_week": now.strftime("%A"),
        "day_of_year": now.timetuple().tm_yday
    })