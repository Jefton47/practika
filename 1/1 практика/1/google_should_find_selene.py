from selene import browser, be, have

browser.config.driver_name = "edge"
browser.open('https://duckduckgo.com/')
browser.element('[name="q"]').should(be.blank).type('Jefton47').press_enter()
browser.element('html').should(have.text('Jefton47'))
print("Test completed successfully.")

