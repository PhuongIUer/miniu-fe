import React from 'react';
import Navbar from '../shared/Navbar';
import { Outlet } from 'react-router-dom';
import './MainLayout.css';

const MainLayout: React.FC = () => {
  return (
    <div>
      <Navbar />
      <div className="container">
        <Outlet />
      </div>
    </div>
  );
};

export default MainLayout;
