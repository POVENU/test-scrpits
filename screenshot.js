const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const page = await browser.newPage();

  // Log in to GitHub
  await page.goto('https://github.com/login');
  await page.type('#login_field', process.env.GITHUB_USERNAME);
  await page.type('#password', process.env.GITHUB_PASSWORD);
  await page.click('[name="commit"]');
  await page.waitForNavigation();

  // Navigate to the Secret Scanning page
  const repository = process.env.GITHUB_REPOSITORY;
  await page.goto(`https://github.com/${repository}/security/secret-scanning`);

  // Wait for the secret scanning results to load
  await page.waitForSelector('.Box-row'); // Adjust this selector to match the actual page structure

  // Take a screenshot
  await page.screenshot({ path: 'secret_scanning.png' });

  await browser.close();
})();
