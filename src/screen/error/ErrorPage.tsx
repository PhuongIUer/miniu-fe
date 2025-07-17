import React from 'react';
import './ErrorPage.css'; // Import file CSS

const ErrorPage: React.FC = () => {
  return (
    <div className="error-container">
      <div className="error-content">
        <h1 className="error-title">404</h1>
        <h2 className="error-subtitle">Oops! Page Not Found</h2>
        <p className="error-message">
          The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.
        </p>
        <a href="/" className="home-link">Go to Homepage</a>
      </div>
    </div>
  );
};

export default ErrorPage;