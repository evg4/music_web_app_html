from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_index_page(db_connection, page, test_web_address):
    page.goto(f'http://{test_web_address}/')
    h1 = page.locator("h1")
    para = page.locator("p").nth(0)
    links = page.locator("a")
    expect(h1).to_have_text("Music library")
    expect(para).to_have_text("Welcome to my music library! Follow the below links to see my music collection.")
    expect(links).to_have_text(["See all artists", "See all albums"])