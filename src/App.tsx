import { createBrowserRouter, RouterProvider } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import LoginPage from "./screen/login/LoginPage";
import AdminPage from "./screen/admin/AdminPage";
import ProfilePage from "./screen/profile/ProfilePage";
import ErrorPage from "./screen/error/ErrorPage";
import { useAuthStore } from "./stores/authStore";
import React from "react";

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      {
        path: "login",
        element: <LoginPage />,
      },
      {
        path: "admin",
        element: <AdminPage />
      },
      {
        path: "profile",
        element: <ProfilePage />
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