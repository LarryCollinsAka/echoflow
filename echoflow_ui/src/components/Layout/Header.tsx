import React from "react";
import { Stack, Text } from "@fluentui/react";

const Header = () => (
  <Stack horizontal verticalAlign="center" padding={10} styles={{ root: { background: "#f3f3f3" } }}>
    <Text variant="large" styles={{ root: { fontWeight: 600 } }}>
      EchoFlow
    </Text>
  </Stack>
);

export default Header;