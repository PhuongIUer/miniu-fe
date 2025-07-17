import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronDown, faUser, faUserShield, faSignOutAlt } from '@fortawesome/free-solid-svg-icons';
import logo from '../assets/logo-full.png'
import defaultAvatar from '../assets/ava.jpg';
import './Navbar.css';
import { useAuthStore } from '../stores/authStore';

const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [showDropdown, setShowDropdown] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();
  const {
    isLoggedIn,
    userName,
    userAvatar,
    isAdmin,
    fetchUserProfile,
    logout
  } = useAuthStore();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 0);
    };

    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setShowDropdown(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    document.addEventListener('click', handleClickOutside);

    // Fetch user profile if token exists
    const token = localStorage.getItem('authToken');
    if (token) {
      fetchUserProfile();
    }

    return () => {
      window.removeEventListener('scroll', handleScroll);
      document.removeEventListener('click', handleClickOutside);
    };
  }, [fetchUserProfile]);

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  const setDefaultAvatar = (e: React.SyntheticEvent<HTMLImageElement>) => {
    e.currentTarget.src = defaultAvatar;
  };

  const handleProfile = () => {
    setShowDropdown(false);
    navigate('/profile');
  };

  const handleAdmin = () => {
    setShowDropdown(false);
    navigate('/admin');
  };

  const handleLogout = async () => {
    try {
      await logout();
      setShowDropdown(false);
      navigate('/login');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <nav className={`navbar ${isScrolled ? 'scrolled' : ''}`}>
      <div className="navbar-container">
        {/* Logo */}
        <div className="navbar-logo">
          <a href="/" className="logo-link">
            <img src={logo} alt="Logo" className="logo-img" />
            MinIu
          </a>
        </div>

        {/* Auth Section */}
        <div className="navbar-auth">
          {!isLoggedIn ? (
            <>
              {/* show-none */}
            </>
          ) : (
            <div className="user-profile">
              {/* User Avatar and Dropdown */}
              <div className="avatar-container" ref={dropdownRef} onClick={toggleDropdown}>
                <div className="avatar-wrapper">
                  <img
                    src={userAvatar || defaultAvatar}
                    onError={setDefaultAvatar}
                    alt="User Avatar"
                    className="avatar"
                  />
                  <div className="username-container">
                    <span className="username">{userName}</span>
                    <FontAwesomeIcon
                      icon={faChevronDown}
                      className="dropdown-icon"
                      style={{ transform: showDropdown ? 'rotate(180deg)' : 'none' }}
                    />
                  </div>
                </div>
                {/* Dropdown menu */}
                {showDropdown && (
                  <div className="dropdown-menu">
                    <button onClick={handleProfile} className="dropdown-item">
                      <FontAwesomeIcon icon={faUser} className="dropdown-icon-left" />
                      <span className="profile-text">Profile</span>
                    </button>
                    <div className="divider"></div>
                    {isAdmin() && (
                      <>
                        <button onClick={handleAdmin} className="dropdown-item">
                          <FontAwesomeIcon icon={faUserShield} className="dropdown-icon-left" />
                          <span className="admin-text">Admin</span>
                        </button>
                        <div className="divider"></div>
                      </>
                    )}
                    <button onClick={handleLogout} className="dropdown-item">
                      <FontAwesomeIcon icon={faSignOutAlt} className="dropdown-icon-left" />
                      <span className="logout-text">Logout</span>
                    </button>
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;