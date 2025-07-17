import React, { useState, useEffect } from 'react';
import { FaUser, FaLock, FaEye, FaEyeSlash } from 'react-icons/fa';
import axios from 'axios';
import './LoginPage.css';
import { useAuthStore } from '../../stores/authStore';
import { useNavigate } from 'react-router-dom';

interface RememberedUser {
  email: string;
  password: string;
  rememberMe: boolean;
}

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  // Load remembered credentials
  useEffect(() => {
    const remembered = localStorage.getItem('rememberedUser');
    if (remembered) {
      const user: RememberedUser = JSON.parse(remembered);
      setEmail(user.email);
      setRememberMe(user.rememberMe);
    }
  }, []);

  const validateForm = (): boolean => {
    if (!email || !password) {
      setError('Please fill in all fields');
      return false;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setError('Please enter a valid email address');
      return false;
    }

    return true;
  };

  const handleLogin = async (e: React.FormEvent) => {
  e.preventDefault();
  setError('');
  
  if (!validateForm()) return;

  setIsLoading(true);

  try {
    const response = await axios.post('http://dfd0783d3578.ngrok-free.app/api/auth/login', {
      email,
      password
    });

    const accessToken = response.data.access_token;
    localStorage.setItem('authToken', accessToken);
    
    // Sử dụng auth store để cập nhật trạng thái
    const { fetchUserProfile } = useAuthStore.getState();
    await fetchUserProfile(); // Quan trọng: Cập nhật thông tin user sau khi login

    if (rememberMe) {
      localStorage.setItem('rememberedUser', JSON.stringify({ 
        email, 
        password, 
        rememberMe: true 
      }));
    } else {
      localStorage.removeItem('rememberedUser');
    }
    navigate('/profile'); // Redirect to profile page after successful login
  } catch (err: any) {
    const message = err.response?.data?.message || 'Login failed. Please try again.';
    setError(message);
    
    // Reset auth state nếu login thất bại
    useAuthStore.getState().logout();
  } finally {
    setIsLoading(false);
  }
};

  return (
    <div className="login-container">
      <div className="login-card">
        <div className="login-header">
          <h2 className="login-title">Welcome Back to <span className="miniu-text">MinIU</span></h2>
          <p className="login-subtitle">Please enter your email and password to login</p>
        </div>

        {error && <div className="login-error">{error}</div>}

        <form onSubmit={handleLogin} className="login-form">
          <div className="login-input-group">
            <FaUser className="login-icon" />
            <input
              type="email"
              placeholder="Email Address"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="login-input"
              autoComplete="username"
            />
          </div>

          <div className="login-input-group">
            <FaLock className="login-icon" />
            <input
              type={showPassword ? 'text' : 'password'}
              placeholder="Password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="login-input"
              autoComplete="current-password"
            />
            <button
              type="button"
              className="login-toggle-password"
              onClick={() => setShowPassword(!showPassword)}
            >
              {showPassword ? <FaEyeSlash /> : <FaEye />}
            </button>
          </div>

          <div className="login-options">
            <label className="remember-me">
              <input
                type="checkbox"
                checked={rememberMe}
                onChange={e => setRememberMe(e.target.checked)}
              />
              Remember me
            </label>
          </div>

          <button
            type="submit"
            className={`login-button ${isLoading ? 'login-button-loading' : ''}`}
            disabled={isLoading}
          >
            {isLoading ? 'Logging in...' : 'Login'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
