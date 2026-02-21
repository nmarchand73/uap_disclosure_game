/**
 * CUJ 2: Join an existing game.
 * User: Second player with a game ID from the host.
 * Goal: Join the game so I can play with others.
 * MOTs: Join succeeds; redirect to /game/:id; game screen loaded.
 * Creates the game via the UI first so API and browser use the same origin.
 */
import { test, expect } from "@playwright/test";

test.describe("CUJ: Join existing game", () => {
  test("player can join with a game ID and see the game screen", async ({ page }) => {
    await page.goto("/");
    await page.getByTestId("lobby-new-game").click();
    await expect(page).toHaveURL(/\/game\/[a-z0-9-]+/i);
    await expect(page.getByTestId("game-disclosure-path")).toBeVisible();
    const gameId = (await page.getByTestId("game-id").textContent())?.trim() ?? "";
    expect(gameId.length).toBeGreaterThan(0);

    await page.goto("/");
    await page.getByTestId("lobby-game-id-input").fill(gameId);
    await expect(page.getByTestId("lobby-game-id-input")).toHaveValue(gameId);
    await expect(page.getByTestId("lobby-join")).toBeEnabled();
    await page.getByTestId("lobby-join").click();

    await expect(page).toHaveURL(new RegExp(`/game/${gameId}`), { timeout: 15000 });
    await expect(page.getByTestId("game-disclosure-path")).toBeVisible();
    const alert = page.getByTestId("game-error");
    await expect(alert).not.toBeVisible();
  });
});
