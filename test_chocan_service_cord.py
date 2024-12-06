import pytest
from unittest.mock import patch
from ChocAnServiceCoordinator import chocan_service_cord

# Mocking the db_client class to simulate database behavior
@pytest.fixture
def mock_database():
    with patch("ChocAnServiceCoordinator.db.db_client") as mock_db_client:
        yield mock_db_client

# Test for add_member
def test_add_member_success(mock_database):
    mock_instance = mock_database.return_value
    mock_instance.add_member.return_value = True

    service_cord = chocan_service_cord()

    with patch("ChocAnServiceCoordinator.valid.read_string", side_effect=["John Doe", "123 Main St", "New York", "NY"]):
        with patch("ChocAnServiceCoordinator.valid.read_int", side_effect=[1234567890, 12345]):
            service_cord.add_member()

    mock_instance.add_member.assert_called_once_with(
        "John Doe", 1234567890, "123 Main St", "New York", "NY", 12345
    )

# Test for remove_member
def test_remove_member_success(mock_database):
    mock_instance = mock_database.return_value
    mock_instance.remove_member.return_value = True

    service_cord = chocan_service_cord()

    with patch("ChocAnServiceCoordinator.valid.read_int", return_value=123456789):
        result = service_cord.remove_member()

    assert result is True
    mock_instance.remove_member.assert_called_once_with(123456789)

#testing provider functions.
def test_add_provider_success(mock_database):
    mock_instance = mock_database.return_value
    mock_instance.add_provider.return_value = True

    service_cord = chocan_service_cord()

    with patch("ChocAnServiceCoordinator.valid.read_string", side_effect=["Provider Name", "Fake Street", "Los Angeles", "CA"]):
        with patch("ChocAnServiceCoordinator.valid.read_int", side_effect=[9876543210, 90001]):
            result = service_cord.add_provider()

    assert result is True
    mock_instance.add_provider.assert_called_once_with(
        "Provider Name", 9876543210, "Fake Street", "Los Angeles", "CA", 90001
    )

# Test for remove_provider
def test_remove_provider_success(mock_database):
    mock_instance = mock_database.return_value
    mock_instance.remove_provider.return_value = True

    service_cord = chocan_service_cord()

    with patch("ChocAnServiceCoordinator.valid.read_int", return_value=123456789):
        result = service_cord.remove_provider()

    assert result is True
    mock_instance.remove_provider.assert_called_once_with(123456789)
