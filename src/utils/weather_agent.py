from langchain_core.tools import tool

@tool
def weather_agent(city_name: str):
    '''
    this tool will return the current weather or temperature for the given city

    Parameters:
    city_name (str): it is a city name.

    Returns:
    str: The weather of the given city.
    '''
    
    text = f"the weather at city {city_name} is currently sunny"
    return text