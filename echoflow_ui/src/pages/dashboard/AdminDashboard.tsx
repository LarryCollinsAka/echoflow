import React from "react";
import { Text } from "@fluentui/react";

const AdminDashboard = () => {
  return (
    <div>
      <Text variant="xLarge">👑 Admin Dashboard</Text>
      <p className="mt-3 text-gray-600">
        Welcome, Admin. You have full visibility across users, meetings, and summaries.
      </p>
    </div>
  );
};

export default AdminDashboard;