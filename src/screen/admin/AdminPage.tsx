import React, { useState } from 'react';
import SideBar from './SideBar';
import UserManagement from './UserManagement/UserManagement';
import CurriculumManagement from './Curriculum/CurriculumManagement';
import './AdminPage.css';

const Admin: React.FC = () => {
  const [activeTab, setActiveTab] = useState('users');

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

export default Admin;