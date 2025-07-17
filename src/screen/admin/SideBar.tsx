import React from 'react';
import { FaUsers, FaBook, FaChevronRight } from 'react-icons/fa';
import './SideBar.css';

interface SideBarProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

const SideBar: React.FC<SideBarProps> = ({ activeTab, setActiveTab }) => {
  return (
    <div className="admin-sidebar">
      <div className="sidebar-header">
        <h3>ADMIN PANEL</h3>
      </div>
      
      <nav className="sidebar-nav">
        <button 
          className={`nav-item ${activeTab === 'users' ? 'active' : ''}`}
          onClick={() => setActiveTab('users')}
        >
          <FaUsers className="nav-icon" />
          <span>User Management</span>
          <FaChevronRight className="nav-arrow" />
        </button>
        
        <button 
          className={`nav-item ${activeTab === 'curriculum' ? 'active' : ''}`}
          onClick={() => setActiveTab('curriculum')}
        >
          <FaBook className="nav-icon" />
          <span>Curriculum Management</span>
          <FaChevronRight className="nav-arrow" />
        </button>
      </nav>
    </div>
  );
};

export default SideBar;