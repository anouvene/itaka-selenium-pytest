# itaka-selenium-pytest
## Installer ChromeDriverManager pour ne plus avoir de pb de version
pip3 install webdriver_manager

## Debug this: requests.exceptions.ConnectionError: Could not reach host. Are you offline?
### use this in conftest.py
import os
os.environ['WDM_SSL_VERIFY'] = '0'
