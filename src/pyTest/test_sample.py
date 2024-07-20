import pytest
from walletclass import WalletClass


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return WalletClass()


@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return WalletClass(20)


def capitalConvert(instr):
    if not isinstance(instr, str):
        pytest.raises(TypeError)
    else:
        return instr.capitalize()


def test_capital_pass():
    assert capitalConvert('test') == 'Test'


def test_wallet_fail(empty_wallet):
    assert empty_wallet.balance != 0
