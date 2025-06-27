import { useAuth } from './pages/auth/useAuth';

export default function Dashboard() {
  const { user } = useAuth();
  return (
    <div>
      <h1>Welcome, {user?.name}</h1>
      {user?.role === 'admin' && <AdminPanel />}
      {user?.role === 'user' && <UserFeatures />}
      {/* Add reviewer, guest, etc. as needed */}
    </div>
  );
}
function AdminPanel() {
  return <div>Admin controls: manage users, see analytics, etc.</div>;
}
function UserFeatures() {
  return <div>User workspace: meetings, summaries, actions, etc.</div>;
}