""" test if file csv is present and readable """

import os
import pandas as pd

class TestReadFile:
    def test_read_csv(self):
        # Load the data
        data = pd.read_csv('./data/world_bank_dataset.csv')
        assert data is not None

    def test_file_exists(self):
        assert os.path.exists('./data/world_bank_dataset.csv') == True