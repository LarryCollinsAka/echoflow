import React from "react";
import { Stack, Nav } from "@fluentui/react";
import { useCurrentUser } from "../../hooks/useCurrentUser";
import { UserRole } from "../../types/enums";

const Sidebar = () => {
  const { user } = useCurrentUser();
  const role = user?.role;

  const links = [
    { key: "dashboard", name: "Dashboard", url: "/dashboard" },
    ...(role === UserRole.ADMIN
      ? [{ key: "users", name: "Manage Users", url: "/admin/users" }]
      : []),
    ...(role && role !== UserRole.STUDENT
      ? [{ key: "summaries", name: "Summaries", url: "/summaries" }]
      : []),
  ];

  return (
    <Stack styles={{ root: { width: 220, background: "#f9f9f9", paddingTop: 10 } }}>
      <Nav groups={[{ links }]} />
    </Stack>
  );
};

export default Sidebar;