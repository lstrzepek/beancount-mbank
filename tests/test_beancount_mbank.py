
from beancount_mbank.cli import main


def test_main():
    assert main([]) == 0
