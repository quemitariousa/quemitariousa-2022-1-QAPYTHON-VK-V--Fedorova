from selenium.webdriver.common.by import By


class BasePageLocators(object):
    PROFILE_LOGIN = (By.XPATH, '//div[contains(text(), "Войти")]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "authForm-module-button") and contains(text(), "Войти")]')
    SPINNER = (By.XPATH, '//div[@class="spinner spinner_large"]')

class LoginPageLocators(BasePageLocators):
    PROFILE_LOGIN = (By.XPATH, '//div[contains(text(), "Войти")]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "authForm-module-button") and contains(text(), "Войти")]')
    PROFILE_LOGIN_LOGOUT = (By.XPATH, '//a[contains(@href, "logout")]')
    AUDIENCE = (By.XPATH, '//a[contains(text(), "Аудитории")]')
    LOGIN_OUT = (By.XPATH, '//div[contains(@class, "right-module-rightWrap")]')


class DashboardPageLocators(BasePageLocators):
    PROFILE = (By.XPATH, '//a[contains(text(), "Профиль")]')
    COMPANY = (By.XPATH, '//a[contains(text(), "Кампании")]')
    AUDIENCE = (By.XPATH, '//a[contains(text(), "Аудитории")]')
    LOGIN_OUT = (By.XPATH, '//div[contains(@class, "right-module-rightWrap")]')
    PROFILE_LOGIN_LOGOUT = (By.XPATH, '//a[contains(@class, "rightMenu-module-rightMenuLink") and contains(@href, '
                                      '"/logout")]')


class CompaignPageLocators(BasePageLocators):
    PROFILE = (By.XPATH, '//a[contains(text(), "Профиль")]')
    СOMPAIGN = (By.XPATH, '//a[contains(text(), "Кампании")]')
    AUDIENCE = (By.XPATH, '//a[contains(text(), "Аудитории")]')
    LOGIN_OUT = (By.XPATH, '//div[contains(@class, "right-module-rightWrap")]')
    PROFILE_LOGIN_LOGOUT = (By.XPATH, '//a[contains(@class, "rightMenu-module-rightMenuLink") and contains(@href, '
                                      '"/logout")]')

    START_LOGIN_BUTTON = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')

    PROFILE_NAME_INPUT = (By.XPATH, '//div[contains(@class, "js-contacts-field-name")]/descendant::input')
    PROFILE_PHONE_INPUT = (By.XPATH, '//div[contains(@class, "js-contacts-field-phone")]/descendant::input')
    PROFILE_EMAIL_INPUT = (By.XPATH, '//div[contains(@class, "js-additional-email")]/descendant::input')
    PROFILE_SAVE = (By.XPATH, '//button[contains(@class, "button_submit")]')

    AUDIENCE = (By.XPATH, '//a[contains(text(), "Аудитории")]')
    CREATE_NEW_СOMPAIGN = (By.XPATH, '//div[contains(text(), "Создать кампанию")]')
    NEW_СOMPAIGN_TRAFFIC = (By.XPATH, '//div[contains(@class, "column-list-item _traffic")]')
    INPUT_URL = (By.XPATH, '//input[contains(@placeholder, "Введите ссылку")]')
    FORMAT_СOMPAIGN = (By.XPATH, '//div[contains(@id, "patterns_banner_4")]')
    NAME_СOMPAIGN = (By.XPATH, './/div[contains(@class, "input_campaign-name")]/descendant::input')
    INPUT_BUDGET_PER_DAY = (By.XPATH, '//div[contains(@class, "js-budget-setting-daily")]/descendant::input')
    INPUT_BUDGET_ALL = (By.XPATH, '//div[contains(@class, "budget-setting__input-wrap '
                                  'js-budget-setting-total")]/descendant::input')
    UPLOAD_PICTURE = (By.XPATH, '//div[contains(@class, "bannerForm-module-roleInline")]/descendant::input')
    SAVE_UPLOAD_PICTURE = (By.XPATH, '//input[contains(@class, "image-cropper__save js-save")]')
    SAVE_СOMPAIGN = (By.XPATH, '//div[contains(text(), "Создать кампанию")]/parent::button')
    MY_СOMPAIGN_NAME_IN_LIST = ()
    TEST_FILE_INPUT = (By.XPATH, '//input[contains(@type, "file") and contains(@data-test, "image_240x400")]')
    TEST_FILE_CLICK = (By.XPATH, './/input[@type="file" and @data-test="image_240x400"]')


class SegmentLocators(object):
    CREATE_FIRST_SEGMENT = (By.XPATH, '//a[contains(@href, "/segments/segments_list/new/")]')
    CREATE_SECOND_SEGMENT = (By.XPATH, "//div[contains(@class, 'button__text')]")
    CREATE_NEW_SEGMENT = (By.XPATH, '//button[contains(@class, "button_submit")]')
    APPS_AND_GAMES_SEGMENT = (By.XPATH, './/div[contains(text(), "Приложения и игры в соцсетях")]')
    PLAYED_AND_PAYED_BUTTON = (By.XPATH, './/input[contains(@class, "adding-segments-source__checkbox ")]')
    SAVE_NEW_SEGMENT = (By.XPATH, './/div[@class="button__text" and contains(text(), "Добавить сегмент")]')
    INPUT_NAME_SEGMENT = (By.XPATH, './/div[@class="js-segment-name"]//input')
    SUBMIT_SEGMENT = (By.XPATH, "//div[@class='create-segment-form']//div[contains(text(),'Создать сегмент')]")
    MY_SEGMENT_NAME_IN_LIST = ()

    SEARCH_OF_SEGMENTS = (By.XPATH, '//input[@placeholder="Поиск по названию или id..."]')
    CHECKBOX_ALL_DELETE = (
        By.XPATH, "//div[@class='segmentsTable-module-idHeaderCellWrap-1M1sHd']//input[@type='checkbox']")
    ACTION_LIST = (By.XPATH, '//span[contains(text(), "Действия")]')
    ACTION_LIST_DELETE = (By.XPATH, '//li[contains(text(), "Удалить")]')
