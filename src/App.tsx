import { createBrowserRouter, RouterProvider, Navigate } from "react-router-dom";
import MainLayout from "./layout/Mainlayout";
import LoginPage from "./screen/login/LoginPage";
import AdminPage from "./screen/admin/AdminPage";
import ProfilePage from "./screen/profile/ProfilePage";
import HomePage from "./screen/HomePage";
import ErrorPage from "./screen/error/ErrorPage";
import { useAuthStore } from "./stores/authStore";
import React from "react";
import type { ReactNode } from "react";

const ProtectedRoute = ({ children }: { children: ReactNode }) => {
  const authToken = localStorage.getItem('authToken');
  const { isLoggedIn } = useAuthStore();
  
  if (!authToken || !isLoggedIn) return <Navigate to="/login" replace />;
  
  return children;
};

const AdminProtectedRoute = ({ children }: { children: ReactNode }) => {
  const authToken = localStorage.getItem('authToken');
  const { isLoggedIn, role } = useAuthStore();
  
  if (!authToken || !isLoggedIn) return <Navigate to="/login" replace />;
  if (role?.name !== 'admin') return <Navigate to="/profile" replace />;
  
  return children;
};

const AuthRoute = ({ children }: { children: ReactNode }) => {
  const authToken = localStorage.getItem('authToken');
  const { isLoggedIn, role } = useAuthStore();
  
  if (authToken && isLoggedIn) {
    // Redirect based on role if already logged in
    return role?.name === 'admin' 
      ? <Navigate to="/admin" replace /> 
      : <Navigate to="/profile" replace />;
  }
  
  return children;
};

const RoleBasedRedirect = () => {
  const { role } = useAuthStore();
  
  return role?.name === 'admin' 
    ? <Navigate to="/admin" replace /> 
    : <Navigate to="/profile" replace />;
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      {
        index: true,
        element: <RoleBasedRedirect />,
      },
      {
        path: "login",
        element: (
          <AuthRoute>
            <LoginPage />
          </AuthRoute>
        ),
      },
      {
        path: "admin",
        element: (
          <AdminProtectedRoute>
            <AdminPage />
          </AdminProtectedRoute>
        ),
      },
      {
        path: "profile",
        element: (
          <ProtectedRoute>
            <ProfilePage />
          </ProtectedRoute>
        ),
      },
      // Thêm các route khác nếu cần
    ],
  },
  {
    path: "*",
    element: <ErrorPage />,
  },
]);

export default function App() {
  const { fetchUserProfile, isLoggedIn } = useAuthStore();
  
  React.useEffect(() => {
    // Only fetch profile if token exists
    if (localStorage.getItem('authToken') && !isLoggedIn) {
      fetchUserProfile();
    }
  }, [fetchUserProfile, isLoggedIn]);

  return <RouterProvider router={router} />;
}