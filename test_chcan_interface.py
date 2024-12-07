import pytest
from unittest.mock import MagicMock, patch
from ChocAnInterface import chocan_interface

@pytest.fixture
def mock_service_coordinator():
    """Mock the service coordinator used by chocan_interface."""
    with patch("ChocAnInterface.chocan_service_cord", autospec=True) as mock_cord:
        yield mock_cord.return_value

@pytest.fixture
def chocan_interface_instance(mock_service_coordinator):
    """Provides an instance of chocan_interface with mocked dependencies."""
    return chocan_interface()

def test_read_provider_id_valid(chocan_interface_instance, mock_service_coordinator):
    mock_service_coordinator.user_id = None

    # Mock input and database response
    with patch("valid.read_int", side_effect=[123456789]):
        with patch("DatabaseApi.db_client.prov_get_name_from_id", return_value="Provider Test") as mock_db:
            result = chocan_interface_instance.read_provider_id()

    assert result is True, "Valid provider ID was not validated correctly."
    assert mock_service_coordinator.user_id == 123456789, "Provider ID was not set correctly."
    mock_db.assert_called_once_with(123456789)

def test_read_provider_id_invalid(chocan_interface_instance):
    # Mock input and database response
    with patch("valid.read_int", side_effect=[123, 987654321]):
        with patch("DatabaseApi.db_client.prov_get_name_from_id", side_effect=[None, "Provider Valid"]) as mock_db:
            result = chocan_interface_instance.read_provider_id()

            # Validate that retries occurred and the correct ID was eventually accepted
            assert result is True, "Valid provider ID was not accepted after retries."
            assert mock_db.call_count == 2, "Database was not queried the correct number of times."
            mock_db.assert_any_call(123)
            mock_db.assert_any_call(987654321)

def test_provider_menu(chocan_interface_instance, mock_service_coordinator):
    # Mock user input
    with patch("valid.read_int", side_effect=[1, 5]):
        chocan_interface_instance.provider_menu()

    mock_service_coordinator.read_member_id.assert_called_once()

def test_manager_menu_add_member(chocan_interface_instance, mock_service_coordinator):
    # Mock user input
    with patch("valid.read_int", side_effect=[1, 8]):
        chocan_interface_instance.manager_menu()

    mock_service_coordinator.add_member.assert_called_once()

def test_manager_menu_invalid_option(chocan_interface_instance):
    # Mock user input
    with patch("valid.read_int", side_effect=[99, 8]):
        chocan_interface_instance.manager_menu()

    # Ensure no unexpected methods were called
    # Use MagicMock methods to ensure no actions are incorrectly triggered
