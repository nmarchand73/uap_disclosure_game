import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";
import { logger } from "./utils/logger";

logger.info("App started", { dev: import.meta.env.DEV });

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
