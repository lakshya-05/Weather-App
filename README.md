# Weather-App
Weather app using api and gui

### Purpose: 
The application retrieves and displays weather information for a given city.

### Data Source: 
It uses the OpenWeatherMap API to fetch weather data.

### Language: 
- The application is written in Python.
- The language used for input and output for the user is English.

### Input: 
The user provides the city name as input.

### Process:
- The application retrieves a pre-stored API key from the system's environment variables.
- It constructs a request to the OpenWeatherMap API, including the city name and the API key.
- It sends the request to the API.
- It receives a response from the API, containing weather data in JSON format.
- It parses the JSON response to extract relevant information:
    - Main weather condition (e.g., "Clouds", "Rain").
    - Icon representing the weather condition.
    - Detailed weather description (e.g., "scattered clouds", "light rain").
    - Current temperature in Fahrenheit.
    - Humidity level.
      
### Output: 
The application displays the extracted weather information to the user.

### Security: 
The API key is stored as an environment variable, which is a more secure practice than embedding it directly in the code.

### Modules Used:
- requests: For making HTTP requests to the API.
- os: For accessing environment variables.
- tkinter: For GUI.
- pillow: Loads, resizes, and displays images in Tkinter.

### Units: 
The temperature is displayed in Celsius.

### Use Cases:
- Quick weather checks for a user's current location or a location they plan to visit.
- Travel planning.
- Daily weather briefings.
- Educational tool for learning about APIs, GUI and JSON.
- Potential for integration with other applications (e.g., desktop widgets, home automation).
- Potential for weather monitoring with further development.

  
