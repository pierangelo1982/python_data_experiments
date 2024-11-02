""" test filter_data.py """
import pandas as pd

from main import format_in_money, get_highest_gdp, get_country_with_highest_gdp

class TestFilterData:
    def test_format_in_money(self):
        assert format_in_money(1000) == "$1,000.00"
        assert format_in_money(1000000) == "$1,000,000.00"
        assert format_in_money(1000000000) == "$1,000,000,000.00"

    def test_get_highest_gdp(self):
        data = pd.DataFrame({
            'Country': ['USA', 'China', 'Japan'],
            'GDP (USD)': [1000, 2000, 3000]
        })
        assert get_highest_gdp(data) == 3000

    def test_get_country_with_highest_gdp(self):
        data = pd.DataFrame({
            'Country': ['USA', 'China', 'Japan'],
            'GDP (USD)': [1000, 2000, 3000]
        })
        assert get_country_with_highest_gdp(data) == 'Japan'

