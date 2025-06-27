import { useLogin } from "../hooks/useLogin";
import { useState } from "react";

export default function LoginForm() {
  const { loginUser } = useLogin();
  const [email, setEmail] = useState("admin@echoflow.com");
  const [password, setPassword] = useState("adminpassword");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await loginUser({ email, password });
    } catch {
      alert("Login failed");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4 max-w-md mx-auto mt-32">
      <h2 className="text-2xl font-bold text-center">EchoFlow Login</h2>
      <input value={email} onChange={(e) => setEmail(e.target.value)} className="input" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="input" />
      <button type="submit" className="btn">Login</button>
    </form>
  );
}