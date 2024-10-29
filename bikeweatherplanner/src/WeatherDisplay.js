import axios from 'axios';
import React, { useEffect, useState } from 'react';

function WeatherDisplay() {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    const fetchWeather = async () => {
      try {
        const apiKey = process.env.REACT_APP_OPENWEATHER_API_KEY;
        const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather?q=NewYork&appid=${apiKey}`);
        setWeather(response.data);
      } catch (error) {
        console.error('Failed to fetch weather', error);
      }
    };

    fetchWeather();
  }, []);

  return (
    <div>
      {weather ? (
        <div>
          <p>Temperature: {(weather.main.temp - 273.15).toFixed(2)}°C</p>
          <p>Weather: {weather.weather[0].description}</p>
        </div>
      ) : <p>Loading...</p>}
    </div>
  );
}

export default WeatherDisplay;
