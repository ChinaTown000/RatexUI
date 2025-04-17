from pytest import fixture

from actions.plans_page__actions import PlansPage
from locators.plans_page_locators import PlansPageLocators

@fixture()
def page(webdriver_fixture):
    main_page = PlansPage(driver=webdriver_fixture, url='https://ratex.ai/plans/')
    main_page.open_page()
    return main_page

def test_h1(page):

    assert 'Take Control Of Your Crypto World With RateX Pro' == page.element_is_visible(locator=PlansPageLocators.H1).text

def test_pricing_default_cards_text_and_clk_buy_now(page):

    assert 'Limited Time Offer to Save!' == page.element_is_visible(locator=PlansPageLocators.FIRST_CARD_HEADER).text
    assert '$299' == page.element_is_visible(locator=PlansPageLocators.FIRST_CARD_PRICE).text

    assert 'Free' == page.element_is_visible(locator=PlansPageLocators.THIRD_CARD_HEADER).text

    assert 'Pro' == page.element_is_visible(locator=PlansPageLocators.SECOND_CARD_HEADER).text
    assert '$49' == page.element_is_visible(locator=PlansPageLocators.SECOND_CARD_PRICE).text.split('\n')[1].strip()
    assert '$299' == page.element_is_visible(locator=PlansPageLocators.SECOND_CARD_OLD_PRICE).text

    assert 'Buy Now' == page.element_is_visible(locator=PlansPageLocators.SECOND_CARD_BTN).text
    page.js_click(element=page.element_is_clickable(locator=PlansPageLocators.SECOND_CARD_BTN))
    page.url_changed(url=page.url)
    assert 'https://ratex.ai/auth/login?next=%2Fplans%2F' == page.driver.current_url

def test_pricing_enterprise_card_text_and_clk_learn_more(page):

    assert 'Enterprise' == page.element_is_visible(locator=PlansPageLocators.FOURTH_CARD_HEADER).text

    assert 'Learn More' == page.element_is_visible(locator=PlansPageLocators.FOURTH_CARD_BTN).text
    page.js_click(element=page.element_is_clickable(locator=PlansPageLocators.FOURTH_CARD_BTN))
    page.url_changed(url=page.url)
    assert 'https://ratex.ai/white-label/' == page.driver.current_url
