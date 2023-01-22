
from beancount_mbank.mbank import MBankImporter


def test_main():
    importer = MBankImporter(account="Assets:MBank:Debit")
    assert importer.name() == "MBankImporter: Assets:MBank:Debit"
