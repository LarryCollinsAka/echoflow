import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { initializeIcons } from "@fluentui/react";
import LoginForm from "./pages/Login";
import DashboardRouter from "./pages/dashboard/DashboardRouter";
import LayoutShell from "./components/Layout/LayoutShell";

initializeIcons();

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginForm />} />

        {/* All dashboard routes go through LayoutShell */}
        <Route
          path="/dashboard/*"
          element={
            <LayoutShell>
              <DashboardRouter />
            </LayoutShell>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;