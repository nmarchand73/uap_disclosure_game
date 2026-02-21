/**
 * CUJ 3: Complete one turn (roll dice and move).
 * User: Player in an existing game (their turn).
 * Goal: Roll dice and move so I can advance on the board.
 * MOTs: Move action succeeds; phase and turn_state update in UI.
 * Creates the game via the UI so API and browser use the same origin.
 */
import { test, expect } from "@playwright/test";

test.describe("CUJ: Play one turn (roll dice & move)", () => {
  test("player can roll dice and see phase update", async ({ page }) => {
    await page.goto("/");
    await page.getByTestId("lobby-new-game").click();
    await expect(page).toHaveURL(/\/game\/[a-z0-9-]+/i);
    await expect(page.getByTestId("game-disclosure-path")).toBeVisible();
    await expect(page.getByTestId("game-roll-dice")).toBeVisible();

    const actionResponse = page.waitForResponse(
      (res) => res.url().includes("/action") && res.request().method() === "POST",
      { timeout: 15000 }
    );
    await page.getByTestId("game-roll-dice").click();
    const res = await actionResponse;
    expect(res.status(), "Move action should succeed (API must be running)").toBe(200);

    await expect(page.getByTestId("game-phase")).toContainText(/spinner|end_turn/i, { timeout: 10000 });
    const errorEl = page.getByTestId("game-error");
    await expect(errorEl).not.toBeVisible();
    await expect(
      page.getByText(/Dice:|No event card matches|Spinner:|Government|Military|Scientific/i)
    ).toBeVisible({ timeout: 5000 });
  });
});
