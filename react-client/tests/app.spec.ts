import { test, expect } from '@playwright/test';

test.describe('Recipe App', () => {
  test('should display the main title', async ({ page }) => {
    await page.goto('/');
    
    const title = page.locator('h1');
    await expect(title).toBeVisible();
    await expect(title).toHaveText('Yet Another Recipe Site');
  });

  test('should display recipe grid', async ({ page }) => {
    await page.goto('/');
    
    await page.waitForSelector('[data-testid="recipe-grid"]', { timeout: 10000 });
    
    const recipeGrid = page.locator('[data-testid="recipe-grid"]');
    await expect(recipeGrid).toBeVisible();
    
    const recipeCards = page.locator('[data-testid="recipe-card"]');
    await expect(recipeCards).toHaveCount(3);
  });

  test('should use Dosis font for title', async ({ page }) => {
    await page.goto('/');
    
    const title = page.locator('h1');
    const fontFamily = await title.evaluate((el) => 
      getComputedStyle(el).fontFamily
    );
    
    expect(fontFamily).toContain('Dosis');
  });
});