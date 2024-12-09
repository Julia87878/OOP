import json
from unittest.mock import MagicMock, patch

from src.utils import read_json


@patch("builtins.open")
def test_read_json(mock_open: MagicMock, path_name: str) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert read_json(path_name) == [{"test": "test"}]
