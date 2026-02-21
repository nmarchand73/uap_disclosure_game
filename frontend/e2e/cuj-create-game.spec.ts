/**
 * CUJ 1: Create a new game (solo) and reach the game screen.
 * User: First-time or returning player (solo).
 * Goal: Create a game so I can see the game board and take my first turn.
 * MOTs: Create game succeeds; redirect to /game/:id; game screen visible.
 */
import { test, expect } from "@playwright/test";

test.describe("CUJ: Create game (solo) and reach game screen", () => {
  test("first-time player can create a game and see the game screen", async ({ page }) => {
    await page.goto("/");

    await page.getByTestId("lobby-new-game").click();

    await expect(page).toHaveURL(/\/game\/[a-z0-9-]+/i);
    await expect(page.getByTestId("game-disclosure-path")).toBeVisible();
    await expect(page.getByTestId("game-phase")).toContainText(/lobby|movement|end_turn|spinner/i);
  });
});
