"""
Minimal test: open Chrome and go to LinkedIn login.
Run this to confirm Chrome + LinkedIn work before running the full bot.

  source venv/bin/activate
  python test_open_linkedin.py
"""
import os
import ssl
import certifi

# Same SSL fix as runAiBot (needed on macOS)
os.environ.setdefault("SSL_CERT_FILE", certifi.where())
os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# Uses same Chrome/driver as the main bot (config/settings.py, config/questions.py)
from modules.open_chrome import driver

print("Opening LinkedIn login in Chrome...")
driver.get("https://www.linkedin.com/login")

print("\n>>> If you see the LinkedIn login page in Chrome, it worked! <<<\n")
print("Press Enter in this terminal to close the browser and exit.")
input()

driver.quit()
print("Done.")
