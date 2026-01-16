from selene import browser, be, have

def test_duckduckgo_search_Jefton47():
    browser.config.timeout = 10
    browser.open('https://duckduckgo.com/')

    search_input = browser.element('input[name="q"]')
    search_input.should(be.visible).type('Jefton47').press_enter()

    results = browser.all('article[data-testid="result"]')

    results.should(have.size_greater_than(0))
    results.first.should(be.visible)

    results.first.should(have.text('Jefton47'))
    browser.should(have.url_containing('Jefton47'))

def test_duckduckgo_search_JesusAVGN():
    browser.config.timeout = 10
    browser.open('https://duckduckgo.com/')

    search_input = browser.element('input[name="q"]')
    search_input.should(be.visible).type('JesusAVGN').press_enter()

    results = browser.all('article[data-testid="result"]')

    results.should(have.size_greater_than(0))
    results.first.should(be.visible)

    results.first.should(have.text('JesusAVGN'))
    browser.should(have.url_containing('JesusAVGN'))
