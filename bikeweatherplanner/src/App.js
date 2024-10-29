import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import WeatherDisplay from './WeatherDisplay';
import BikeAdvice from './BikeAdvice';
import Home from './Home';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/weather" element={<WeatherDisplay />} />
        <Route path="/advice" element={<BikeAdvice />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;
