import pytest
from unittest.mock import MagicMock

# A simple function simulating data transformation
def process_data(spark_session):
    # In reality, this would be: spark_session.read.table(...)
    df = spark_session.createDataFrame([("Alice", 30), ("Bob", 25)], ["Name", "Age"])
    return df.filter("Age > 26")

def test_process_data_mocked():
    # 1. Create a mock Spark session and DataFrame
    mock_spark = MagicMock()
    mock_df = MagicMock()
    
    # 2. Define what the mock should return
    mock_spark.createDataFrame.return_value = mock_df
    mock_df.filter.return_value = mock_df
    mock_df.count.return_value = 1  # Simulating 1 row left after filter

    # 3. Run the function with the mock
    result_df = process_data(mock_spark)

    # 4. Assertions to verify the logic was called correctly
    mock_spark.createDataFrame.assert_called_once()
    mock_df.filter.assert_called_once_with("Age > 26")
    assert result_df.count() == 1