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
