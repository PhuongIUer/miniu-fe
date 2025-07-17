import React, { useState } from 'react';
import { FaTimes, FaCheck } from 'react-icons/fa';
import './NewUserModal.css';
import type { newUser } from '../../../types/user';
import { userApi } from '../../../api/api';

interface NewUserModalProps {
  onClose: () => void;
  onCreate: (user: any) => void;
}

const NewUserModal: React.FC<NewUserModalProps> = ({ onClose, onCreate }) => {
  const [userData, setUserData] = useState<newUser>({
    email: '',
    password: '',
    userName: ''
  });

  const [isCreating, setIsCreating] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setUserData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsCreating(true);

    try {
      const createdUser = await userApi.createUser(userData);
      onCreate(createdUser);
      onClose();
    } catch (error) {
      console.error('Error creating user:', error);
      // Xử lý lỗi (hiển thị thông báo, etc.)
    } finally {
      setIsCreating(false);
    }
  };

  return (
    <div className="new-user-modal-overlay">
      <div className="new-user-modal-content">
        <div className="new-user-modal-header">
          <h2 className="new-user-modal-title">Create New User</h2>
          <button 
            className="new-user-close-btn" 
            onClick={onClose}
            disabled={isCreating}
          >
            <FaTimes />
          </button>
        </div>
        
        <form onSubmit={handleSubmit} className="new-user-modal-body">
          <div className="new-user-form-group">
            <label className="new-user-form-label">Email*</label>
            <input
              type="email"
              name="email"
              placeholder='Enter email'
              value={userData.email}
              onChange={handleChange}
              className="new-user-form-control"
              required
              disabled={isCreating}
            />
          </div>

          <div className="new-user-form-group">
            <label className="new-user-form-label">Username*</label>
            <input
              type="text"
              name="userName"
              placeholder='Enter username'
              value={userData.userName}
              onChange={handleChange}
              className="new-user-form-control"
              required
              disabled={isCreating}
            />
          </div>

          <div className="new-user-form-group">
            <label className="new-user-form-label">Password*</label>
            <input
              type="password"
              name="password"
              placeholder='Enter password'
              value={userData.password}
              onChange={handleChange}
              className="new-user-form-control"
              required
              disabled={isCreating}
            />
          </div>

          <div className="new-user-modal-actions">
            <button 
              type="button" 
              className="new-user-cancel-btn" 
              onClick={onClose}
              disabled={isCreating}
            >
              Cancel
            </button>
            <button 
              type="submit" 
              className="new-user-save-btn"
              disabled={isCreating}
            >
              {isCreating ? 'Creating...' : <><FaCheck /> Create User</>}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default NewUserModal;