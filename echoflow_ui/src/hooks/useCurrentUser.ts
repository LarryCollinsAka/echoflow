import { useAuth } from "../context/AuthContext";
import API from "../lib/axios";

export const useCurrentUser = () => {
  const { user, setUser, isAuthenticated } = useAuth();

  const login = (newUser: typeof user) => {
    localStorage.setItem("user", JSON.stringify(newUser));
    setUser(newUser);
  };

  const logout = () => {
    localStorage.removeItem("user");
    setUser(null);
  };

  return { user, isAuthenticated, login, logout };
};