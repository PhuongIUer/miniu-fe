// authStore.ts
import { create } from 'zustand';
import defaultAvatar from '../assets/ava.jpg';
import authApi from '../api/api';

interface Role {
  id: number;
  name: string;
}

interface AuthState {
  isLoggedIn: boolean;
  isBlocked: boolean;
  tokenExpired: boolean; // Thêm trạng thái token hết hạn
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
  isTokenExpired: () => boolean; // Hàm kiểm tra token hết hạn
}

export const useAuthStore = create<AuthState>((set, get) => ({
  isLoggedIn: false,
  isBlocked: false,
  tokenExpired: false, // Mặc định là false
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
        tokenExpired: false, // Reset trạng thái token khi fetch thành công
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
    } catch (error: any) {
      console.error('Error fetching user profile:', error);
      
      // Nếu lỗi 401 thì set tokenExpired = true
      if (error.response?.status === 401) {
        set({ tokenExpired: true });
      }
      
      set({ isLoggedIn: false });
    }
  },

  logout: async () => {
    try {
      await authApi.logout();
    } catch (error) {
      console.error('Error during logout:', error);
    } finally {
      localStorage.removeItem('authToken');
      localStorage.removeItem('currentUser');
      set({
        isLoggedIn: false,
        tokenExpired: false, // Reset khi logout
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
  isTokenExpired: () => get().tokenExpired, // Hàm kiểm tra token hết hạn
}));