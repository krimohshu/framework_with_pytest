from pytest import mark

@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get('https://google.com')
    assert True

def test_env_is_qa(env):
    assert env == 'qa'

def test_env_is_dev(env):
    assert env == 'dev'