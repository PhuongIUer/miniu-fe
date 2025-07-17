import { useEffect } from "react";
import { createBrowserRouter, RouterProvider, Navigate } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import LoginPage from "./screen/login/LoginPage";
import AdminPage from "./screen/admin/AdminPage";
import ProfilePage from "./screen/profile/ProfilePage";
import ErrorPage from "./screen/error/ErrorPage";
import { useAuthStore } from "./stores/authStore";
import type { ReactNode } from "react";

// ======= Route Guards =======
const hasAuth = () => !!localStorage.getItem("authToken");

const ProtectedRoute = ({ children }: { children: ReactNode }) => {
  const { isLoggedIn } = useAuthStore();
  return hasAuth() && isLoggedIn ? <>{children}</> : <Navigate to="/login" replace />;
};

const AdminProtectedRoute = ({ children }: { children: ReactNode }) => {
  const { isLoggedIn, role } = useAuthStore();
  if (!hasAuth() || !isLoggedIn) return <Navigate to="/login" replace />;
  if (role?.name !== "admin") return <Navigate to="/profile" replace />;
  return <>{children}</>;
};

const AuthRoute = ({ children }: { children: ReactNode }) => {
  const { isLoggedIn, role } = useAuthStore();
  return hasAuth() && isLoggedIn ? (
    <Navigate to={role?.name === "admin" ? "/admin" : "/profile"} replace />
  ) : (
    <>{children}</>
  );
};

const RoleBasedRedirect = () => {
  const { role } = useAuthStore();
  return <Navigate to={role?.name === "admin" ? "/admin" : "/profile"} replace />;
};

// ======= Router Setup =======
const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      { index: true, element: <RoleBasedRedirect /> },
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
    ],
  },
  { path: "*", element: <ErrorPage /> },
]);

// ======= App Root =======
export default function App() {
  const { fetchUserProfile, isLoggedIn } = useAuthStore();

  useEffect(() => {
    if (hasAuth() && !isLoggedIn) {
      fetchUserProfile();
    }
  }, [fetchUserProfile, isLoggedIn]);

  return <RouterProvider router={router} />;
}
