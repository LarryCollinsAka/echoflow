import React from "react";
import { Text } from "@fluentui/react";

const StudentDashboard = () => {
  return (
    <div>
      <Text variant="xLarge">Student Dashboard</Text>
      <p className="mt-3 text-gray-600">
        Welcome, Student. You have full visibility across summaries.
      </p>
    </div>
  );
};

export default StudentDashboard;