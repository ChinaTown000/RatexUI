from selenium.webdriver.common.by import By

class PlansPageLocators:

# pricing
    H1 = By.CSS_SELECTOR, 'body h1'
    FIRST_CARD_HEADER =By.CSS_SELECTOR, '._top_1nz6y_66 ._subtitle_1nz6y_76'
    FIRST_CARD_PRICE = By.CSS_SELECTOR, '._top_1nz6y_66 ._price_1nz6y_94'
    SECOND_CARD_HEADER = By.CSS_SELECTOR, '[class="_header_enxhy_6 _bg_enxhy_18"] > p'
    SECOND_CARD_PRICE = By.CSS_SELECTOR, '._subscriptionCard_enxhy_1 ._price_enxhy_104'
    SECOND_CARD_OLD_PRICE = By.CSS_SELECTOR, '._subscriptionCard_enxhy_1 ._oldPrice_enxhy_132'
    SECOND_CARD_BTN = By.CSS_SELECTOR, '[class="_button_85hnt_152 btn-primary btn-xxl _upgradeBtn_1ydcp_1"]'
    THIRD_CARD_HEADER = By.CSS_SELECTOR, '[class="_header_enxhy_6"] > p'
    FOURTH_CARD_HEADER = By.CSS_SELECTOR, '[class="_enterprise_1mcdz_1"] ._subtitle_1mcdz_29'
    FOURTH_CARD_BTN = By.CSS_SELECTOR, '[class="_enterprise_1mcdz_1"] > button > a'
