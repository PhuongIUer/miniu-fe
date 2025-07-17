import React, { useState, useEffect } from 'react';
import { FaUser, FaEnvelope, FaLock, FaCamera, FaSave, FaGraduationCap, FaBriefcase, FaBuilding, FaKey } from 'react-icons/fa';
import axios from 'axios';
import { useAuthStore } from '../../stores/authStore';
import './ProfilePage.css';
import { useNavigate } from 'react-router-dom';

const Profile: React.FC = () => {
  const {
    userName,
    email,
    userAvatar,
    major,
    position,
    office,
    fetchUserProfile
  } = useAuthStore();

  // Profile info states
  const [username, setUsername] = useState(userName);
  const [currentMajor, setCurrentMajor] = useState(major);
  const [currentPosition, setCurrentPosition] = useState(position);
  const [currentOffice, setCurrentOffice] = useState(office);
  const [avatar, setAvatar] = useState<string | null>(userAvatar);
  const [avatarFile, setAvatarFile] = useState<File | null>(null);
  const [isEditingInfo, setIsEditingInfo] = useState(false);
  const [isLoadingInfo, setIsLoadingInfo] = useState(false);
  const [infoError, setInfoError] = useState<string | null>(null);

  // Password change states
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isEditingPassword, setIsEditingPassword] = useState(false);
  const [isLoadingPassword, setIsLoadingPassword] = useState(false);
  const [passwordError, setPasswordError] = useState<string | null>(null);
  const [passwordSuccess, setPasswordSuccess] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetchUserProfile();
  }, [fetchUserProfile]);

  useEffect(() => {
    setUsername(userName);
    setCurrentMajor(major);
    setCurrentPosition(position);
    setCurrentOffice(office);
    setAvatar(userAvatar);
  }, [userName, major, position, office, userAvatar]);

  useEffect(() => {
    const authToken = localStorage.getItem('authToken');
    if (!authToken) {
      navigate('/login');
    }
  }, [navigate]);
  
  const handleAvatarChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setAvatarFile(file);
      const reader = new FileReader();
      reader.onloadend = () => {
        setAvatar(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleUpdateInfo = async (e: React.FormEvent) => {
    e.preventDefault();
    setInfoError(null);
    setIsLoadingInfo(true);

    try {
      const token = localStorage.getItem('authToken');
      if (!token) throw new Error('No authentication token found');

      const formData = new FormData();
      
      if (avatarFile) formData.append('avatar', avatarFile);
      if (username !== userName) formData.append('userName', username);
      if (currentMajor !== major) formData.append('major', currentMajor);
      if (currentPosition !== position) formData.append('position', currentPosition);
      if (currentOffice !== office) formData.append('office', currentOffice);
      
      const response = await axios.patch(
        'http://localhost:3000/api/users/current-profile',
        formData,
        {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'multipart/form-data'
          }
        }
      );

      if (response.status === 200) {
        await fetchUserProfile();
        setIsEditingInfo(false);
      }
    } catch (error) {
      console.error('Error updating profile:', error);
      setInfoError('Failed to update profile. Please try again.');
    } finally {
      setIsLoadingInfo(false);
    }
  };

  const handleUpdatePassword = async (e: React.FormEvent) => {
    e.preventDefault();
    setPasswordError(null);
    setPasswordSuccess(null);

    if (newPassword !== confirmPassword) {
      setPasswordError("New passwords don't match!");
      return;
    }

    setIsLoadingPassword(true);

    try {
      const token = localStorage.getItem('authToken');
      if (!token) throw new Error('No authentication token found');

      const response = await axios.post(
        'http://localhost:3000/api/auth/change-password',
        {
          currentPassword,
          newPassword,
          confirmPassword
        },
        {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          }
        }
      );

      if (response.status === 200) {
        setPasswordSuccess('Password has been changed successfully');
        setCurrentPassword('');
        setNewPassword('');
        setConfirmPassword('');
        setIsEditingPassword(false);
      }
    } catch (error: any) {
      console.error('Error changing password:', error);
      if (error.response?.status === 400) {
        setPasswordError(error.response.data.message || 'Invalid data or current password is incorrect');
      } else if (error.response?.status === 401) {
        setPasswordError('Unauthorized - Please login again');
      } else {
        setPasswordError('Failed to change password. Please try again.');
      }
    } finally {
      setIsLoadingPassword(false);
    }
  };

  const toggleEditInfo = () => {
    setIsEditingInfo(!isEditingInfo);
    if (isEditingInfo) {
      setUsername(userName);
      setCurrentMajor(major);
      setCurrentPosition(position);
      setCurrentOffice(office);
      setAvatar(userAvatar);
      setAvatarFile(null);
      setInfoError(null);
    }
  };

  const toggleEditPassword = () => {
    setIsEditingPassword(!isEditingPassword);
    if (isEditingPassword) {
      setCurrentPassword('');
      setNewPassword('');
      setConfirmPassword('');
      setPasswordError(null);
      setPasswordSuccess(null);
    }
  };

  return (
    <div className="profile-container">
      <div className="profile-card">
        <div className="profile-header">
          <h2>My Profile</h2>
        </div>

        <div className="profile-section">
          <div className="section-header">
            <h3>Profile Information</h3>
            <button 
              onClick={toggleEditInfo}
              className={`edit-button ${isEditingInfo ? 'cancel-button' : ''}`}
              disabled={isLoadingInfo}
            >
              {isLoadingInfo ? 'Saving...' : isEditingInfo ? 'Cancel' : 'Edit Info'}
            </button>
          </div>

          {infoError && <div className="error-message">{infoError}</div>}

          <form onSubmit={handleUpdateInfo}>
            <div className="avatar-upload">
              <div className="avatar-preview">
                <img src={avatar || userAvatar} alt="Avatar" />
                {isEditingInfo && (
                  <label className="avatar-edit">
                    <FaCamera />
                    <input 
                      type="file" 
                      accept="image/*" 
                      onChange={handleAvatarChange} 
                      hidden 
                    />
                  </label>
                )}
              </div>
            </div>

            <div className="form-group">
              <label><FaEnvelope /> Email</label>
              <input 
                type="email" 
                value={email} 
                disabled 
                className="form-input" 
              />
            </div>
                
            <div className="form-group">
              <label><FaUser /> Username</label>
              <input
                type="text"
                value={username}
                onChange={e => setUsername(e.target.value)}
                className="form-input"
                disabled={!isEditingInfo}
                required
              />
            </div>

            <div className="form-group">
              <label><FaGraduationCap /> Major</label>
              <input
                type="text"
                value={currentMajor}
                onChange={e => setCurrentMajor(e.target.value)}
                className="form-input"
                disabled={!isEditingInfo}
              />
            </div>

            <div className="form-group">
              <label><FaBriefcase /> Position</label>
              <input
                type="text"
                value={currentPosition}
                onChange={e => setCurrentPosition(e.target.value)}
                className="form-input"
                disabled={!isEditingInfo}
              />
            </div>

            <div className="form-group">
              <label><FaBuilding /> Office</label>
              <input
                type="text"
                value={currentOffice}
                onChange={e => setCurrentOffice(e.target.value)}
                className="form-input"
                disabled={!isEditingInfo}
              />
            </div>

            {isEditingInfo && (
              <button type="submit" className="save-button" disabled={isLoadingInfo}>
                <FaSave /> {isLoadingInfo ? 'Saving...' : 'Save Profile'}
              </button>
            )}
          </form>
        </div>

        <div className="profile-section password-section">
          <div className="section-header">
            <h3>Password Settings</h3>
            <button 
              onClick={toggleEditPassword}
              className={`edit-button ${isEditingPassword ? 'cancel-button' : ''}`}
              disabled={isLoadingPassword}
            >
              {isLoadingPassword ? 'Saving...' : isEditingPassword ? 'Cancel' : 'Change Password'}
            </button>
          </div>

          {passwordError && <div className="error-message">{passwordError}</div>}
          {passwordSuccess && <div className="success-message">{passwordSuccess}</div>}

          {isEditingPassword && (
            <form onSubmit={handleUpdatePassword}>
              <div className="form-group">
                <label><FaLock /> Current Password</label>
                <input
                  type="password"
                  value={currentPassword}
                  onChange={e => setCurrentPassword(e.target.value)}
                  className="form-input"
                  placeholder="Enter current password"
                  required
                />
              </div>

              <div className="form-group">
                <label><FaKey /> New Password</label>
                <input
                  type="password"
                  value={newPassword}
                  onChange={e => setNewPassword(e.target.value)}
                  className="form-input"
                  placeholder="Enter new password"
                  required
                />
              </div>

              <div className="form-group">
                <label><FaKey /> Confirm Password</label>
                <input
                  type="password"
                  value={confirmPassword}
                  onChange={e => setConfirmPassword(e.target.value)}
                  className="form-input"
                  placeholder="Confirm new password"
                  required
                />
              </div>

              <button type="submit" className="save-button" disabled={isLoadingPassword}>
                <FaSave /> {isLoadingPassword ? 'Updating...' : 'Update Password'}
              </button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};

export default Profile;