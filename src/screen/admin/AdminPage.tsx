import React, { useState, useEffect } from 'react';
import SideBar from './SideBar';
import UserManagement from './UserManagement/UserManagement';
import CurriculumManagement from './Curriculum/CurriculumManagement';
import './AdminPage.css';
import { useAuthStore } from '../../stores/authStore';
import { useNavigate } from 'react-router-dom';

const AdminPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState('users');
  const { role } = useAuthStore();
  const navigate = useNavigate();

  useEffect(() => {
    if (role?.name !== 'admin') {
      navigate('/profile'); // Redirect to login if not admin
    }
  }, [role, navigate]);

  if (role?.name !== 'admin') {
    return null; // Or a loading spinner while redirect happens
  }

  return (
    <div className="admin-container">
      <SideBar activeTab={activeTab} setActiveTab={setActiveTab} />
      
      <div className="admin-content">
        {activeTab === 'users' && <UserManagement />}
        {activeTab === 'curriculum' && <CurriculumManagement />}
      </div>
    </div>
  );
};

export default AdminPage;