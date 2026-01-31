from mcp.server.fastmcp import FastMCP
from pydantic import Field
app = FastMCP(name='mcp_client', stateless_http=True)
 
 
population_data = {
    "pakistan": {"country": "Pakistan", "population": "241 million", "capital": "Islamabad"},
    "india": {"country": "India", "population": "1.43 billion", "capital": "New Delhi"},
    "usa": {"country": "USA", "population": "339 million", "capital": "Washington, D.C."},
    "china": {"country": "China", "population": "1.41 billion", "capital": "Beijing"},
    "france": {"country": "France", "population": "65 million", "capital": "Paris"},
}

@app.tool(name='get_population')
def get_population(country: str = Field(description='Country name for which to fetch population')):
    country_key = country.lower()
    if country_key not in population_data:
        raise ValueError(f"Population data for {country} is not available")
    return population_data[country_key]


  
weather_data = {
    "london": {"city": "London", "temperature": "15°C", "condition": "Cloudy", "humidity": "70%"},
    "paris": {"city": "Paris", "temperature": "18°C", "condition": "Sunny", "humidity": "60%"},
    "new york": {"city": "New York", "temperature": "22°C", "condition": "Rainy", "humidity": "75%"},
    "tokyo": {"city": "Tokyo", "temperature": "27°C", "condition": "Clear sky", "humidity": "55%"},
}


@app.tool(name='get_weather')
def get_weather(city: str = Field(description='City name for which to fetch the weather')):
    """
    Fetch weather for a given city from hardcoded values.
    """
    city_key = city.lower()
    if city_key not in weather_data:
        raise ValueError(f"Weather data for {city} is not available")
    return weather_data[city_key]



mcp_app = app.streamable_http_app()