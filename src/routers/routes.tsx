import { lazy, Suspense } from "react";
import { Navigate, Outlet } from "react-router-dom";
import { useAuthStore } from "../stores/authStore";

// Lazy loading
const LoginPage = lazy(() => import("../screen/login/LoginPage"));
const AdminPage = lazy(() => import("../screen/admin/AdminPage"));
const ProfilePage = lazy(() => import("../screen/profile/ProfilePage"));
const MainLayout = lazy(() => import("../layouts/MainLayout"));
const ErrorPage = lazy(() => import("../screen/error/ErrorPage"));

// Route guards
const ProtectedRoute = () => {
  const { isLoggedIn } = useAuthStore();
  return isLoggedIn ? <Outlet /> : <Navigate to="/login" replace />;
};

const AdminRoute = () => {
  const { isLoggedIn, role } = useAuthStore();
  if (!isLoggedIn) return <Navigate to="/login" replace />;
  if (role?.name !== "admin") return <Navigate to="/profile" replace />;
  return <Outlet />;
};

const AuthOnlyRoute = () => {
  const { isLoggedIn, role } = useAuthStore();
  return isLoggedIn ? <Navigate to={role?.name === "admin" ? "/admin" : "/profile"} replace /> : <Outlet />;
};

const RoleRedirect = () => {
  const { role } = useAuthStore();
  return <Navigate to={role?.name === "admin" ? "/admin" : "/profile"} replace />;
};

// Export routes
export const routes = [
  {
    path: "/",
    element: (
      <Suspense fallback={<div>Loading...</div>}>
        <MainLayout />
      </Suspense>
    ),
    children: [
      { index: true, element: <RoleRedirect /> },
      {
        element: <AuthOnlyRoute />,
        children: [{ path: "login", element: <LoginPage /> }],
      },
      {
        element: <ProtectedRoute />,
        children: [{ path: "profile", element: <ProfilePage /> }],
      },
      {
        element: <AdminRoute />,
        children: [{ path: "admin", element: <AdminPage /> }],
      },
    ],
  },
  { path: "*", element: <ErrorPage /> },
];
