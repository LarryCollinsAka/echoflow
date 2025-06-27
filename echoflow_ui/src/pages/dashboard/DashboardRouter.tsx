import React from "react";
import { useCurrentUser } from "../../hooks/useCurrentUser";
import { UserRole } from "../../types/enums";
import AdminDashboard from "./AdminDashboard";
import OrganizerDashboard from "./OrganizerDashboard";
import AnalystDashboard from "./AnalystDashboard";
import ReporterDashboard from "./ReporterDashboard";
import StudentDashboard from "./StudentDashboard";

const DashboardRouter = () => {
  const { user } = useCurrentUser();

  if (!user) return <p>Loading dashboard...</p>;

  switch (user.role) {
    case UserRole.ADMIN:
      return <AdminDashboard />;
    case UserRole.ORGANIZER:
      return <OrganizerDashboard />;
    case UserRole.ANALYST:
      return <AnalystDashboard />;
    case UserRole.REPORTER:
      return <ReporterDashboard />;
    case UserRole.STUDENT:
    case UserRole.PERSONAL:
    default:
      return <StudentDashboard />;
  }
};

export default DashboardRouter;