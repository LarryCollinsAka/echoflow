import React from "react";
import { UserRole } from "../../types/enums";
import { useCurrentUser } from "../../hooks/useCurrentUser";

export const RequireRole = ({
  roles,
  children,
}: {
  roles: UserRole[];
  children: JSX.Element;
}) => {
  const { user, isAuthenticated } = useCurrentUser();

  if (!isAuthenticated || !user || !roles.includes(user.role)) {
    return <div className="text-red-500 mt-4">⛔ Access Denied</div>;
  }

  return children;
};