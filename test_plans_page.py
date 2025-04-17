import time

from pytest import fixture

from actions.plans_page__actions import PlansPage
from locators.plans_page_locators import PlansPageLocators

@fixture()
def page(webdriver_fixture):
    plans_page = PlansPage(driver=webdriver_fixture, url='https://ratex.ai/plans/')
    plans_page.open_page()
    time.sleep(1)
    return plans_page

def test_h1(page):
    """
        Check h1

        Reason: base smoke test
    """

    assert 'Take Control Of Your Crypto World With RateX Pro' == page.element_is_visible(locator=PlansPageLocators.H1).text

def test_pricing_default_cards_text_and_clk_buy_now(page):
    """
        Check the title of each card
        Check text of btn 'Buy Now'
        Click btn 'Buy Now'
        Check changes in url

        Reason: cards - main conversion functional
    """

    assert 'Limited Time Offer to Save!' == page.element_is_visible(locator=PlansPageLocators.FIRST_CARD_HEADER).text

    assert 'Free' == page.element_is_visible(locator=PlansPageLocators.THIRD_CARD_HEADER).text

    assert 'Pro' == page.element_is_visible(locator=PlansPageLocators.SECOND_CARD_HEADER).text

    assert 'Buy Now' == page.element_is_visible(locator=PlansPageLocators.SECOND_CARD_BTN).text

    page.js_click(element=page.element_is_clickable(locator=PlansPageLocators.SECOND_CARD_BTN))
    page.url_changed(url=page.url)
    assert 'https://ratex.ai/auth/login?next=%2Fplans%2F' == page.driver.current_url

def test_pricing_enterprise_card_text_and_clk_learn_more(page):
    """
        Check the title of Enterprise card
        Check text of btn 'Learn More'
        Click btn 'Learn More'
        Check changes in url

        Reason: card - main conversion functional
    """

    assert 'Enterprise' == page.element_is_visible(locator=PlansPageLocators.FOURTH_CARD_HEADER).text

    assert 'Learn More' == page.element_is_visible(locator=PlansPageLocators.FOURTH_CARD_BTN).text

    page.js_click(element=page.element_is_clickable(locator=PlansPageLocators.FOURTH_CARD_BTN))
    page.url_changed(url=page.url)
    assert 'https://ratex.ai/white-label/' == page.driver.current_url
