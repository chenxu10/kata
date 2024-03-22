# Composite Pattern
# Path: app_code/cleaner.py
class Cleaner:
    def __init__(self, bank, file_path):
        self.bank = bank
        self.file_path = file_path

    def change_amount_sign(self):
        if self.bank == 'chase':
            return ChaseCleaner(self.file_path).change_amount_sign()
        elif self.bank == 'bofa':
            return BofaCleaner(self.file_path).change_amount_sign()
        else:
            raise ValueError("Invalid bank name")

class ChaseCleaner(Cleaner):
    def change_amount_sign(self):
        df = pd.read_csv(self.file_path, index_col=False)
        df['Amount'] = df['Amount'] * -1
        return df

class BofaCleaner(Cleaner):
    def change_amount_sign(self):
        df = pd.read_csv(self.file_path, index_col=False)
        df['Amount'] = df['Amount'] * -1
        return df

# Path: tests/test_csvcleaner.py
import pytest
import pandas as pd
from app_code.cleaner import Cleaner

def test_cleaner():
    chasecleaner = Cleaner(
        'chase',
        'tests/data/chase_test.csv')
    actual = chasecleaner.change_amount_sign()
    expected = pd.read_csv("tests/data/chase_expected.csv", index_col=False)
    pd.testing.assert_frame_equal(actual, expected)


# Strategy Pattern
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def create_model(self):
        pass

class LSTMStrategy(Strategy):
    def create_model(self, df):
        df['Amount'] = df['Amount'] * -1
        return df

class TreeStrategy(Strategy):
    def create_model(self, df):
        df['Amount'] = df['Amount'] * -1
        return df

class ModelChooser:
    def __init__(self, model, file_path):
        self.model = model
        self.file_path = file_path
        self.strategy = self._get_strategy()

    def _get_strategy(self):
        if self.model == 'LSTM':
            return LSTMStrategy()
        elif self.model == 'Terary':
            return TreeStrategy()
        else:
            raise ValueError("Invalid model name name")

    def create_model(self):
        df = pd.read_csv(self.file_path, index_col=False)
        return self.strategy.create_model(df)


# Path: tests/test_csvcleaner.py

import pytest
import pandas as pd
from app_code.cleaner import Cleaner

def test_cleaner():
    chasecleaner = Cleaner(
        'chase',
        'tests/data/chase_test.csv')
    actual = chasecleaner.change_amount_sign()
    expected = pd.read_csv("tests/data/chase_expected.csv", index_col=False)
    pd.testing.assert_frame_equal(actual, expected)



# Decorator Pattern

class Decorator(ABC):
    @abstractmethod
    def change_amount_sign(self):
        pass

class ChaseDecorator(Decorator):
    def __init__(self, cleaner):
        self.cleaner = cleaner

    def change_amount_sign(self):
        df = self.cleaner.change_amount_sign()
        df['Amount'] = df['Amount'] * -1
        return df

class BofaDecorator(Decorator):
    def __init__(self, cleaner):
        self.cleaner = cleaner

    def change_amount_sign(self):
        df = self.cleaner.change_amount_sign()
        df['Amount'] = df['Amount'] * -1
        return df

class Cleaner:
    def __init__(self, bank, file_path):
        self.bank = bank
        self.file_path = file_path
        self.decorator = self._get_decorator()

    def _get_decorator(self):
        if self.bank == 'chase':
            return ChaseDecorator(self)
        elif self.bank == 'bofa':
            return BofaDecorator(self)
        else:
            raise ValueError("Invalid bank name")

    def change_amount_sign(self):
        df = pd.read_csv(self.file_path, index_col=False)
        return self.decorator.change_amount_sign(df)



