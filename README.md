# WEATHER-APP
Weather App - Python

This is a simple Python program that fetches the current weather temperature of any city using the WeatherAPI and reads it aloud using text-to-speech.

---

🛠️ Features:
- Takes city name as input
- Uses WeatherAPI to get current temperature in Celsius
- Uses `pyttsx3` to speak the weather aloud
- Prints the temperature in the console

---

📦 Requirements:
- Python 3.x
- requests
- json (built-in)
- pyttsx3

You can install the required libraries using:
pip install requests pyttsx3

---

📝 How to Use:
1. Run the script.
2. Enter the name of a city when prompted.
3. The program will:
   - Fetch the weather data
   - Print the temperature
   - Read the temperature aloud

---

🔐 API Key:
The script uses the WeatherAPI. You can get your free API key from:
https://www.weatherapi.com/

Replace the API key in the URL string with your own if needed:
`key=your_api_key`

---

🎤 Example Output:
Enter the name of city:
Lahore
The current weather in Lahore is 33.0 degrees

