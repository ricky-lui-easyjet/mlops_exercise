from src.common import load_data

def test_load_data():
    # Test loading CSV data
    df = load_data("src/data/train.csv")
    assert df is not None, "DataFrame should not be None"
    assert not df.empty, "DataFrame should not be empty"
    assert "Id" in df.columns, "'Id' column should be present in the DataFrame"
    assert "Species" in df.columns, "'Species' column should be present in the DataFrame"

    # Test loading unsupported data format
    try:
        load_data("src/data/train.txt", data_format="txt")
    except ValueError as e:
        assert str(e) == "Unsupported data format: txt", "Should raise ValueError for unsupported format"