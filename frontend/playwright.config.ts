import { defineConfig, devices } from "@playwright/test";

/**
 * Playwright config for Critical User Journey (CUJ) e2e tests.
 * Requires: frontend dev server (npm run dev) and API (python api/run_local.py) running.
 * Frontend proxies /api to the API; use baseURL to hit the frontend.
 */
export default defineConfig({
  testDir: "e2e",
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: 1,
  reporter: "html",
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL ?? "http://localhost:5173",
    trace: "on-first-retry",
    screenshot: "only-on-failure",
  },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
  timeout: 15000,
  expect: { timeout: 5000 },
});
