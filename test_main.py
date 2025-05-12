from main import hello


def test_hello():
    assert hello('GitHub Actions') == "Hello, GitHub Actions!"
    

def test_hello_custom_name():
    assert hello('Sylvain') == "Hello, Sylvain!"
