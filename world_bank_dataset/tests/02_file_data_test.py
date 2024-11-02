""" file data containt columns and data """
# with this test:
import pandas as pd

# Load the data
data = pd.read_csv('./data/world_bank_dataset.csv')
print(data.head())

class TestFileData:
    def test_data_head(self):
        data_head = data.head()
        assert data_head.equals(data.head()) == True