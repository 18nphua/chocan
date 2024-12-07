import pytest
import sqlite3
from DatabaseApi import db_client

@pytest.fixture
def test_db():
    """Creates a temporary in-memory SQLite database for testing."""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create tables for testing
    cursor.execute('''CREATE TABLE members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone_number INTEGER,
        street_address TEXT,
        city TEXT,
        state TEXT,
        zip_code INTEGER,
        last_payment_date TEXT,
        status TEXT,
        balance REAL
    )''')

    cursor.execute('''CREATE TABLE providers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone_number TEXT,
        street_address TEXT,
        city TEXT,
        state TEXT,
        zip_code INTEGER
    )''')

    cursor.execute('''CREATE TABLE services (
        service_code INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        fee REAL
    )''')

    cursor.execute('''CREATE TABLE services_provided_log (
        date_service_logged TEXT,
        date_service_provided TEXT,
        provider_id INTEGER,
        member_id INTEGER,
        member_name TEXT,
        s_code INTEGER,
        fee REAL
    )''')

    conn.commit()
    yield conn
    conn.close()

@pytest.fixture
def db_client_with_test_db(test_db):
    client = db_client()
    client.db = test_db
    client.cur = test_db.cursor()
    return client

def test_add_member(db_client_with_test_db):
    client = db_client_with_test_db

    # Add a member
    result = client.add_member("Alice", 1234567890, "123 Choco Lane", "Cocoa City", "Choco State", 12345)
    assert result is True, "Failed to add a new member."

    # Verify the member exists
    client.cur.execute("SELECT * FROM members WHERE name = ?", ("Alice",))
    member = client.cur.fetchone()
    assert member is not None, "Member not found in the database."

def test_add_duplicate_member(db_client_with_test_db):
    client = db_client_with_test_db

    # Add a member
    client.add_member("Bob", 9876543210, "456 Cocoa Blvd", "Cocoa City", "Choco State", 67890)
    
    # Try adding the same member again
    result = client.add_member("Bob", 9876543210, "456 Cocoa Blvd", "Cocoa City", "Choco State", 67890)
    assert result is False, "Duplicate member was incorrectly added."

def test_remove_member(db_client_with_test_db):
    client = db_client_with_test_db

    # Add and remove a member
    client.add_member("Charlie", 1122334455, "789 Cocoa Road", "Choco Town", "Sweet State", 54321)
    client.cur.execute("SELECT id FROM members WHERE name = ?", ("Charlie",))
    member_id = client.cur.fetchone()[0]

    result = client.remove_member(member_id)
    assert result is True, "Failed to remove the member."

    # Verify the member was removed
    client.cur.execute("SELECT * FROM members WHERE id = ?", (member_id,))
    member = client.cur.fetchone()
    assert member is None, "Member was not removed from the database."

def test_add_service(db_client_with_test_db):
    client = db_client_with_test_db

    # Add a service
    result = client.add_service("Chocolate Therapy", 50.00)
    assert result is True, "Failed to add a new service."

    # Verify the service exists
    client.cur.execute("SELECT * FROM services WHERE name = ?", ("Chocolate Therapy",))
    service = client.cur.fetchone()
    assert service is not None, "Service not found in the database."

def test_remove_service(db_client_with_test_db):
    client = db_client_with_test_db

    # Add and remove a service
    client.add_service("Cocoa Massage", 100.00)
    client.cur.execute("SELECT service_code FROM services WHERE name = ?", ("Cocoa Massage",))
    service_code = client.cur.fetchone()[0]

    result = client.remove_service(service_code)
    assert result is True, "Failed to remove the service."

    # Verify the service was removed
    client.cur.execute("SELECT * FROM services WHERE service_code = ?", (service_code,))
    service = client.cur.fetchone()
    assert service is None, "Service was not removed from the database."
