import Navbar from '../shared/Navbar';
import { Outlet } from 'react-router-dom';
import './MainLayout.css';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
const MainLayout = () => {
  const navigate = useNavigate();
    useEffect(() => {
      const authToken = localStorage.getItem('authToken');
      if (!authToken) {
        navigate('/login');
      }
    }, [navigate]);

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
