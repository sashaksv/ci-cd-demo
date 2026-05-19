from unittest.mock import patch
from open_site import open_workua


@patch("webbrowser.open")
def test_open_workua_returns_correct_url(mock_open):
    result = open_workua()

    mock_open.assert_called_once_with("https://www.work.ua")

    assert result == "https://www.work.ua"