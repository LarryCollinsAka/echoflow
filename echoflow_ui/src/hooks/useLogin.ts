import { useNavigate } from "react-router-dom";
import API from "../lib/axios";
import { useCurrentUser } from "./useCurrentUser";
import type { User } from "../context/AuthContext";

type LoginPayload = {
  email: string;
  password: string;
};

export const useLogin = () => {
  const { login } = useCurrentUser();
  const navigate = useNavigate();

  const loginUser = async ({ email, password }: LoginPayload) => {
    try {
      // Step 1: Get JWT
      const tokenRes = await API.post("/auth/login", { email, password });
      const { access_token } = tokenRes.data;

      localStorage.setItem("token", access_token);

      // 👤 Step 2: Fetch user profile
      const meRes = await API.get<User>("/users/me");

      // Step 3: Set user in context
      login(meRes.data);

      // Step 4: Navigate to dashboard
      navigate("/dashboard");
    } catch (err: any) {
      console.error("Login failed:", err);
      throw err; // Let caller handle error
    }
  };

  return { loginUser };
};

