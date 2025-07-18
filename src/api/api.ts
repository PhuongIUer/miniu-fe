import axios from "axios";
import type { UserResponse } from '../types/response';
import type { newUser, access_token, User } from '../types/user'
import type { Subject, Curriculum } from '../types/curriculum'
import type { CurriculumResponse, MajorResponse, ConcentrationResponse, SemesterResponse, SubjectResponse} from '../types/response';
import type { RegisterResponse, responseLecturer } from '../types/lecturer'
import EnvironmentConfig from '../common/Environment';

const api = axios.create({
  baseURL: EnvironmentConfig.NGROK_BASE_URL,
  headers: {
    'ngrok-skip-browser-warning': 'true' 
  }
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      console.error('Unauthorized - có thể token hết hạn');
    }
    return Promise.reject(error);
  }
);

export const userApi = {
  getUserbyEmail: (email: string) => api.get<responseLecturer>(`/users/email/${email}`),
  getUsers: (page: number, limit: number) => 
    api.get<UserResponse>('/users', { params: { page, limit } }),
  updateUser: (id: number, data: Partial<any>) => api.patch(`/users/${id}/profile`, data),
  deleteUser: (id: number) => api.delete(`/auth/users/${id}`),
  createUser: (data: Partial<newUser>) => api.post<RegisterResponse>(`/auth/register`, data),
  updateCurrentUser: (data: FormData) => api.patch(`/users/current-profile`,{data}),
};
export const curriApi = {
  getLastedCurri: () => api.get<Curriculum>('/curricula/latest'),
  createCurri: (name: string) => api.post<CurriculumResponse>('/curricula', {name: name}),
  createMajor: (name: string, id: number) => api.post<MajorResponse>(`/majors/${id}`, {name: name}),
  createConcen: (name: string, id: number) => api.post<ConcentrationResponse>(`/concentrations/${id}`, {name: name}),
  createSems: (name: string, id: number) => api.post<SemesterResponse>(`/semesters/${id}`, {name: name}),
  createSub: (data: Partial<Subject>, id: number) => api.post<SubjectResponse>(`/subjects/${id}`, data),
}
export const authApi = {
  login: (email: string, password: string) => api.post<access_token>('/auth/login', {email, password}),
  getProfile: () => api.get<User>('/auth/profile'),
  logout: () => api.post('/auth/logout'),
  changePass: (
    currentPassword: string,  
    newPassword: string,  
    confirmPassword: string
  ) => api.post('/auth/change-password',{currentPassword, newPassword, confirmPassword}),
};

export default authApi;

