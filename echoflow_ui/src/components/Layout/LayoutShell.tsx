import React from "react";
import { Stack } from "@fluentui/react";
import Header from "./Header";
import Sidebar from "./Sidebar";

const LayoutShell = ({ children }: { children: React.ReactNode }) => {
  return (
    <Stack horizontal styles={{ root: { height: "100vh" } }}>
      <Sidebar />
      <Stack grow>
        <Header />
        <Stack grow padding={20}>
          {children}
        </Stack>
      </Stack>
    </Stack>
  );
};

export default LayoutShell;