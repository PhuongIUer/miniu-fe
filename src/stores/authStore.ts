// authStore.ts
import { create } from 'zustand';
import defaultAvatar from '../assets/ava.jpg';
import authApi from '../api/api'; // Import module API

interface Role {
  id: number;
  name: string;
}

interface AuthState {
  isLoggedIn: boolean;
  isBlocked: boolean;
  userId: number | null;
  userName: string;
  userAvatar: string;
  email: string;
  major: string;
  position: string;
  office: string;
  role: Role;
  fetchUserProfile: () => Promise<void>;
  logout: () => Promise<void>;
  isAdmin: () => boolean;
  isTeacher: () => boolean;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  isLoggedIn: false,
  isBlocked: false,
  userId: null,
  userName: '',
  userAvatar: defaultAvatar,
  email: '',
  major: '',
  position: '',
  office: '',
  role: { id: 0, name: '' },

  fetchUserProfile: async () => {
    try {
      const response = await authApi.getProfile();
      const userData = response.data;

      set({
        isLoggedIn: true,
        userId: userData.id || null,
        userName: userData.userName || '',
        userAvatar: userData.avatar || defaultAvatar,
        email: userData.email || '',
        major: userData.major || '',
        position: userData.position || '',
        office: userData.office || '',
        role: userData.role || { id: 0, name: '' },
      });
      
      localStorage.setItem('userAvatar', userData.avatar || defaultAvatar);
      localStorage.setItem('userName', userData.userName || 'ErrorLoadingName');
    } catch (error) {
      console.error('Error fetching user profile:', error);
      set({ isLoggedIn: false });
    }
  },

  logout: async () => {
    try {
      await authApi.logout();
      
      localStorage.removeItem('authToken');
      localStorage.removeItem('currentUser');
      set({
        isLoggedIn: false,
        userId: null,
        userName: '',
        userAvatar: defaultAvatar,
        email: '',
        major: '',
        position: '',
        office: '',
        role: { id: 0, name: '' },
      });
    } catch (error) {
      console.error('Error during logout:', error);
      // Vẫn clear local storage ngay cả khi logout API fail
      localStorage.removeItem('authToken');
      localStorage.removeItem('currentUser');
      set({
        isLoggedIn: false,
        userId: null,
        userName: '',
        userAvatar: defaultAvatar,
        email: '',
        major: '',
        position: '',
        office: '',
        role: { id: 0, name: '' },
      });
    }
  },

  isAdmin: () => get().role.name === 'admin',
  isTeacher: () => get().role.name === 'teacher',
}));