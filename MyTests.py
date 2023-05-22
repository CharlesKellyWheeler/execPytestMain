
def test_title(driver):
    driver.get('https://www.example.com')
    assert driver.title == 'Example Domain'

def test_function(request):
    test_name = request.config.getoption('test_name')
    if test_name == "test_function":
        assert True
    else:
        assert False
