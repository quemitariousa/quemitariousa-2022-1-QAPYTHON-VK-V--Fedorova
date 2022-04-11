from selenium.webdriver.common.by import By

PROFILE_LOGIN = (By.XPATH, '//div[contains(text(), "Войти")]')
EMAIL_INPUT = (By.NAME, 'email')
PASSWORD_INPUT = (By.NAME, 'password')
LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "authForm-module-button") and contains(text(), "Войти")]')

AUDIENCE = (By.XPATH, '//a[contains(text(), "Аудитории")]')
PROFILE = (By.XPATH, '//a[contains(text(), "Профиль")]')

LOGIN_OUT = (By.XPATH, '//div[contains(@class, "right-module-rightWrap")]')
PROFILE_LOGIN_LOGOUT = (By.XPATH, '//a[contains(@class, "rightMenu-module-rightMenuLink") and contains(@href, '
                                  '"/logout")]')

START_LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')

PROFILE_NAME_INPUT = (By.XPATH, '//div[contains(@class, "js-contacts-field-name")]/descendant::input')
PROFILE_PHONE_INPUT = (By.XPATH, '//div[contains(@class, "js-contacts-field-phone")]/descendant::input')
PROFILE_EMAIL_INPUT = (By.XPATH, '//div[contains(@class, "js-additional-email")]/descendant::input')
PROFILE_SAVE = (By.XPATH, '//button[contains(@class, "button_submit")]')
