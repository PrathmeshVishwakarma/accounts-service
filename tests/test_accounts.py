"""
Unit tests for the Accounts service.
"""
import unittest

from service import create_app
from service.models import Account, db

DATABASE_URI = "sqlite:///:memory:"


class TestAccountService(unittest.TestCase):
    """Account service tests."""

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(
            {
                "TESTING": True,
                "SQLALCHEMY_DATABASE_URI": DATABASE_URI,
                "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            }
        )

    def setUp(self):
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def _create_account(self, name="John Doe", email="john@example.com"):
        return self.client.post(
            "/accounts",
            json={
                "name": name,
                "email": email,
                "phone_number": "555-1234",
                "address": "123 Main St",
            },
        )

    def test_health(self):
        """The health endpoint returns OK."""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "OK")

    def test_create_account(self):
        """Creating an account returns 201 and the account payload."""
        response = self._create_account()
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIsNotNone(data["id"])
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["email"], "john@example.com")

    def test_create_account_missing_fields(self):
        """Missing required fields return 400."""
        response = self.client.post("/accounts", json={"name": "No Email"})
        self.assertEqual(response.status_code, 400)

    def test_list_accounts(self):
        """Listing accounts returns every account."""
        self._create_account()
        self._create_account(name="Jane Doe", email="jane@example.com")
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2)

    def test_list_accounts_empty(self):
        """Listing an empty database returns an empty list."""
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_read_account(self):
        """Reading an existing account returns it."""
        account_id = self._create_account().get_json()["id"]
        response = self.client.get(f"/accounts/{account_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], account_id)

    def test_read_account_not_found(self):
        """Reading a missing account returns 404."""
        response = self.client.get("/accounts/9999")
        self.assertEqual(response.status_code, 404)

    def test_update_account(self):
        """Updating an account persists the new values."""
        account_id = self._create_account().get_json()["id"]
        response = self.client.put(
            f"/accounts/{account_id}", json={"address": "456 Oak Ave"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["address"], "456 Oak Ave")

    def test_update_account_not_found(self):
        """Updating a missing account returns 404."""
        response = self.client.put("/accounts/9999", json={"address": "Nowhere"})
        self.assertEqual(response.status_code, 404)

    def test_delete_account(self):
        """Deleting an account removes it."""
        account_id = self._create_account().get_json()["id"]
        response = self.client.delete(f"/accounts/{account_id}")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.client.get(f"/accounts/{account_id}").status_code, 404)

    def test_delete_account_not_found(self):
        """Deleting a missing account returns 404."""
        response = self.client.delete("/accounts/9999")
        self.assertEqual(response.status_code, 404)

    def test_model_serialization(self):
        """The model round-trips through from_dict/to_dict."""
        account = Account()
        account.from_dict(
            {
                "name": "Ada Lovelace",
                "email": "ada@example.com",
                "phone_number": "555-0000",
                "address": "1 Analytical Way",
            }
        )
        payload = account.to_dict()
        self.assertEqual(payload["name"], "Ada Lovelace")
        self.assertEqual(payload["email"], "ada@example.com")


if __name__ == "__main__":
    unittest.main()
