import { useEffect } from "react";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { useAuthStore } from "./stores/authStore";
import { routes } from "./routers/routes";

const router = createBrowserRouter(routes);

export default function App() {
  const { fetchUserProfile, isLoggedIn } = useAuthStore();

  useEffect(() => {
    if (localStorage.getItem("authToken") && !isLoggedIn) {
      fetchUserProfile();
    }
  }, [fetchUserProfile, isLoggedIn]);

  return <RouterProvider router={router} />;
}
