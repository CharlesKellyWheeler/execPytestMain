
def test_title(do):
    request = do[0]
    driver = do[1]
    driver.get('https://www.example.com')
    test_data = request.config.getoption('test_data')

    print(f"testing:{test_data}")
    assert driver.title == 'Example Domain'

def test_function(do):
    request = do[0]
    test_name = request.config.getoption('test_name')
    if test_name == "test_function":
        assert True
    else:
        assert False
