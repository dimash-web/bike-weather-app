import React from 'react';

function BikeAdvice({ weather }) {
  const advice = weather.rain ? "It's raining, better to take public transport." : "Good day for biking!";

  return (
    <div>
      <p>{advice}</p>
    </div>
  );
}

export default BikeAdvice;
