import React, { useState, useEffect } from 'react';
import { FaUser, FaCamera, FaTimes, FaCheck } from 'react-icons/fa';
import './EditUserModal.css';
import type { User, updateUser } from '../../../types/user';
import { userApi } from '../../../api/api';

interface EditUserModalProps {
  user: User;
  onClose: () => void;
  onSave: (updatedUser: any) => void;
}

const EditUserModal: React.FC<EditUserModalProps> = ({ user, onClose, onSave }) => {
  const [newUser, setNewUser] = useState<updateUser>({
    avatar: null,
    userName: user.userName,
    major: user.major,
    position: user.position,
    office: user.office,
  });
  const [avatarPreview, setAvatarPreview] = useState<string | null>(
    user.avatar && typeof user.avatar === 'string' ? user.avatar : null
  );
  const [isLoading, setIsLoading] = useState(false);
  const [loadingDots, setLoadingDots] = useState('.');

  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (isLoading) {
      interval = setInterval(() => {
        setLoadingDots(prev => {
          if (prev.length >= 3) return '.';
          return prev + '.';
        });
      }, 500);
    }
    return () => clearInterval(interval);
  }, [isLoading]);

  const handleAvatarChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setNewUser(prev => ({ ...prev, avatar: file }));
      
      const reader = new FileReader();
      reader.onload = (event) => {
        if (event.target?.result) {
          setAvatarPreview(event.target.result as string);
        }
      };
      reader.readAsDataURL(file);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setNewUser(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const formData = new FormData();
      if (newUser.avatar instanceof File) {
        formData.append('avatar', newUser.avatar);
      }
      formData.append('userName', newUser.userName || '');
      formData.append('major', newUser.major || '');
      formData.append('position', newUser.position || '');
      formData.append('office', newUser.office || '');

      const response = await userApi.updateUser(user.id, formData);
      onSave(response.data);
      onClose();
    } catch (error) {
      console.error('Error updating user:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="edit-user-modal-overlay">
      <div className="edit-user-modal-content">
        <div className="edit-user-modal-header">
          <h2 className="edit-user-modal-title">Edit User</h2>
          <button className="edit-user-close-btn" onClick={onClose}>
            <FaTimes />
          </button>
        </div>
        
        <form onSubmit={handleSubmit} className="edit-user-modal-body">
          <div className="edit-user-avatar-upload">
            {avatarPreview ? (
              <img src={avatarPreview} alt="Avatar" className="edit-user-avatar-preview" />
            ) : (
              <div className="edit-user-avatar-placeholder">
                <FaUser />
              </div>
            )}
            <label className="edit-user-avatar-upload-btn">
              <FaCamera /> Change Avatar
              <input
                type="file"
                accept="image/*"
                onChange={handleAvatarChange}
                hidden
              />
            </label>
          </div>

          <div className="edit-user-form-group">
            <label className="edit-user-form-label">Username</label>
            <input
              type="text"
              name="userName"
              placeholder="Enter username"
              value={newUser.userName || ""}
              onChange={handleChange}
              className="edit-user-form-control"
              required
            />
          </div>
          
          <div className="edit-user-form-group">
            <label className="edit-user-form-label">Major</label>
            <input
              type="text"
              name="major"
              placeholder="Enter major"
              value={newUser.major || ""}
              onChange={handleChange}
              className="edit-user-form-control"
              required
            />
          </div>
          
          <div className="edit-user-form-group">
            <label className="edit-user-form-label">Position</label>
            <input
              type="text"
              name="position"
              placeholder="Enter position"
              value={newUser.position || ""}
              onChange={handleChange}
              className="edit-user-form-control"
              required
            />
          </div>
          
          <div className="edit-user-form-group">
            <label className="edit-user-form-label">Office</label>
            <input
              type="text"
              name="office"
              placeholder="Enter office"
              value={newUser.office || ""}
              onChange={handleChange}
              className="edit-user-form-control"
              required
            />
          </div>

          <div className="edit-user-modal-actions">
            <button type="button" className="edit-user-cancel-btn" onClick={onClose}>
              Cancel
            </button>
            <button 
              type="submit" 
              className="edit-user-save-btn"
              disabled={isLoading}
            >
              {isLoading ? (
                <span>Loading{loadingDots}</span>
              ) : (
                <>
                  <FaCheck /> Save Changes
                </>
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default EditUserModal;