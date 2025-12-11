from tools.implementations import (
    get_weather,
    search_web,
    summarize_pdf,
    calculate_expression,
    get_date_info
)

# Mapping function names to actual python functions
AVAILABLE_FUNCTIONS = {
    "get_weather": get_weather,
    "search_web": search_web,
    "summarize_pdf": summarize_pdf,
    "calculate_expression": calculate_expression,
    "get_date_info": get_date_info,
}