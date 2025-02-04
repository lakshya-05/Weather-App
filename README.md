# Weather-App
Simple weather app using api

### Purpose: 
The application retrieves and displays weather information for a given city.

### Data Source: 
It uses the OpenWeatherMap API to fetch weather data.

### Language: 
The application is written in Python.

### Input: 
The user provides the city name as input.

### Process:
- The application retrieves a pre-stored API key from the system's environment variables.
- It constructs a request to the OpenWeatherMap API, including the city name and the API key.
- It sends the request to the API.
- It receives a response from the API, containing weather data in JSON format.
- It parses the JSON response to extract relevant information:
    - Main weather condition (e.g., "Clouds", "Rain").
    - Detailed weather description (e.g., "scattered clouds", "light rain").
    - Current temperature in Fahrenheit.
    - Humidity level.
      
### Output: 
The application displays the extracted weather information to the user.

### Error Handling: 
If the API request fails (e.g., invalid city name), the application displays an error message.

### Security: 
The API key is stored as an environment variable, which is a more secure practice than embedding it directly in the code.
### Libraries Used:
requests: For making HTTP requests to the API.
os: For accessing environment variables.

### Units: 
The temperature is displayed in Fahrenheit.

### Use Cases:
- Quick weather checks for a user's current location or a location they plan to visit.
- Travel planning.
- Daily weather briefings.
- Educational tool for learning about APIs and JSON.
- Potential for integration with other applications (e.g., desktop widgets, home automation).
- Potential for weather monitoring with further development.

  
