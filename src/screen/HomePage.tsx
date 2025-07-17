import React from 'react';
import { useAuthStore } from '../stores/authStore';
import './HomePage.css';

const HomePage: React.FC = () => {
  const { userName, userAvatar, isAdmin, isTeacher } = useAuthStore();
  
  return (
    <div className="home-page">
      <header className="header">
        <div className="user-info">
          <img 
            src={userAvatar || '/default-avatar.jpg'} 
            alt="User Avatar" 
            className="avatar"
          />
          <h1>Welcome back, {userName}!</h1>
        </div>
      </header>

      <main className="main-content">
        <section className="welcome-section">
          <h2>Dashboard Overview</h2>
          <p>Here's what's happening today.</p>
        </section>

        <div className="cards-container">
          <div className="card">
            <h3>Recent Activities</h3>
            <p>Check your latest notifications and updates.</p>
          </div>

          <div className="card">
            <h3>Quick Actions</h3>
            <p>Access frequently used features quickly.</p>
          </div>

          {(isAdmin() || isTeacher()) && (
            <div className="card admin-card">
              <h3>Management</h3>
              <p>Access administrative tools and settings.</p>
            </div>
          )}
        </div>
      </main>

      <footer className="footer">
        <p>© 2023 My Application. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;